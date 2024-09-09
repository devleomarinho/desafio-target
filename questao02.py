# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

num = int(input("Digite o número para a ver a sequência de Fibonacci até ele: "))

fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"Sequência de Fibonacci até {num}:")
print(fibonacci)

if num in fibonacci:
    print(f"O número {num} PERTENCE à sequência de Fibonacci")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci")