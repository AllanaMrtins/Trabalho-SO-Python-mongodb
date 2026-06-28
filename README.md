<div align="center">

# 🎓 SIGMON
### Sistema de Gerenciamento de Monitoria

*Aplicação web para cadastro de alunos, monitores e atendimentos acadêmicos com banco de dados distribuído.*

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.1-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-8.0-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Swarm-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

## 📌 Sobre o projeto

O **SIGMON** é uma aplicação web desenvolvida em Python com Flask para gerenciar o sistema de monitoria de uma instituição de ensino. Permite o cadastro e listagem de **alunos**, **monitores** e **atendimentos**, além de um **dashboard** com contadores em tempo real.

O banco de dados utiliza **MongoDB com Replica Set de 3 nós** para garantir alta disponibilidade e persistência dos dados, orquestrado com **Docker Swarm**.

---

## ✨ Funcionalidades

| Módulo | Descrição |
|---|---|
| 👨‍🎓 **Alunos** | Cadastro com nome, e-mail, curso, período e disciplinas |
| 🧑‍🏫 **Monitores** | Cadastro com disciplina, docente e período |
| 📋 **Atendimentos** | Registro com vínculo automático ao monitor da disciplina |
| 📊 **Dashboard** | Painel com totais de alunos, monitores e atendimentos |

---

## 🛠️ Stack utilizada

- **Python 3.13** — linguagem principal
- **Flask 3.1.1** — framework web com Blueprints e Jinja2
- **MongoDB 8.0** — banco NoSQL com Replica Set de 3 nós (`rs0`)
- **PyMongo 4.13.2** — driver oficial para comunicação com o MongoDB
- **Docker + Docker Swarm** — containerização e orquestração com alta disponibilidade
- **Mongo Express** — interface visual para administração do MongoDB (porta 8081)

---

## 📁 Estrutura do projeto

```
Trabalho-SO-Python-mongodb/
├── app.py                        # Entry-point da aplicação Flask
├── requirements.txt              # Dependências Python
│
├── config/
│   └── settings.py               # MONGO_URI, DATABASE_NAME, SECRET_KEY
│
├── database/
│   ├── connection.py             # Singleton de conexão com MongoDB
│   └── replica_set.py            # Status do Replica Set
│
├── models/
│   ├── aluno.py                  # Classe Aluno com to_dict()
│   ├── monitor.py                # Classe Monitor com to_dict()
│   └── atendimento.py            # Classe Atendimento com to_dict()
│
├── repositories/
│   ├── aluno_repository.py
│   ├── monitor_repository.py
│   └── atendimento_repository.py
│
├── services/
│   ├── aluno_service.py
│   ├── monitor_service.py
│   ├── atendimento_service.py
│   └── dashboard_service.py
│
├── controllers/
│   ├── aluno_controller.py
│   ├── monitor_controller.py
│   ├── atendimento_controller.py
│   └── dashboard_controller.py
│
├── routes/
│   ├── alunos_routes.py
│   ├── monitores_routes.py
│   ├── atendimentos_routes.py
│   └── dashboard_routes.py
│
├── templates/                    # HTML Jinja2
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── alunos.html
│   ├── monitores.html
│   └── atendimentos.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── docker/
    ├── Dockerfile
    ├── docker-compose.yml        # Ambiente local
    ├── docker-stack.yml          # Produção com Docker Swarm
    └── init-replica.js           # Inicialização do Replica Set
```

---

## 🗄️ Modelos de dados

<details>
<summary><strong>👨‍🎓 Aluno</strong></summary>

| Campo | Tipo |
|---|---|
| `matricula` | string |
| `nome` | string |
| `email` | string |
| `curso` | string |
| `periodo` | int |
| `disciplinas` | string |

</details>

<details>
<summary><strong>🧑‍🏫 Monitor</strong></summary>

| Campo | Tipo |
|---|---|
| `matricula` | string |
| `nome` | string |
| `email` | string |
| `disciplina` | string |
| `horario` | string |

</details>

<details>
<summary><strong>📋 Atendimento</strong></summary>

| Campo | Tipo |
|---|---|
| `aluno_matricula` | string |
| `monitor_matricula` | string |
| `disciplina` | string |
| `data` | string |
| `horario` | string |
| `local` | string |
| `descricao` | string |
| `status` | string |

</details>

---

## 🌐 Rotas da aplicação

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Tela de login |
| `POST` | `/` | Autenticação e redirecionamento ao dashboard |
| `GET` | `/dashboard-page` | Painel com totais em tempo real |
| `GET` | `/alunos-page` | Listagem de alunos |
| `POST` | `/alunos-page` | Cadastro de novo aluno |
| `GET` | `/monitores-page` | Listagem de monitores |
| `POST` | `/monitores-page` | Cadastro de novo monitor |
| `GET` | `/atendimentos-page` | Listagem de atendimentos |
| `POST` | `/atendimentos-page` | Registro com vínculo automático ao monitor |
| `GET` | `/api/dashboard` | API JSON com contadores do dashboard |
| `GET` | `/api/replica-status` | Status do Replica Set MongoDB |

---

## 🏗️ Infraestrutura

```
┌─────────────────────────────────────────────┐
│              Docker Swarm / Compose          │
│                                             │
│  ┌──────────────┐     ┌──────────────────┐  │
│  │  sigmon_app  │     │  mongo-express   │  │
│  │  :5000 (×2) │     │     :8081        │  │
│  └──────┬───────┘     └────────┬─────────┘  │
│         │                      │            │
│         └──────────┬───────────┘            │
│                    │                        │
│        ┌───────────▼──────────┐             │
│        │   Replica Set rs0    │             │
│   ┌────┴────┐ ┌────┴────┐ ┌──┴──────┐      │
│   │ mongo1  │ │ mongo2  │ │ mongo3  │      │
│   │ :27017  │ │ :27018  │ │ :27019  │      │
│   └─────────┘ └─────────┘ └─────────┘      │
└─────────────────────────────────────────────┘
```

String de conexão:
```python
MONGO_URI = "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"
DATABASE_NAME = "sigmon"
```

---

## 🚀 Como executar

### Com Docker Compose (desenvolvimento local)

```bash
# Sobe todos os serviços (app + 3 nós MongoDB)
docker compose -f docker/docker-compose.yml up --build
```

Acesse em: **http://localhost:5000**

---

### Com Docker Swarm (produção)

```bash
# Inicializa o swarm (apenas na primeira vez)
docker swarm init

# Deploy do stack com 2 réplicas da aplicação
docker stack deploy -c docker/docker-stack.yml sigmon
```

- Aplicação: **http://localhost:5000**
- Mongo Express: **http://localhost:8081**

---

### Localmente sem Docker

```bash
# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
export MONGO_URI="mongodb://localhost:27017/?replicaSet=rs0"
export DATABASE_NAME="sigmon"

# Execute
python app.py
```

> ⚠️ **Atenção:** O MongoDB deve estar rodando em modo Replica Set (`rs0`) para que a aplicação funcione corretamente.

---

## 📦 Dependências

```
Flask==3.1.1
pymongo==4.13.2
python-dotenv==1.1.1
dnspython==2.7.0
```

---

## 🎓 Fins Acadêmicos

Este projeto foi desenvolvido exclusivamente para fins acadêmicos, como trabalho avaliativo da disciplina de **Sistemas Operacionais**. O objetivo é demonstrar na prática conceitos de processos, concorrência, comunicação entre serviços e sistemas distribuídos, aplicados através de uma arquitetura real com containers Docker e banco de dados com Replica Set.

---

## 👥 Responsáveis

<div align="center">

| Nome | Papel |
|---|---|
| 👩‍💻 **Allana Martins** | Desenvolvedora |
| 👩‍💻 **Janiele Barbosa** | Desenvolvedora |
| 👨‍💻 **José Henrique** | Desenvolvedor |
| 👨‍💻 **Lucas** | Desenvolvedor |
| 👨‍💻 **Gabriel Santos** | Desenvolvedor |

</div>

---

<div align="center">

SIGMON · Trabalho de Sistemas Operacionais · Python + Flask + MongoDB · 2026

*Desenvolvido para fins acadêmicos.*

</div>
