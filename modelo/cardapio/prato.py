from modelo.cardapio.item_cardapio import ItemCardapio                   
                                     
class Prato(ItemCardapio):                           #A classe Prato vai herdar informações e atributos da classe item_cardapio.
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)               # Super: permite acessar informações de outra classe.
        self.descricao = descricao

    def __str__(self):
        return self._nome