from classes import *

Carrinho_Usuario = Carrinho_Compra()
n1 = Produtos("Notebook", 4500)
n2 = Produtos("Iphone", 8000)
n3 = Produtos("Tablet", 2500)
Carrinho_Usuario.inserir_produto_loja(n1)
Carrinho_Usuario.inserir_produto_loja(n2)
Carrinho_Usuario.inserir_produto_loja(n3)

def main():
    contProdut = 0
    contID = 0
    s = 0
    while s == 0:
        limpar()
        print("BEM VINDO A NOSSA LOJA ")
        print("Bem vindo a Loja do Cacique")
        print("[1] - Cadastro")
        print("[2] - Ver Produtos")
        print("[3] - Adicionar ao Carrinho")
        print("[4] - Remover do Carrinho")
        print("[5] - Ver Carrinho")
        print("[6] - Sair")
        print("Digite o numero equivalente a opção que deseja")
        try:
            menu = int(input(">>"))
            match menu:
                case 1:
                    limpar()
                    print("---CADASTRO DE CLIENTE---")
                    print("INFORME OS SEUS DADOS")
                    contID += 1
                    id = contID
                    nome = input("Nome - ")
                    cpf = int(input("CPF - "))
                    tel = int(input("Telefone - "))                    

                    Carrinho_Usuario.cadastrarCliente(id, nome, cpf, tel)

                    print("CLIENTE CADASTRADO")
                    print("--------")
                    pause()
                
                case 2:
                    limpar()
                    Carrinho_Usuario.listar_produtos_loja()
                    pause()
                    
                case 3:
                    limpar()
                    print("ADICIONAR AO CARRINHO")
                    Carrinho_Usuario.listar_produtos_loja()
                    print("Digite o indice do produto que deseja")
                    indice = int(input(">>"))
                    Carrinho_Usuario.add_produto_carrinho(indice)
                    print("Produto Adicionado ao Carrinho!!")
                    pause()
                
                case 4:
                    limpar()
                    print("EXCLUIR PRODUTO DO CARRINHO")
                    Carrinho_Usuario.listar_produtos_carrinho()
                    print("Digite o indice do produto que deseja remover")
                    vetor_carrinho = int(input(">>"))
                    Carrinho_Usuario.delProduto_carrinho(vetor_carrinho)
                    pause()
                    
                case 5:
                    limpar()
                    Carrinho_Usuario.listar_produtos_carrinho()
                    pause()
                
                case 6:
                    limpar()
                    print("Saindo...")
                    pause()
                    break
                
                case _:
                    limpar()
                    print("Opção Inválida")
                    pause()
                
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            pause()
                
        
