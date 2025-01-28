# 📧 Classificador de Emails Produtivos e Improdutivos

Este projeto é uma aplicação **Flask** que classifica emails como **"Produtivo"** ou **"Improdutivo"** utilizando a API da **OpenAI** e gera uma resposta profissional para o email enviado.

## 📌 Funcionalidades
- Classificação de emails como **produtivo** ou **improdutivo**.
- Upload de arquivos **.txt** e **.pdf** para análise.
- Geração automática de uma **resposta profissional** com base na classificação.
- Interface simples utilizando **Flask**.

---

## 🏗 Estrutura do Projeto

```
📂 MeuProjeto/
│-- README.md
│-- app.py
│-- requirements.txt
│-- .env (não enviado ao GitHub, ver Configuração)
│-- 📂 templates/
│   └── index.html
│-- 📂 tests/
│   ├── improd1.txt
│   ├── improd2.txt
│   ├── prod1.pdf
│   ├── prod1.txt
│   └── prod2.txt
│-- 📂 uploads/ (armazenamento de arquivos enviados)
```

---

## 🚀 Configuração e Execução

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/ThiagoLahass/Classificador-de-Emails-com-API-da-OpenAI
cd Classificador-de-Emails-com-API-da-OpenAI
```

### 2️⃣ Criar e Ativar um Ambiente Virtual (Opcional)
```sh
python -m venv venv       # Criar ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar a Chave da API OpenAI
Crie um arquivo **.env** na raiz do projeto e adicione sua chave da API:
```
API_KEY=sua_chave_aqui
```
> ⚠ **Importante**: Nunca compartilhe sua chave da API publicamente!

### 5️⃣ Executar a Aplicação
```sh
python app.py
```
Acesse em **http://127.0.0.1:5000/** no navegador.

---

## 📝 Principais Componentes

### 🔹 `app.py`
- Configura a API OpenAI via **dotenv**.
- Gerencia uploads de arquivos.
- Processa arquivos **.txt** e **.pdf** para extração de texto.
- Classifica emails usando **GPT-4o-mini**.
- Gera uma resposta automática com base na classificação.

### 🔹 `templates/index.html`
- Interface simples para envio de emails e arquivos.

### 🔹 `uploads/`
- Armazena temporariamente os arquivos enviados pelos usuários.

### 🔹 `tests/`
- Arquivos de exemplo para testar a classificação.

---

## 🛠 Tecnologias Utilizadas
- **Flask**: Framework web para Python.
- **OpenAI API**: Para classificação e geração de respostas.
- **dotenv**: Gerenciamento seguro de variáveis de ambiente.
- **PyPDF2**: Extração de texto de arquivos PDF.
- **Werkzeug**: Segurança no upload de arquivos.

---

## 📌 Observações
- Para implantar a aplicação em produção, configure **variáveis de ambiente seguras** e desative o modo `debug`.
- Você pode integrar a aplicação com um **frontend mais elaborado** para uma melhor experiência do usuário.

---

## 📜 Licença
Este projeto é distribuído sob a licença **MIT**. Sinta-se livre para utilizá-lo e melhorá-lo! 🎉
