import string

print("\n\tConversão numérica")

# Lista de caracteres
caracteres = [str(num) for num in range(10)]   # numéricos
alfabeticos = list(string.ascii_uppercase)  # alfabéticos

caracteres.extend(alfabeticos)
caracteres.extend(["!","@","#","$"])    # símbolos

# Entrada
# número de entrada
numero = (input("\nDigite um valor positivo maior que zero (0): "))

# Transforma todas as letras que o usuário digitou em maiúsculas
numero = numero.upper()

# Verifica se o número digitado na entrada é válido
def menor_igual_a_zero (num_usuario):
    # Verifica se o valor é negativo
    if "-" in num_usuario:
        return True
    # Verifica se o valor é zero
    if num_usuario == "0":
        return True
    return False 

# Verifica se todos os caracteres digitados estão dentro da lista de caracteres
def verif(num_usuario, lista):
    for caractere in num_usuario:
        if caractere not in lista:
            return False
    v = menor_igual_a_zero(num_usuario)
    if v:
        return False
    return True

verifica = verif(numero, caracteres)

# Em caso de número errado na entrada, repete a mensagem de aviso para o usuário até
# que o número esteja correto.
if not verifica:
    print(f"\nO caractere que você digitou não foi reconhecido!")
    print(f"Lista de caracteres disponíveis: {caracteres}\n")
    while not verifica:
        numero = input("\tDigite um número com caracteres válidos que seja positivo e maior que zero (0): ")
        numero = numero.upper()
        verifica = verif(numero, caracteres)

# base do número
base_num = (input("Digite a base do número informado (2 a 40): "))

# Exibe a mensagem de aviso em caso de bases incorretas
while not base_num.isdigit() or int(base_num) < 2 or int(base_num) > 40:
    base_num = input("\tA base deve ser de 2 a 40: ")

base_num = int(base_num)
    
# base que deseja converter
base = (input("Digite a base que deseja converter (2 a 40): "))

# Exibe a mensagem de aviso em caso de bases incorretas
while not base.isdigit() or int(base) < 2 or int(base) > 40:
    base = input("\tA base deve ser de 2 a 40: ")

base = int(base)

# Quantidade de algarismos que existe no valor
def algarismo (num_usuario):
    tamanho = len(num_usuario)
    return tamanho

# Converte o número para decimal
def conversao_decimal(num_usuario,base_numero,lista):
    quant = algarismo(num_usuario)
    decimal = 0
    # Faz a conversão para inteiro baseada nos índices da lista de caracteres
    for indice in num_usuario:
        if indice in lista:
            indice = lista.index(indice)
            quant-=1
            conta = indice*pow(base_numero,quant)
            decimal = decimal + conta
    return decimal

# Realiza a conversão final
def conversao_final (base_conversao,num_decimal,lista):
    # Primeiro a variável de resultado recebe o primeiro resto 
    rest = num_decimal % base_conversao
    # Conversão para o caractere da lista:
    # Procura o número/letra/símbolo a partir do índice (resto) que retorna o caractere correspondente
    resultado = lista[rest]
    # Depois é realizado o cálculo para somar os outros restos
    while num_decimal > 0:
        div = num_decimal // base_conversao
        # Realiza a atribuição do resultado apenas se o resultado da divisão não deu zero
        if div != 0:
            rest = div % base_conversao
            resto = lista[rest]
            resultado = resultado + resto
        num_decimal = div
    return resultado [::-1] # Inverte a string

# Impressão
print("\n................................................\n")  

if base_num == base:
    print(f"O número convertido é: \n{numero}\n")
elif base == 10:
    decimal = conversao_decimal(numero,base_num,caracteres)
    print(f"O número convertido é: \n{decimal}\n")
else:
    decimal = conversao_decimal(numero,base_num,caracteres)
    conversao = conversao_final(base,decimal,caracteres)
    print(f"O número convertido é: \n{conversao}\n")