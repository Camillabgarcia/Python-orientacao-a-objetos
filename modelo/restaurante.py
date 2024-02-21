class Restaurante:  
    # CLASS: Criando classe em Python com atributos (nome, categoria, ativo) juntos.
    # SELF: Restaurante vai ter suas próprias informações.
    # INIT: É usado para inicializar os atributos do objeto.
    def __init__(self, nome, categoria):
        self.nome = nome  # Atributos (características)
        self.categoria = categoria  # Atributos
        self.ativo = False  # Atributos

    # __STR__: Pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
    # mostraremos determinada informação.
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Gourmet')
# Criando um novo restaurante que contenha os atributos iguais ao de Restaurante().
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
# Objeto (restaurante_pizza) criado com a classe (Restaurante).

restaurantes = [restaurante_praca, restaurante_pizza]

# print(vars(restaurante_praca))  # VARS: Ver um dicionário (atributo) desse objeto.

print(restaurante_praca)
print(restaurante_pizza)


