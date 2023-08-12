# Estrutura Condicional junto com while:

# Ex01:
n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))
if n1 > n2:
    print(f"O numero {n1} é maior que {n2}")
else:
    print(f"O numero {n2} é maior que {n1}")

# Ex02:
n1 = float(input("Digite a sua nota da primeira prova: "))
while n1 < 0 and n1 > 10:
    n1 = float(input("Nota invalida! Digite a sua nota da primeira prova: "))
n2 = float(input("Digite a sua nota da segunda prova: "))
while n2 < 0 and n2 > 10:
    n2 = float(input("Nota invalida! Digite a sua nota da segunda prova: "))
media = (n1 + n2) / 2
if media >= 7:
    print(f"Parabens você foi aprovado, a sua media foi de {media}")
else:
    print(f"Você foi reprovado, a sua media foi de {media}")

# Ex03:
n1 = float(input("Digite a sua nota da primeira prova: "))
while n1 < 0 and n1 > 10:
    n1 = float(input("Nota invalida! Digite a sua nota da primeira prova: "))
n2 = float(input("Digite a sua nota da segunda prova: "))
while n2 < 0 and n2 > 10:
    n2 = float(input("Nota invalida! Digite a sua nota da segunda prova: "))
n3 = float(input("Digite a sua nota da terceira prova: "))
while n3 < 0 and n3 > 10:
    n3 = float(input("Nota invalida! Digite a sua nota da terceira prova: "))
media = (n1 + n2 + n3) / 3
if media >= 0 and media < 3:
    print(f"Voce foi reprovado, sua media foi de {media}")
elif media >= 3 and media < 7:
    print(f"Voce pode fazer o exame, sua media foi de {media}")
elif media >= 7 and media <= 10:
    print(f"Voce foi aprovado, sua media foi de {media}")

# Ex04:
n1 = float(input("Digite o primeiro numero: "))
while n1 <= 0:
    n1 = float(input("Numero invalida! Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
while n2 <= 0:
    n2 = float(input("Numero invalida! Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
while n3 <= 0:
    n3 = float(input("Numero invalida! Digite o terceiro numero: "))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("É possível fazer um triângulo com essas medidas")
else:
    print("Não é possível fazer um triângulo com essas medidas")

# Ex05:
while True:
    sexualidade = int(input("Informe a sua sexualidade: \n"
                            "1 - Homem\n"
                            "2 - Mulher"))
    if sexualidade == 1:
        print("Você é um homem.")
        altura = float(input("Informe a sua altura: ").replace(",", "."))
        pesoIdealHomens = (72.7 * altura) - 58
        print(
            f"O peço ideal para a sua altura é de {round(pesoIdealHomens, 2)}")
    elif sexualidade == 2:
        print("Você é uma mulher.")
        altura = float(input("Informe a sua altura: ").replace(",", "."))
        pesoIdealMulher = (62.1 * altura) - 44.7
        print(
            f"O peço ideal para a sua altura é de {round(pesoIdealMulher, 2)}")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        continue
    break


# Funções:

# Um número inteiro e que retorne o valor do fatorial deste número:
def calcularFatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
numero = 5
resultado = calcularFatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

# Um número inteiro e que retorne True se o número for par, e False caso contrário:
def parImpar(numero):
    if numero % 2 == 0:
        print("True")
    else:
        print("False")
    return numero
parImpar(5)
parImpar(4)
parImpar(10)

# Dois números inteiros e que retorne o maior entre eles:
def maiorNumeros(n1, n2):
    return max(n1, n2)
n1 = 10
n2 = 20
maior = maiorNumeros(n1, n2)
print(f"O maior número entre {n1} e {n2} é {maior}")

# Um número inteiro e que retorne o dobro deste número:
def dobroNumero(numero):
    return numero * 2
numero = 5
resultado1 = dobroNumero(numero)
print(f"O dobro de {numero} é {resultado1}")

numero = 10
resultado2 = dobroNumero(numero)
print(f"O dobro de {numero} é {resultado2}")

# Estrutura Sequencial:

# Ex01:
n1 = float(input("Informr o primeiro numero: ").replace(",", "."))
n2 = float(input("Informr o segundo numero: ").replace(",", "."))
n3 = float(input("Informr o terceiro numero: ").replace(",", "."))
media = (n1 + n2 + n3) / 6
print(f"A média aritmética de {n1}, {n2} e {n3} é {round(media, 2)}")

# Ex02:
anoNascimento = int(input("Informe o seu ano de nascimento: "))
idadeAtual = 2023 - anoNascimento
idade2050 = 2050 - anoNascimento

print(f"Esse ano voce estará com {idadeAtual} anos")
print(f"Em 2050 você estará com {idade2050} anos")

# Ex 03:
a = float(input("Informe o coeficiente A: "))
b = float(input("Informe o coeficiente B: "))
c = float(input("Informe o coeficiente C: "))

delta = b**2 - 4*a*c

if delta >= 0:
    raizDelta = delta ** 0.5
    x1 = (-b + raizDelta) / (2*a)
    x2 = (-b - raizDelta) / (2*a)
    print(f"As raizes da equação são: x1 = {round(x1, 2)} e x2 = {x2}")
else:
    print("A equação não possui raizes reais")

# Ex04:
numero = float(input("Informe um numero: ").replace(",", "."))
x1 = print(f"{numero} x 1 = {numero * 1}")
x2 = print(f"{numero} x 2 = {numero * 2}")
x3 = print(f"{numero} x 3 = {numero * 3}")
x4 = print(f"{numero} x 4 = {numero * 4}")
x5 = print(f"{numero} x 5 = {numero * 5}")
x6 = print(f"{numero} x 6 = {numero * 6}")
x7 = print(f"{numero} x 7 = {numero * 7}")
x8 = print(f"{numero} x 8 = {numero * 8}")
x9 = print(f"{numero} x 9 = {numero * 9}")
x10 = print(f"{numero} x 10 = {numero * 10}")

# Estruturas de Repetição - FOR:

# Ex 01:
for x in range(1, 11):
    dobro = x * 2
    print(f"o dobro de {x} é {dobro}")

# Ex02:
for i in range(1, 11):
    if i % 2 != 0:
        print(f"Numeros impares: {i}")
print()
for x in range(1, 11):
    if x % 2 == 0:
        print(f"Numeros pares: {x}")

# Ex03:
numero = float(input("Informe um numero: ").replace(",", "."))
for i in range(1, 11):
    multiplicacao = numero * i
    print(f"A multiplicação de {numero} x {i} = {multiplicacao}")

# Ex 04:
n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
menor = min(n1, n2)
maior = max(n1, n2)
for numero in range(menor, maior + 1):
    print(numero)

# Ex 05:
numero = int(input("Informe o numero: "))
soma = 0
for i in range(numero + 1):
    soma += i
print(f"A soma de todos os numeros entre 1 e {numero} é {soma}")

# Ex 09:

media_idade = 0
peso_maior_90 = 0
for i in range(1, 7):
    print(f"[Pessoa {i}]")
    idade = int(input("Informe a idade: "))
    media_idade += idade
    peso = float(input("Informe o peso: ").replace(",", "."))
    if peso > 90:
        peso_maior_90 += 1
media_idade = media_idade / 7
print("")
print(f"Media idades: {round(media_idade, 2)}")
print(f"Qunatidade de pessoas com mais de 90kg: {peso_maior_90}")


# Estruturas de Dados:
# Ex 05:
meses = [
    "janeiro", "fevereiro", "março", "abril",
    "maio", "junho", "julho", "agosto",
    "setembro", "outubro", "novembro", "dezembro"
]
data = input("Informe a data no formato DD/MM/AAAA: ")
dia, mes, ano = data.split("/")
mes_extenso = meses[int(mes) - 1]
print(f"A data digitada é {dia} de {mes_extenso} de {ano}")



