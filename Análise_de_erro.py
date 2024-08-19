import math
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Definição da Função
def serie_tarefa1(x, n):
    return ((-1)**n) * (((2*x) + 3)**n) / (n * math.log(n))

# Definição de x
X = [-2, -1]

# Definição do critério de parada (Eppara)
N = 8  # Critério de parada
Eppara = (0.5 * 10**(2 - N))  # "N" número de algarismos significativos
print(f"Eppara: {Eppara}")

# Loop para cada valor de X
for i in range(len(X)):
    print(f"Índice: {i}, Valor: {X[i]}")

    # Resetando variáveis para cada novo valor de x
    soma = 0
    erro = 100
    old = 0
    new = 0
    iteracao = 0

    # Vetores para armazenar resultados
    ERROR = []
    SOMA = []
    Iteracao = []

    # Termo "n"
    n = 2  # Começa em dois devido à restrição no logaritmo

    # Número de Iterações
    while erro > Eppara:
        x = X[i]
        soma += serie_tarefa1(x, n)

        old = new
        new = soma

        erro = abs((new - old) / new) * 100

        ERROR.append(erro)
        SOMA.append(soma)
        Iteracao.append(iteracao)

        iteracao += 1
        n += 1

    # Resultado
    print(f"Valor de x: {X[i]}")
    print(f"Iterações: {iteracao}")
    print(f"Soma: {soma}")
    print(f"Erro: {erro}")

    # Criando o DataFrame
    df = pd.DataFrame({
        'Iteração': range(1, iteracao + 1),
        'Erro (%)': ERROR,
        'Soma': SOMA
    })

    print(df)

    # Plotando o gráfico para o valor atual de x
    plt.plot(Iteracao, ERROR, label=f'x = {X[i]}')
    plt.title('Gráfico de Erro x Iteração')
    plt.xlabel('Iteração')
    plt.ylabel('Erro (%)')
    plt.legend()

# Mostra o gráfico após todas as iterações
plt.show()
#teste