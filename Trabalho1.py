 
# conforme o pedido do enunciado:
#   - O programa imprime a mensagem de boas vindas com meu nome
#   - Recebe o valor unitário e a quantidade do produto.
#   - Calcula o valor total sem desconto com base no valor unitário e quantidade.
#   - Aplica o desconto conforme as condições especificadas.
#   - Calcula o valor do desconto e o valor total com desconto.
#   - Imprime um resumo do pedido com os resultados.

# 1. Mensagem de boas vindas
nome_usuario = input("Digite seu nome: ")
print(f"Seja Bem-vindo(a) {nome_usuario}, a loja do Diogo Pedroso aproveite os descontos e boas compras!")

# 2. Input do valor unitário e quantidade do produto
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# 3. Calculando o valor total sem o desconto
valor_total_sem_desconto = valor_unitario * quantidade

# 4. Implementando o desconto conforme o enunciado pede
if valor_total_sem_desconto < 1000:
    desconto_percentual = 0
elif valor_total_sem_desconto < 3000:
    desconto_percentual = 3
elif valor_total_sem_desconto < 5000:
    desconto_percentual = 5
else:
    desconto_percentual = 8

# Calculando o valor do desconto
desconto = (desconto_percentual / 100) * valor_total_sem_desconto

# Calculando o valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto - desconto

# 5. Imprime os resultados
print("\nResumo do Pedido:")
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Desconto de {desconto_percentual}%: R${desconto:.2f}")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")

# 6. Mensagem de desconto para valor total sem desconto acima de 1000
if valor_total_sem_desconto > 1000:
    print("Parabéns! Você recebeu um desconto especial no valor total.")
    print('Obrigado pelas compras e volte sempre. Diogo Pedroso Agradece a Preferência! ')






