from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Laranja', 10.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_rosca = Prato('Rosca Hungara', 5.00, 'Recheio de Coco')
prato_rosca.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_rosca)




#restaurante_praca.receber_avalicao('Gui', 10)
#restaurante_praca.receber_avalicao('Lais', 8)
#restaurante_praca.receber_avalicao('Emy', 2)

def main():
    restaurante_praca.exibir_cardapio



#def main():
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':                 # Programa principal que não foi imnportado por outro script para ser executado.
    main()                                 # Main = principal.