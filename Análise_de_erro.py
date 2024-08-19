import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configura para mostrar gráficos no console
plt.switch_backend('Agg')

#Definição da Função
def serie_tarefa1(x,n):
    return ((-1)**n) * (((2*x)+3)**n)/(n*(math.log(n)))

soma = 0
erro=100
old=0
new=0
iteracao=0

#Definição de x, onde ele vai de -2 a -1, com 100 valores igual mente espaçados
X=np.linspace(-2,-1,100)

#Vetores
ERROR = []
SOMA = []
Iteracao = []

#Definição do (Eppara)
N = 3 #Critério de parada
Eppara = (0.5*10**(2-N))# "N" número de algarismos significativos
print(f"Eppara:",Eppara)

# Termo "n"
n = 2  #Começa em dois pois ha uma restrição no ln
#Loop
for i in range (0,len(X)):
    print(f"Índice: {i}, Valor: {X[i]}")


#Número de Iterações
    while erro > Eppara:

        x=X[i]

        soma += serie_tarefa1(x,n)

        old = new
        new = soma
        erro = abs((new - old) / new) * 100

        ERROR.append(erro)
        SOMA.append(soma)
        Iteracao.append(iteracao)

        iteracao+=1
        n += 1
    #Resultado
    print(f"Valor de x:", X[i])
    print(f"Iterações:",iteracao)
    print(f"soma:",soma)
    print(f"erro:",erro)

    # Criando o DataFrame
    df = pd.DataFrame({
        'Iteração': range(1, iteracao+1),
         'Erro (%)': ERROR,
         'Soma': SOMA
        })

    print(df)
    #plt.plot(ERROR, label='Erro')
    #plt.plot(SOMA, label='Soma')
    plt.plot(Iteracao, ERROR, label='Iteração x Erro (%)', color='blue')
    plt.title('Gráfico de Erro x Iteração')
    plt.xlabel('Iteração')
    plt.ylabel('Erro (%)')
    plt.legend()
    #plt.show()
    df=0

    soma=0
    ERROR = []
    SOMA = []
    Iteracao = []

    soma = 0

    erro=100
    old=0
    new=0
    iteracao=0
