peso = float(input("Digite seu peso (kg): "))
altura_input = input("Digite sua altura (m): ")
altura = float(altura_input.replace(',','.'))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Alerta: O sistema detectou vulnerabilidade por baixo peso.")
elif imc < 25:
    print("Acesso Permitido: Você está protegido e saudável,junte-se aos sobreviventes e faça parte da repopulação da humanidade.")
else:
    print("Acesso Negado: O sistema detectou humano infectado,recomenda medidas de segurança imediatas.Praticar mais atividades físicas,reduzir açúcar e ingerir bastante água.")