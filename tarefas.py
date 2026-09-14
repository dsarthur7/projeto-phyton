arquivo = "tarefas.txt"


def carregar_tarefas():
    """Lê o arquivo tarefas.txt e transforma cada linha numa tarefa."""
    tarefas = []
    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            titulo, status = linha.split("|")
            concluida = status == "1"
            tarefas.append({"titulo": titulo, "concluida": concluida})
        arquivo.close()
    except FileNotFoundError:
      
        pass
    return tarefas


def salvar_tarefas(tarefas):
    """Escreve a lista de tarefas de volta no arquivo tarefas.txt."""
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    for tarefa in tarefas:
        status = "1" if tarefa["concluida"] else "0"
        arquivo.write(tarefa["titulo"] + "|" + status + "\n")
    arquivo.close()


def mostrar_menu():
    print("\n===== Minhas Tarefas =====")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir/Desmarcar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada ainda.")
        return

    print("\nSuas tarefas:")
    for i in range(len(tarefas)):
        tarefa = tarefas[i]
        marcador = "[X]" if tarefa["concluida"] else "[ ]"
        print(str(i + 1) + " " + marcador + " " + tarefa["titulo"])


def adicionar_tarefa(tarefas):
    titulo = input("\nDigite o nome da nova tarefa: ").strip()
    if titulo == "":
        print("A tarefa não pode ficar vazia.")
        return
    tarefas.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada!")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if len(tarefas) == 0:
        return
    escolha = input("\nDigite o número da tarefa pra marcar/desmarcar: ")
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
            print("Tarefa atualizada!")
        else:
            print("Número inválido.")
    else:
        print("Digite um número válido.")


def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if len(tarefas) == 0:
        return
    escolha = input("\nDigite o número da tarefa pra excluir: ")
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print("Tarefa removida: " + removida["titulo"])
        else:
            print("Número inválido.")
    else:
        print("Digite um número válido.")


def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("\nTarefas salvas. Até mais!")
            break
        else:
            print("Opção inválida, tente de novo.")


if __name__ == "__main__":
    main()
