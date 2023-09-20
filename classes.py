import os

class Carrinho_Compra:
    def __init__(self):
        self.cliente = {}

    lista_loja = []
    lista_carrinho = []
    
    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel        
        self.cliente[self.id] = [self.nome, self.cpf, self.tel]
        
    def dadosClientes(self):
        for chave,valor in self.cliente.items():
            print(f"ID:{chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")
            
    def criar_produto(self, nome_produto, valor):
        self.nome = nome_produto
        self.valor = valor
        
        novo_produto = Produtos(self.nome, self.valor)
        self.lista_loja.append(novo_produto)
        print(f"Produto '{nome_produto}' foi adicionado à lista da loja.")
        
    
    #FUNCIONALIDADE DA LISTA DE PRODUTOS DA LOJA
    def inserir_produto_loja(self, produto):
        self.produto = produto
        self.lista_loja.append(self.produto)
        

    def listar_produtos_loja(self):
        self.cont = 0
        for produto in self.lista_loja:
            self.cont += 1
            print(f"{self.cont} -> Nome: {produto.getNome()}, Valor: {produto.getValor()}")

    def getLista_loja(self, vetor_loja):
        return self.lista_loja[vetor_loja]
    
    def delProduto_loja(self, vetor_loja):
        self.vetor_lista = vetor_loja - 1
        self.lista_loja.pop(self.vetor_lista)
        
    #FUNCIONALIDADE DA LISTA DO CARRINHO DO USUARIO
    def add_produto_carrinho(self, indice):
        if indice >= 1 and indice <= len(self.lista_loja):
            indice_lista = indice - 1
            produto = self.lista_loja[indice_lista]  
            self.lista_carrinho.append(produto)  
        else:
            print("Índice inválido.")
            
    def listar_produtos_carrinho(self):
        self.cont = 0
        for produto in self.lista_carrinho:
            self.cont += 1
            print(f"{self.cont} -> Nome: {produto.getNome()}, Valor: {produto.getValor()}")
            
    def delProduto_carrinho(self, vetor_carrinho):
        self.vetor_carrinho = vetor_carrinho - 1
        self.lista_carrinho.pop(self.vetor_carrinho)
        

class Produtos:
    def __init__(self,nome, valor):
       self.nome = nome
       self.valor = valor

    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor
 
def pause():
    os.system("pause") 
   
def limpar():
    os.system("cls")
