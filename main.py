'''Se debe modificar la clase CuentaBancaria para que sea abstracta, 
ademas los metodos extraer y depositar deben volverse abstractos.
Tambien se debe crear una clase CuentaAhorro que herede de CuentaBancaria 
y se le agregue un atributo privado de tasa de interes, 
el cual tendra un valor establecido de 0.001 y un metodo que nos calcule el interes.
'''

from cb import CuentaAhorro
from cc import CuentaCorriente

ahorro = CuentaAhorro("Gabriel", 333333, "1990/02/03", 15000)
corriente = CuentaCorriente("Lali", 444444, "1988/05/12", 8000)

print("Edad de Gabriel:", ahorro.obtener_edad())
ahorro.depositar(1000)
ahorro.calcular_interes()
ahorro.extraer(500)

corriente.depositar(2000)
corriente.extraer(600)   # debería fallar por el límite
corriente.extraer(400)   # extracción válida
