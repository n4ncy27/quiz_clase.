#Programa ejercicio 4. convertir una cantidad dada de °c en su equivalencia a °k y °f 
print("---------------------------------")
print("--CONVERTIDOR DE °c A °K y °F----")
print("---------------------------------")

#input 
c = int(input("ingrse el valor de la temperatur en °c:"))


#proceso
k= c + 273.15
f= c * (5/9) + 32

#output
print( str (c) + "°c son: " + str (k) + " k")
print( str (c) + "°c son: " + str (f) + " f")
