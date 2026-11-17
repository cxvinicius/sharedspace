# B03 — Database Persistence

##  Objetivo
Implementar a camada de persistência do **SharedSpace**, conectando os modelos de domínio a um banco **PostgreSQL** através do **SQLAlchemy** e **Alembic**.

---

##  Estratégia
* **Separação de Conceitos:** A B03 mantém a separação entre domínio e persistência estabelecida na B02.
* **Modelagem:** Os modelos de domínio continuam utilizando `dataclasses`, enquanto os modelos de persistência utilizam `SQLAlchemy`.
* **Ambiente:** O PostgreSQL é executado em um container Docker, garantindo um ambiente de desenvolvimento reproduzível.
* **Evolução do Banco:** O Alembic é utilizado para controlar as migrations do banco de dados.

---

##  Infraestrutura

O **PostgreSQL** foi configurado através do Docker Compose com os seguintes parâmetros:

* **Banco utilizado:** `sharedspace`
* **Container:** `sharedspace-postgres`
* **Porta:** `5432`

### Dependências Python adicionadas:
* `SQLAlchemy`
* `Alembic`
* `psycopg`
* `psycopg-binary`

---

## Persistência

A camada de persistência foi estritamente separada do domínio dentro da estrutura de diretórios:

```text
app/
├── models/
│   ├── space.py
│   ├── session.py
│   └── event.py
│
└── persistence/
    └── models/
        ├── space.py
        ├── session.py
        └── event.py
```

Os modelos de persistência representam as entidades `SpaceModel`, `SessionModel` e `EventModel`, utilizando uma `Base` própria do SQLAlchemy.

---

## Tabelas e Atributos

### 1. `spaces`
Representa os espaços monitorados pelo SharedSpace.
* `id`: UUID
* `name`: str
* `description`: str | None
* `capacity`: int

### 2. `sessions`
Representa as sessões de permanência nos espaços.
* `id`: UUID
* `space_id`: UUID
* `status`: str
* `started_at`: datetime
* `confirmation_requested_at`: datetime | None
* `ended_at`: datetime | None

### 3. `events`
Representa os eventos relacionados ao ciclo de vida de uma sessão.
* `id`: UUID
* `session_id`: UUID
* `type`: str
* `occurred_at`: datetime

###  Relacionamentos e Chaves Estrangeiras

```text
SPACE
  │
  └── 1:N SESSION
              │
              └── 1:N EVENT
```

* `sessions.space_id` ➔ `spaces.id`
* `events.session_id` ➔ `sessions.id`

---

## Migrations

O Alembic foi configurado para controlar a evolução do schema do banco.

* **Primeira migration:** `bdbbd471cace_create_sharedspace_tables.py`
* **Escopo:** Criação das tabelas `spaces`, `sessions`, `events` e suas respectivas Foreign Keys.

---

##  Validação

1. A conexão entre aplicação e PostgreSQL foi validada através do SQLAlchemy.
2. A migration foi aplicada com sucesso utilizando o comando:
   ```bash
   alembic upgrade head
   ```
3. O PostgreSQL foi validado posteriormente, confirmando a existência física das tabelas e integridade das Foreign Keys.

---

##  Resultado

A B03 estabelece a persistência do SharedSpace sem acoplar o domínio diretamente ao banco de dados, resultando no seguinte fluxo arquitetural:

```text
Domain      ➔  Dataclasses
    ↓
Persistence ➔  SQLAlchemy
    ↓
Migration   ➔  Alembic
    ↓
Database    ➔  PostgreSQL
```