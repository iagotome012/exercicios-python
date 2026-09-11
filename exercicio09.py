#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
#   mostre a temperatura em graus Celsius.

tempF = float(input("digite a temperatura em graus Fahrenheit: "))

tempC = 5 * ((tempF-32) / 9)
print("A temperatura em graus celcius é:" , tempC)