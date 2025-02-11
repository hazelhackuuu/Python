   #TERMOMETRO
                                    
                                    
#PEQUEÑO PROYECTO UTILIZANDO DATOS DE ENTRADA, VARIBALES Y NUMEROS FLOTANTES.


temperatura= float(input("Ingrese temeperatura:"))

escala = input("¿Es Farenheit (F) o es Celsius(C)?")

if escala  == "F":
    
    celsius = (temperatura - 32) * 5/9 
    
    print(celsius)
    
elif escala == "C":
    
    fahrenheit = temperatura *1.8 + 32
    
    print(fahrenheit)
