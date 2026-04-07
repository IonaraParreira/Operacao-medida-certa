from colorama import Fore,Style,init
init(autoreset=True)
peso = float(input("Digite seu peso (kg): "))
altura_input = input("Digite sua altura (m): ")
altura = float(altura_input.replace(',','.'))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print(f"{Fore.YELLOW}⚠️ Alerta:{Style.RESET_ALL}O sistema detectou vulnerabilidade por baixo peso.")
elif imc < 25:
    print(f"{Fore.GREEN}Acesso Permitido:{Style.RESET_ALL} Você está protegido e saudável,junte-se aos sobreviventes e faça parte da repopulação da humanidade.")
else:
    print(f"{Fore.RED}Acesso Negado:{Style.RESET_ALL} O sistema detectou {Fore.RED}humano infectado☣️{Style.RESET_ALL}, recomenda medidas de segurança imediatas.{Fore.BLUE}Praticar mais atividades físicas,reduzir açúcar e ingerir bastante água.{Style.RESET_ALL}")