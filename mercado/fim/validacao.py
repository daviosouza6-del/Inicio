import datetime
import produto

def verificar_validade():
    codigo = input("informe o código do produto: ")
    if codigo in produto.produtos:
        data_hoje = input("informe a data de hoje (DD/MM/AAAA): ")
        try:
            data_val = datetime.datetime.strptime(produto.produtos[codigo]["validade"], "%d/%m/%Y")
            data_atual = datetime.datetime.strptime(data_hoje, "%d/%m/%Y")
        except:
            print("data inválida")
            return

        if data_val >= data_atual:
            print(f"O produto está dentro da validade ({produto.produtos[codigo]['validade']})")
        else:
            print(f"O produto está vencido ({produto.produtos[codigo]['validade']})")
    else:
        print("produto não encontrado")
