

# ### **1- Classe Pessoa**

# Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione um método `apresentar()` que exiba `"Olá, meu nome é [nome] e tenho [idade] anos."` Crie duas pessoas diferentes e chame o método.


# class Pessoa:
#     def __init__(self , nome , idade):
    
#      self.nome = nome
#      self.idade = idade
#     def apresentar (self):
#        print(f"olá meu nome é {self.nome} e tenho {self.idade}")
# pessoa = Pessoa("leonardo", 20)
# pessoa.apresentar()






# ### **2.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

# class Retangulo :
#    def __init__(self , largura , altura ):
      
#       self.largura = largura
#       self.altura = altura
#    def apresentar (self): 
#       print(f"LARGURA  { self.largura } \nALTURA { self.altura }")
#       print(f"Soma da largura vezes a altura é de : {self.altura ** self.largura // 2}")
#    def calcular_area (self): 
#       print(f"LARGURA  { self.largura } \nALTURA { self.altura }")
#       print(f"Soma da largura vezes a altura  : {self.altura * self.largura }")
# retangulo = Retangulo( 5,2 )
# retangulo.apresentar()
# retangulo.calcular_area()



### **3.   Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.



class Conta_bancaria :
    def __init__(self ,  titular , saldo ):
        self.titular = titular
        self.saldo = saldo
    def apresentar (self):
        print(f"Senhor clinte {self.titular}")
        print(f"Saldo em conta é de R$ :  {self.saldo}")
conta_bancaria = Conta_bancaria("Leonardo medina" , 5823.25)
conta_bancaria.apresentar()
