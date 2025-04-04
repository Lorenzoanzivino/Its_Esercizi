''' 1-5
    Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula
    gradiCelsius=5∗(gradiFahrenheit−32)/9
    Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.
    La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile
    con una precisione di un decimo di grado.'''

gradi_fahrenheit: int = 72
gradi_Celsius = 5*(gradi_fahrenheit - 32)/9

print(f"{gradi_fahrenheit}°F corrispondono a {gradi_Celsius:.1f}°C")