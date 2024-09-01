print("Bem vindo(a)! Calculadora de Tinta")
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
print(f"Sua parede tem a dimensão de {largura} x {altura} e sua área é de {largura * altura}m².")
print(f"Para pintar este ambiente, serão necessários {largura * altura / 2} litros de tinta.")
# A proposta do exercício era receber os valores de altura e largura de uma parede,
# calcular a sua área e calcular a quantidade necessária de tinta para pintar este
# ambiente, onde a cada 1 litro de tinta, 2m² devem ser pintados.