# O exercício proposto foi para perguntar quantos KM foram percorridos com o carro alugado,
# e a quantidade de dias ao qual foi alugado, para calcular quanto que o cliente
# deveria pagar ao final, sabendo que a diária é de R$60 e o KM rodado é de R$0,15.

km = float(input("Digite a quantidade de KMs utilizado: "))
diaria = int(input("Digite a quantidade de dias usado: "))
valor = (km * 0.15) + (diaria * 60)
print(f"Com {km}km percorridos e {diaria} dias locado, o valor a pagar é de R${valor}.")
