from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':                 # Programa principal que não foi imnportado por outro script para ser executado.
    main()                                 # Main = principal.