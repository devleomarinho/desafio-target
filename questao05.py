# 5) Escreva um programa que inverta os caracteres de um string.

string = input("Digite a palavra que deseja inverter: ")

string_invertida = ""
for i in range(len(string) -1, -1, -1):
    string_invertida += string[i]

print(f"String original: {string}")
print(f"String invertida: {string_invertida}")