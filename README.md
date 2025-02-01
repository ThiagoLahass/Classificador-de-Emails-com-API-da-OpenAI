# 📧 Classificador de Emails Produtivos e Improdutivos

Este projeto é uma aplicação **Flask** que classifica emails como **"Produtivo"** ou **"Improdutivo"** utilizando a API da **OpenAI** e gera uma resposta profissional para o email enviado.

## 📌 Funcionalidades
- Classificação de emails como **produtivo** ou **improdutivo**.
- Upload de arquivos **.txt** e **.pdf** para análise.
- Geração automática de uma **resposta profissional** com base na classificação.
- Interface simples utilizando **Flask**.

---

## 🏷 Estrutura do Projeto

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

### 1⃣ Clonar o Repositório
```sh
git clone https://github.com/ThiagoLahass/Classificador-de-Emails-com-API-da-OpenAI
cd Classificador-de-Emails-com-API-da-OpenAI
```

### 2⃣ Criar e Ativar um Ambiente Virtual (Opcional)
```sh
python -m venv venv       # Criar ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3⃣ Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4⃣ Configurar a Chave da API OpenAI
Crie um arquivo **.env** na raiz do projeto e adicione sua chave da API:
```
API_KEY=sua_chave_aqui
```
> ⚠ **Importante**: Nunca compartilhe sua chave da API publicamente!

### 5⃣ Executar a Aplicação
```sh
python app.py
```
Acesse em **http://127.0.0.1:5000/** no navegador.

---

## 📝 Deploy na Railway

### 1⃣ Criar uma Conta na Railway
Acesse [Railway.app](https://railway.app/) e crie uma conta ou faça login.

### 2⃣ Criar um Novo Projeto
- Clique em "New Project" e escolha "Deploy from GitHub".
- Conecte seu repositório do GitHub ao Railway.

### 3⃣ Configurar as Variáveis de Ambiente
- No painel do Railway, acesse a aba **"Variables"**.
- Adicione a chave da API OpenAI:
  ```
  API_KEY=sua_chave_aqui
  ```

### 4⃣ Configurar o Service
- No Railway, sua aplicação precisará de um **Procfile** para definir como rodar o Flask.
- Crie um arquivo chamado `Procfile` no diretório raiz do projeto e adicione:
  ```
  web: python app.py
  ```

### 5⃣ Definir a Porta no `app.py`
A Railway usa a variável de ambiente `PORT`. Atualize `app.py` para utilizar essa porta:
```python
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
```

### 6⃣ Implantar o Projeto
- Clique em **Deploy** e aguarde a conclusão.
- Acesse o link gerado pela Railway para testar sua aplicação online.

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

## ⭐ Agradecimento
Se você gostou deste projeto, por favor, deixe uma ⭐ no repositório! Isso motiva a continuar melhorando e trazendo mais aplicações legais. Obrigado pelo seu apoio! 🙌