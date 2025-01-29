from flask import Flask, render_template, request, jsonify
import openai
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import logging
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(level=logging.DEBUG)

# Inicialização do Flask
app = Flask(__name__)

# Configuração da chave de API OpenAI
load_dotenv()
openai.api_key = os.getenv("API_KEY")

# Configurações para upload de arquivos
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Verifica se o arquivo enviado é de um formato permitido.

    Parâmetros:
        `filename (str)`: O nome do arquivo enviado.

    Retorna:
        `bool`: `True` se o arquivo é permitido, `False` caso contrário.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file_path):
    """
    Extrai texto de arquivos .txt ou .pdf.

    `Parâmetros`:
        `file_path (str)`: Caminho completo para o arquivo.

    `Retorna`:
        `str`: Texto extraído do arquivo.
    """
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        pdf_reader = PdfReader(file_path)
        return " ".join([page.extract_text() for page in pdf_reader.pages])
    return ""

@app.route("/")
def home():
    """
    Rota principal que renderiza a página inicial.

    `Retorna`:
        `str`: O conteúdo `HTML` da página inicial.
    """
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def classify_email():
    """
    `Endpoint` para classificar emails como 'Produtivo' ou 'Improdutivo' e gerar uma resposta profissional.

    `Retorna`:
        `Response`: Uma resposta `JSON` contendo a classificação e a resposta gerada.

    `Erros`:
        `400`: Se nenhum texto ou arquivo válido for fornecido.
        `500`: Se ocorrer um erro no processamento da solicitação.
    """
    try:
        logging.debug("Recebendo solicitação no endpoint /classify")

        email_content = None

        # Processamento de arquivo enviado
        if "file" in request.files:
            file = request.files["file"]
            if file and allowed_file(file.filename):
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(file_path)
                email_content = extract_text_from_file(file_path)
            else:
                return jsonify({"error": "Arquivo inválido. Apenas .txt ou .pdf são aceitos."}), 400

        # Processamento de texto enviado diretamente
        elif "email" in request.form:
            email_content = request.form["email"]

        # Caso nenhum conteúdo válido seja enviado
        if not email_content:
            return jsonify({"error": "Nenhum texto ou arquivo válido foi fornecido."}), 400

        logging.debug(f"Conteúdo do email recebido: {email_content}")

        # Classificação do email via API OpenAI
        classification_response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Classifique emails como 'Produtivo' ou 'Improdutivo'."},
                {"role": "user", "content": f"Classifique o seguinte email:\n\n{email_content}\n\nClassificação:"}
            ],
            max_tokens=10
        )
        classification = classification_response["choices"][0]["message"]["content"].strip()
        logging.debug(f"Classificação obtida: {classification}")

        # Geração de resposta profissional com base na classificação
        response_prompt = f"Baseado na classificação '{classification}', sugira uma resposta profissional para este email:\n\n{email_content}\n\nResposta:"
        response_suggestion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Gere respostas profissionais para emails."},
                {"role": "user", "content": response_prompt}
            ],
            max_tokens=200
        )
        response = response_suggestion["choices"][0]["message"]["content"].strip()
        logging.debug(f"Resposta gerada: {response}")

        return jsonify({
            "classification": classification,
            "response": response
        })

    except Exception as e:
        logging.error(f"Erro no servidor: {e}", exc_info=True)
        return jsonify({"error": "Ocorreu um erro no processamento da solicitação."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))