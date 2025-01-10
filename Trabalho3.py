# Conforme o pedido do enunciado:
# O programa solicita ao usuário que escolha um serviço de cópia (DIG, ICO, IBO, FOT)
# Calcula o custo com base no serviço escolhido, no número de páginas e nos serviços adicionais selecionados
# Exibe o total a pagar e mensagens de erro caso haja problemas com a entrada do usuário

import random

print("Bem-vindo ao Sistema de Cobrança da Copiadora do Diogo Pedroso!")

# Função para escolher o serviço de cópia
def escolha_servico():
    while True:
        servico = input("Digite o serviço desejado (DIG/ICO/IBO/FOT): ").upper()
        if servico in ["DIG", "ICO", "IBO", "FOT"]:
            return servico
        else:
            print("Opção inválida. Por favor, escolha entre DIG, ICO, IBO ou FOT.")

# Função para calcular o número de páginas com desconto
def num_paginas_com_desconto():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas desejado: "))
            if num_paginas < 10:
                return num_paginas
            elif 10 <= num_paginas < 100:
                return int(num_paginas * 0.9)
            elif 100 <= num_paginas < 1000:
                return int(num_paginas * 0.85)
            elif 1000 <= num_paginas < 10000:
                return int(num_paginas * 0.8)
            else:
                print("Número de páginas excede o limite máximo permitido (10.000).")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

# Função para escolher serviço adicional
def servico_extra():
    while True:
        try:
            adicional = int(input("Escolha um serviço adicional (1 - Encadernação Simples, 2 - Encadernação Capa Dura, 0 - Nenhum): "))
            if adicional in [1, 2, 0]:
                return adicional
            else:
                print("Opção inválida. Por favor, escolha entre 1, 2 ou 0.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

try:
    # Chama as funções para obter informações do usuário
    servico = escolha_servico()
    num_paginas = num_paginas_com_desconto()
    adicional = servico_extra()

    # Define os valores dos serviços
    valor_servico = {"DIG": 1.10, "ICO": 1.00, "IBO": 0.40, "FOT": 0.20}
    total = valor_servico[servico] * num_paginas

    # Adiciona o custo do serviço adicional, se houver
    if adicional == 1:
        total += 10.00
    elif adicional == 2:
        total += 25.00

    # Imprime o total a pagar
    print(f"Total a pagar: R${total:.2f}")

except Exception as e:
    # Imprime mensagem de erro caso ocorra uma exceção
    print(f"Erro: {e}")
    print("Erro: Opção de serviço inválida. Por favor, reinicie o programa e escolha um serviço válido.")
    print("Erro: Número de páginas excede o limite máximo permitido (10.000). Por favor, reinicie o programa com um número menor de páginas.")

# Mensagem de agradecimento
print("Obrigado por utilizar o Sistema de Cobrança da Copiadora. Desenvolvido por Diogo Pedroso.")
