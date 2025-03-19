def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Entrada de datos por teclado
monto1 = float(input("Ingrese el monto total de la primera compra: "))
monto2 = float(input("Ingrese el monto total de la segunda compra: "))
porcentaje2 = float(input("Ingrese el porcentaje de descuento para la segunda compra: "))

descuento1 = calcular_descuento(monto1)  # Usa el valor predeterminado del 10%
descuento2 = calcular_descuento(monto2, porcentaje2)  # Usa el porcentaje ingresado por el usuario

# Mostrar resultados
print(f"Compra de ${monto1}: Descuento ${descuento1:.2f}, Total a pagar ${monto1 - descuento1:.2f}")
print(f"Compra de ${monto2}: Descuento ${descuento2:.2f}, Total a pagar ${monto2 - descuento2:.2f}")
