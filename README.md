# TaskTracker

Aplicação de linha de comando (CLI) em Python para gerenciar tarefas do dia a dia, agora **empacotada com Docker** e executável via **Docker Compose**.
Projeto cumulativo do **Bootcamp II** — Fase 3 (Entrega Final).

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

- Python 3.11
- Docker e Docker Compose
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Guia Docker

**Pré-requisito:** [Docker](https://docs.docker.com/get-docker/) instalado (com o plugin Docker Compose).

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/sarammacedo/bootcamp-2.git
cd bootcamp-2
```

### Como construir a imagem:

```bash
docker build -t tasktracker-app .
```

### Como rodar o container em modo isolado:

```bash
docker run -it --rm tasktracker-app
```

### Como rodar via orquestração (Recomendado):

```bash
docker compose run --rm tasktracker
```

> O `docker-compose.yml` usa `stdin_open: true` e `tty: true` para manter o canal de entrada aberto e alocar um terminal virtual, permitindo o uso do `input()` da CLI dentro do container.

## Execução sem Docker (opcional)

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Execute a aplicação:
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

## Autora

Sara Menezes Macedo — Ciência de Dados — Bootcamp II
