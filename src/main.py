"""
TaskTracker - Fase 2 (Bootcamp II)
Aplicação CLI para cadastro e visualização de tarefas.

A lógica segue a "receita lógica" planejada na Fase 1:
  - Cadastro: título (obrigatório) -> descrição -> prioridade (validada) -> data limite
  - Visualização: avisa se a lista está vazia; senão mostra tarefa por tarefa
"""

from datetime import datetime

# Aceita "Alta", "Média" (ou "Media") e "Baixa", sem diferenciar maiúsculas/minúsculas.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


# ---------------------------------------------------------------
# Funções de validação (regras de negócio)
# ---------------------------------------------------------------
def titulo_valido(titulo):
    """Retorna True se o título não for vazio nem só espaços em branco."""
    return len(titulo.strip()) > 0


def normalizar_prioridade(texto):
    """Retorna 'Alta', 'Média' ou 'Baixa' se válida; caso contrário, None."""
    return PRIORIDADES_VALIDAS.get(texto.strip().lower())


def data_valida(texto):
    """Retorna True se a data estiver no formato DD/MM/AAAA e existir de verdade."""
    try:
        datetime.strptime(texto.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------
# Funções de entrada de dados (repetem o prompt até ser válido)
# ---------------------------------------------------------------
def pedir_titulo():
    while True:
        titulo = input("Título da tarefa: ")
        if titulo_valido(titulo):
            return titulo.strip()
        print("Erro: o título não pode ficar vazio. Tente novamente.")


def pedir_prioridade():
    while True:
        texto = input("Prioridade (Alta, Média ou Baixa): ")
        prioridade = normalizar_prioridade(texto)
        if prioridade is not None:
            return prioridade
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def pedir_data_limite():
    while True:
        texto = input("Data limite (DD/MM/AAAA) [Enter para pular]: ").strip()
        if texto == "":
            return "Não informada"
        if data_valida(texto):
            return texto
        print("Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 20/10/2026).")


# ---------------------------------------------------------------
# Funcionalidades principais
# ---------------------------------------------------------------
def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data_limite = pedir_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # sempre começa como Pendente
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título     : {tarefa['titulo']}")
        print(f"  Descrição  : {tarefa['descricao']}")
        print(f"  Prioridade : {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status     : {tarefa['status']}")
    print(f"\nTotal de tarefas: {len(tarefas)}")


def exibir_menu():
    print("\n===== TaskTracker =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []  # lista que guarda todas as tarefas (dicionários)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
