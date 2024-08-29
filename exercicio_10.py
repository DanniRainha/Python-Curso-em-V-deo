# Leia qual o valor desejado e veja quantos dólares pode comprar,
# sendo US$1,00 = R$3,27.
print("A atual cotação do dólar está em US$1,00 = R$3,27.")
carteira = float(input("Digite o valor que possui em R$: "))
print(f"Com o valor R${carteira} você poderá comprar US${carteira / 3.27:.2f}.")