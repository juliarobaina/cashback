# 💸 Cashback API + Frontend

![Python](https://img.shields.io/badge/python-3.14-red)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-blue)
![Frontend](https://img.shields.io/badge/frontend-JS%20puro-yellow)
![Status](https://img.shields.io/badge/status-finalizado-success)

Sistema completo para cálculo de cashback com histórico por IP.

---
## 🚀 Demo

### 🔗 API (Swagger)  
https://cashback-0j64.onrender.com/docs  

### 🔗 Frontend  
https://juliarobaina.github.io/frontend_api_cashback/

---

## 🧠 Visão Geral

Este projeto implementa uma API para cálculo de cashback com persistência em banco de dados e um frontend simples para interação com o usuário.

A aplicação foi construída seguindo uma separação clara de responsabilidades:

- Frontend → interface e validação de entrada
- Backend (FastAPI) → API REST
- Service Layer → regras de negócio
- Database Layer → persistência desacoplada
- Deploy em ambiente real (Render + Railway + GitHub Pages)

---

## 🏗️ Arquitetura

```text
backend/
├── app.py           # Inicialização da aplicação
├── routes.py        # Controllers (endpoints)
├── services.py      # Regras de negócio (cashback)
├── models.py        # Modelo da tabela (SQLModel)
├── schemas.py       # Validação e modelos (SQLModel)
├── database.py      # Conexão com banco
├── settings.py      # Configuração via .env
├── requirements.txt # Dependências
└── .env.example     # Arquivo de exemplo para o .env com variáveis de ambiente

frontend/
├── index.html
├── index.css
└── api_data.js       # Consumo da API + lógica JS

calcular_cashback.py  # Execução via terminal do cálculo do cashback
```
---

## ⚙️ Tecnologias
<ul>
  <li>Backend
    <ul>
      <li>FastAPI</li>
      <li>SQLModel</li>
      <li>MySQL</li>
    </ul>
  </li>
</ul>
<ul>
  <li>Frontend
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript puro</li>
    </ul>
  </li>
</ul>
<ul>
  <li>Deploy
    <ul>
      <li>API → Render</li>
      <li>Banco → Railway</li>
      <li>Frontend → GitHub Pages</li>
    </ul>
  </li>
</ul>

---

## 🔥 Funcionalidades
- ✅ Cálculo de cashback com regras de negócio
- ✅ Persistência em banco de dados
- ✅ Histórico de consultas por IP
- ✅ Validação no frontend e backend
- ✅ Formatação de valores (pt-BR)
- ✅ API documentada automaticamente (Swagger)

---

## 💡 Regras de Negócio

A lógica de cálculo está isolada em:

services.py

Isso garante:

- Reutilização
- Testabilidade
- Separação entre HTTP e domínio

---

## 🔐 Variáveis de Ambiente

O arquivo .env.example é um arquivo de exemplo com as variáveis de ambiente que o arquivo .env deve ter:

```text
# Example MySQL
DB_TYPE=mysql
DB_DRIVER=pymysql
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_database

# Example Settings Uvicorn
HOST_IP=127.0.0.1
PORT=8000
```
Essas variáveis são carregadas via settings.py, evitando hardcode e deixando o projeto mais seguro.

---

## 🧪 Execução Local
### Backend
<p>🔧 Instalar dependências</p>

`pip install -r requirements.txt`
<p>▶️ 2. Executar a API</p>

`uvicorn app:app --reload` ou `python app.py`

### Frontend
Abrir index.html

---

## 🌐 Frontend

O frontend:

- Consome a API via fetch
- Aplica validações em JavaScript
- Formata valores no padrão brasileiro
- Converte valores para o formato aceito pelo backend

---

## 🧾 Algoritmo Cashback

O arquivo abaixo contém somente o algoritmo para o cálculo do cashback:

<p>▶️ Executar:</p>

`python calcular_cashback.py`

---

## 🗄️ Banco de Dados
- Tipo: MySQL
- Hospedagem: Railway
- Integração via variáveis de ambiente

Uso de SQLModel permite abstração e flexibilidade para troca de banco.

---
## 📌 Destaques
- Separação clara de camadas
- Uso de variáveis de ambiente
- Máscara e tratamento de valores monetários
- Deploy completo (frontend + backend + banco)

