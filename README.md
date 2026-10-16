# bootcamp-2

# TaskTracker

Aplicação de linha de comando (CLI) em Python para gerenciar tarefas do dia a dia.
Projeto cumulativo do **Bootcamp II** — Fase 2 (Entrega Intermediária).

## Descrição funcional

O TaskTracker permite:

- **Cadastrar tarefas** com título, descrição, prioridade e data limite;
- **Visualizar** todas as tarefas cadastradas, com status e demais informações.

### Regras de negócio

- O **título é obrigatório**: entradas vazias ou só com espaços são rejeitadas.
- A **prioridade** aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.
- A **data limite** é opcional; se informada, deve estar no formato `DD/MM/AAAA`.
- Toda tarefa nova começa com status **Pendente**.
- Se não houver tarefas, o sistema avisa que não existem registros.

## Tecnologias

- Python 3
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```
   (No Linux/macOS, se necessário, use `python3 src/main.py`.)

## Exemplo de uso

```
===== TaskTracker =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1
Título da tarefa: Estudar para a prova de Lógica
...
Tarefa cadastrada com sucesso!
```



Sara Menezes Macedo — Ciência de dados — Bootcamp II
