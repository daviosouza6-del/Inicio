import sessao

produtos = {}

def cadastrar_produto():
    codigo = input("código do produto: ")
    if codigo in produtos:
        print("código em uso")
        return

    nome = input("nome do produto: ")
    sessao_nome = input("nome da sessão: ")

    if sessao_nome not in sessao.sessoes:
        print("sessão não encontrada")
        return

    try:
        valor = float(input("valor unitário: "))
        peso = float(input("peso: "))
        quantidade = int(input("quantidade: "))
        validade = input("data de validade (DD/MM/AAAA): ")
    except:
        print("erro em valores numéricos")
        return

    produtos[codigo] = {"nome": nome,"sessao": sessao_nome,"valor": valor,"peso": peso,"quantidade": quantidade,"validade": validade,}
    print("produto cadastrado")

def listar_produto():
    if not produtos:
        print("nenhum produto cadastrado")
    else:
        for codigo, p in produtos.items():
            print(f"código: {codigo}")
            print(f"nome: {p['nome']}")
            print(f"sessão: {p['sessao']}")
            print(f"valor: {p['valor']:.2f}")
            print(f"peso: {p['peso']}")
            print(f"quantidade: {p['quantidade']}")
            print(f"validade: {p['validade']}")
            print()

def pesquisar_produto():
    codigo = input("informe o código do produto: ")
    if codigo in produtos:
        p = produtos[codigo]
        print(f"produto: {p['nome']}")
        print(f"sessão: {p['sessao']}")
        print(f"valor: {p['valor']:.2f}")
        print(f"peso: {p['peso']}")
        print(f"quantidade: {p['quantidade']}")
        print(f"validade: {p['validade']}")
    else:
        print("produto não encontrado")

def alterar_produto():
    codigo = input("código do produto que deseja alterar: ")
    if codigo in produtos:
        p = produtos[codigo]
        print(f"produto atual: {p['nome']} ({p['valor']:.2f})")

        novo_nome = input("novo nome: ") or p["nome"]
        try:
            novo_valor = float(input("novo valor: ") or p["valor"])
            nova_quantidade = float(input("nova quantidade: ") or p["quantidade"])
        except:
            print("erro em valores numéricos")
            return

        p["nome"] = novo_nome
        p["valor"] = novo_valor
        p["quantidade"] = nova_quantidade
        print("produto alterado")
    else:
        print("produto não encontrado")

def excluir_produto():
    codigo = input("código do produto a excluir: ")
    if codigo in produtos:
        del produtos[codigo]
        print("produto excluído")
    else:
        print("produto não encontrado")
