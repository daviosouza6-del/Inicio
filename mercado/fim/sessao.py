sessoes = []

def cadastrar_sessao():
    nome = input("nome da sessão: ")
    if nome in sessoes:
        print("sessão em uso")
    else:
        sessoes.append(nome)
        print("sessão cadastrada")

def listar_sessoes():
    if not sessoes:
        print("nenhuma sessão cadastrada")
    else:
        print("sessões cadastradas:")
        for s in sessoes:
            print("-", s)
        print()

def excluir_sessao():
    if not sessoes:
        print("nenhuma sessão cadastrada")
        return

    nome = input("informe o nome da sessão: ")
    if nome in sessoes:
        sessoes.remove(nome)
        print("sessão excluída")
    else:
        print("sessão não encontrada")
