from colorama import Fore, Style

usuario_correto = "j.uliasw"
senha_correta = "judri0105"

def calcular_notas(a, b, c):
    soma_avaliacao = (a + b) / 2 
    media = (c + soma_avaliacao) / 2
    return media

def obter_notas():
    a = float(input("Qual foi sua nota de AI? "))
    b = float(input("Qual foi sua nota de AF? "))
    c = float(input("Qual foi a nota da sua prova final? "))
    return [a, b, c]

def menu_login():
    print(Fore.MAGENTA + "Bem-vindo(a) ao sistema de cálculo de notas da Julia!")

while True:
    menu_login()
    usuario = input("digite seu nome de usuário: ")
    senha = input("digite sua senha: ")
    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vinda Julia!")
        a, b, c = obter_notas()
        resultado = calcular_notas(a, b, c)
        print(f"Sua média é: {resultado}")
    else:
        print(Fore.RED + f"Usuário ou senha incorretos, tente novamente!")
    break