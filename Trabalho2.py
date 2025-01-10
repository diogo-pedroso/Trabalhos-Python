#conforme o pedido do enunciado:
# O programa exibe uma mensagem de boas vindas ao aplicativo
# Entra no loop com while true
# Apresenta o input solicitando que o usuário escolha o sabor desejado
# Faz a verificação do sabor com o if e se for diferente das opções disponíveis apresenta um print com a mensagem de erro
# Faz essa verificação até que o usuário coloque um valor válido
# Assim que o valor de entrada passa a ser válido, o programa solicita a partir de um input que o usuário escolha um tamanho
# Faz a verificação e se for diferente dos tamanhos disponíveis apresenta um print com mensagem de erro
# Utilizando o if e elif define o valor do pedido conforme o sabor e tamanho escolhidos
# Adiciona o valor do pedido ao total do pedido
# Pergunta se o usuário deseja realizar outro pedido utilizando o input
# Se a resposta for igual a 'S' (sim), volta ao início do programa 
# mas se a resposta for diferente de 'S' (sim), sai do loop a partir de um break 
# Por fim, imprime o valor total ao usuário
# Utilizei o .upper() no código para fazer a conversão de letras minúsculas para maiúsculas 

# Mensagem de boas-vindas 
print("Bem-vindo a loja Diogo Pedroso Açaí e Cupuaçu! ")

# Inicializa o total do pedido como zero
total_pedido = 0  

# Loop principal que continua até que o usuário decida parar
while True:
    # Solicita ao usuário que escolha o sabor e converte para maiúsculas
    sabor = input("Escolha o sabor (CP para Cupuaçu, AC para Açaí): ").upper()
    
    # Verifica se o sabor escolhido é válido
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue  # Volta ao início do loop se o sabor for inválido

    # Solicita ao usuário que escolha o tamanho e converte para maiúsculas
    tamanho = input("Escolha o tamanho (P, M, G): ").upper()
    
    # Verifica se o tamanho escolhido é válido
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  # Volta ao início do loop se o tamanho for inválido

    # Define o valor do pedido com base no sabor e tamanho escolhidos
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 10
        elif tamanho == 'M':
            valor_pedido = 15
        elif tamanho == 'G':
            valor_pedido = 19
    elif sabor == 'AC':
        if tamanho == 'P':
            valor_pedido = 12
        elif tamanho == 'M':
            valor_pedido = 17
        elif tamanho == 'G':
            valor_pedido = 21

    # Adiciona o valor do pedido ao total do pedido
    total_pedido += valor_pedido

    # Pergunta ao usuário se deseja fazer mais pedidos e encerra o loop se a resposta não for 'S'
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais_pedidos != 'S':
        break  # Sai do loop se a resposta não for 'S'

# Imprime o total do pedido formatado com duas casas decimais
print(f"Total do pedido: R${total_pedido:.2f}")
