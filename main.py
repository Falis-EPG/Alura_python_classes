from restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japi Sushi', 'Japones')

restaurante_mexicano.alternar_estado()
restaurante_mexicano.receber_avaliacao('Erick', 10)
restaurante_praca.receber_avaliacao('Nicolas', 9)
restaurante_mexicano.receber_avaliacao('Ygor', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
