# B02 — Domain Modeling

## Objetivo

Modelar em Python os principais conceitos do domínio do SharedSpace antes da implementação da persistência em banco de dados.

## Estratégia

A B02 utiliza modelos de domínio puros com `dataclasses`.

A persistência com SQLAlchemy será introduzida na B03 — Database.

Essa separação mantém a modelagem do domínio independente da tecnologia de banco neste estágio do projeto.

## Modelos

### Space

Representa um espaço compartilhado monitorado pelo SharedSpace.

Atributos:

- `id: UUID`
- `name: str`
- `description: str | None`
- `capacity: int`

A ocupação não é armazenada diretamente no modelo.

Ela será derivada das sessões ativas.

### Session

Representa uma permanência anônima em um espaço.

Atributos:

- `id: UUID`
- `space_id: UUID`
- `status: SessionStatus`
- `started_at: datetime`
- `confirmation_requested_at: datetime | None`
- `ended_at: datetime | None`

Uma sessão não possui dados pessoais do usuário.

### Event

Representa um acontecimento relevante no ciclo de vida de uma sessão.

Atributos:

- `id: UUID`
- `session_id: UUID`
- `type: EventType`
- `occurred_at: datetime`

## Relacionamentos

```text
SPACE
  │
  └── 1:N SESSION
              │
              └── 1:N EVENT