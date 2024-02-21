class Restaurante:  
    restaurantes = []
    # CLASS: Criando classe em Python com atributos (nome, categoria, ativo) juntos.
    # SELF: Restaurante vai ter suas próprias informações.
    # INIT: É usado para inicializar os atributos do objeto.
    def __init__(self, nome, categoria):
        self.nome = nome  # Atributos (características)
        self.categoria = categoria  # Atributos
        self.ativo = False  # Atributos
        Restaurante.restaurantes.append(self)

    # __STR__: Pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
    # mostraremos determinada informação.
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
# Criando um novo restaurante que contenha os atributos iguais ao de Restaurante().
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
# Objeto (restaurante_pizza) criado com a classe (Restaurante).

Restaurante.listar_restaurantes()

# print(vars(restaurante_praca))  # VARS: Ver um dicionário (atributo) desse objeto.


