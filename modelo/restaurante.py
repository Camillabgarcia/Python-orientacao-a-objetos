class  restaurante:              #CLASS: criando classe no python com atributos (nome, categoria, ativo) juntos.
    nome = ''
    categoria = ''
    ativo = False
restaurante_praca = restaurante()                 #Criando um novo restaurante que contenha as informações iguais a de restaurante().
restaurante_pizza = restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)