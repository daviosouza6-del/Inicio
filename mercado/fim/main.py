import sessao as ses
import produto as pro
import vendas as ven
import validacao as vali

def menu():
    while True:
        print("===== SISTEMA DE SUPERMERCADO ======")
        print("1 - cadastrar sessão")
        print("2 - listar sessão")
        print("3 - excluir sessão")
        print("4 - cadastrar produto")
        print("5 - listar produto")
        print("6 - pesquisar produto")
        print("7 - alterar produto")
        print("8 - excluir produto")
        print("9 - calcular vendas")
        print("10 - verificar validade")
        print("0 - sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ses.cadastrar_sessao()
        elif opcao == "2":
            ses.listar_sessoes()
        elif opcao == "3":
            ses.excluir_sessao()
        elif opcao == "4":
            pro.cadastrar_produto()
        elif opcao == "5":
            pro.listar_produto()
        elif opcao == "6":
            pro.pesquisar_produto()
        elif opcao == "7":
            pro.alterar_produto()
        elif opcao == "8":
            pro.excluir_produto()
        elif opcao == "9":
            ven.calcular_venda()
        elif opcao == "10":
            vali.verificar_validade()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida")

def menuPrincipal():
    menu()

menuPrincipal()
