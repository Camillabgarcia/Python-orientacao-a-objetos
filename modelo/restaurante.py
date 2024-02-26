from modelo.avaliacao import Avaliacao
from modelo.cardapio.item_cardapio import ItemCardapio

class Restaurante:  
    restaurantes = []
    # CLASS: Criando classe em Python com atributos (nome, categoria, ativo) juntos.
    # SELF: Restaurante vai ter suas próprias informações.
    # INIT: É usado para inicializar os atributos do objeto.
    def __init__(self, nome, categoria):         #Não define 'Ativo' como parâmetro.
        self._nome = nome.title()                # Atributos (características) #Title: mantem a primeira letra maiuscula. #_nome: protegio e não pode alterar o nome.
        self._categoria = categoria.upper()      # Atributos # UPPER: todas as letras maiusculas.
        self._ativo = False                      #Definiu apenas como falso(Padrão)._ativo: para as pessoas não acessarem (Protegido).
        self._avalicao = []                      # Não entra como parametro, pois não é para manipular como os demais.
        self._cardapio = []                    
        Restaurante.restaurantes.append(self)

    # __STR__: Pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto,
    # mostraremos determinada informação.
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')  #LJUST(?):para dar espaço.

    @property                                    #Modificar como determinado atributo (ex: ativo) vai ser lido.
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avalicao(self,cliente, nota):                       # Self = Objeto(restaurante).
        if 0 < nota <= 5 :
            avalicao = Avaliacao(cliente, nota)                         # avalicao: novo objeto criado.
            self._avalicao.append(avalicao)

    @property
    def media_avaliacao(self):                                 #self: avaliação do restaurante que está sendo usado.
        if not self._avalicao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avalicao)
        quantidade_de_notas = len(self._avalicao)
        media = round(soma_das_notas / quantidade_de_notas, 1)     #ROUND: arredonda o valor da equação e deixar 1 casa decimal.
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    @property            # Somente para leitura.
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}.Nome: {item._nome} | Preço: R$: {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}.Nome: {item._nome} | Preço: R$: {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)



# print(vars(restaurante_praca))  # VARS: Ver um dicionário (atributo) desse objeto.


