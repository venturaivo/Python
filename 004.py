import random
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Gera 50 chaves
chaves = []
for _ in range(50):
    numeros = random.sample(range(1, 51), 5)
    estrelas = random.sample(range(1, 13), 2)
    chaves.append(numeros + estrelas)

# Guarda as chaves num ficheiro csv
with open('chaves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['numero1', 'numero2', 'numero3', 'numero4', 'numero5', 'estrela1', 'estrela2'])
    writer.writerows(chaves)

# Conta o número de vezes que os números e estrelas foram gerados
contador = Counter([num for chave in chaves for num in chave])

# Cria um gráfico com o número de vezes que os números e estrelas foram gerados
plt.bar(contador.keys(), contador.values())
plt.xlabel('Número ou Estrela')
plt.ylabel('Frequência')
plt.title('Frequência dos Números e Estrelas Gerados')
plt.show()