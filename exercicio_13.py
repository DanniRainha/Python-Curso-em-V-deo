# A proposta do exercício é de receber o atual salário do funcionário, calcular
# um aumento de 15% e exibir o salário atualizado.

salario = float(input("Digite o atual salário para o cálculo do aumento: "))
novo_salario = (salario * 1.15)
print(f"O novo salário é de R${novo_salario:.2f}.")
