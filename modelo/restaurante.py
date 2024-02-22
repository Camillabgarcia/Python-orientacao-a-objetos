class Restaurante:  
    restaurantes = []
    # CLASS: Criando classe em Python com atributos (nome, categoria, ativo) juntos.
    # SELF: Restaurante vai ter suas próprias informações.
    # INIT: É usado para inicializar os atributos do objeto.
    def __init__(self, nome, categoria):       #Não define 'Ativo' como parâmetro.
        self._nome = nome.title()                # Atributos (características) #Title: mantem a primeira letra maiuscula. #_nome: protegio e não pode alterar o nome.
        self._categoria = categoria.upper()      # Atributos # UPPER: todas as letras maiusculas.
        self._ativo = False              #Definiu apenas como falso(Padrão)._ativo: para as pessoas não acessarem (Protegido).
        Restaurante.restaurantes.append(self)

    # __STR__: Pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
    # mostraremos determinada informação.
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')  #LJUST(?):para dar espaço.

    @property                                    #Modificar como determinado atributo (ex: ativo) vai ser lido.
    def ativo(self):
        return '☑' if self._ativo else '☐'

restaurante_praca = Restaurante('praça', 'Gourmet')   # Criando um novo restaurante que contenha os atributos iguais ao de Restaurante().

restaurante_pizza = Restaurante('pizza express', 'Italiana')   # Objeto (restaurante_pizza) criado com a classe (Restaurante).


Restaurante.listar_restaurantes()

# print(vars(restaurante_praca))  # VARS: Ver um dicionário (atributo) desse objeto.


