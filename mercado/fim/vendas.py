import produto

def calcular_venda():
    codigo = input("informe o código do produto: ")
    if codigo in produto.produtos:
        p = produto.produtos[codigo]
        print(f"produto: {p['nome']}")
        print(f"valor unitário: {p['valor']:.2f}")

        try:
            qtd = int(input("quantidade que deseja: "))
        except:
            print("erro em valores numéricos")
            return

        if qtd <= p["quantidade"]:
            total = p["valor"] * qtd
            print(f"total da compra: {total:.2f}")
        else:
            print("estoque insuficiente")
    else:
        print("produto não encontrado")
