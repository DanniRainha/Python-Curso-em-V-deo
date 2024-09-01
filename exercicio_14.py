# O exercício proposto foi para criar um conversor de temperaturas, 
# onde o usuário digita a temperatura em °C para ser exibido em °F.

temperatura = float(input("Digite a temperatura em °C que deseja converter: "))
converter = (temperatura * 9 / 5) + 32
print(f"A temperatura de {temperatura}°C convertida fica em {converter}°F.")
