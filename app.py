from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avalicao('Gui', 10)
restaurante_praca.receber_avalicao('Lais', 8)
restaurante_praca.receber_avalicao('Emy', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':                 # Programa principal que não foi imnportado por outro script para ser executado.
    main()                                 # Main = principal.