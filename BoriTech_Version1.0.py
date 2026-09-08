# --- CONSTANTES ---
IMPUESTO_IVU = 0.115


# --- FUNCIONES ---
def solicitar_datos_equipo():
    """Solicita los datos del equipo al usuario y realiza las conversiones."""
    nombre = input("Ingrese el nombre del equipo electrónico: ")
    precio = float(input("Ingrese el precio del equipo electrónico ($): "))
    cantidad = int(input("Ingrese la cantidad de unidades recibidas: "))
    return nombre, precio, cantidad


def calcular_totales_inventario(subtotal, impuesto_rate):
    """Calcula el descuento, impuesto y total abonado."""
    if subtotal > 500:
        descuento = subtotal * 0.05
        print("\n¡Se aplicó un 5% de descuento por compra mayor a $500!")
    else:
        descuento = 0.0

    subtotal_con_descuento = subtotal - descuento
    monto_impuesto = subtotal_con_descuento * impuesto_rate
    costo_total = subtotal_con_descuento + monto_impuesto

    return descuento, subtotal_con_descuento, monto_impuesto, costo_total


def mostrar_resumen(nombre, cantidad, precio, subtotal, descuento, monto_impuesto, costo_total):
    """Muestra los resultados del registro en pantalla de forma limpia."""
    print("\n" + "=" * 40)
    print("  RESUMEN DE REGISTRO DE INVENTARIO  ")
    print("=" * 40)
    print(f"Equipo registrado:       {nombre}")
    print(f"Cantidad de unidades:    {cantidad}")
    print(f"Precio por unidad:       ${precio:.2f}")
    print(f"Subtotal inicial:        ${subtotal:.2f}")
    print(f"Descuento aplicado:      ${descuento:.2f}")
    print(f"Impuesto estimado (IVU): ${monto_impuesto:.2f}")
    print(f"Costo total abonado:     ${costo_total:.2f}")
    print("=" * 40)


def procesar_registro():
    """Función principal que control el flujo del programa."""
    continuar = "s"

    while continuar.lower() == "s":
        print("\n--- REGISTRO DE NUEVO EQUIPO ---")
        
        # Uso de función para solicitar datos
        nombre_equipo, precio_unitario, cantidad = solicitar_datos_equipo()

        # Decisión 1: Validación de entrada de datos
        if precio_unitario > 0 and cantidad > 0:
            subtotal = precio_unitario * cantidad

            # Uso de función para cálculo de totales
            descuento, subtotal_desc, monto_impuesto, costo_total = calcular_totales_inventario(
                subtotal, IMPUESTO_IVU
            )

            # Uso de función sin 'return' explícito para mostrar la salida
            mostrar_resumen(
                nombre_equipo, cantidad, precio_unitario, subtotal, 
                descuento, monto_impuesto, costo_total
            )
        else:
            print("\n[ERROR] El precio y la cantidad deben ser valores mayores a cero.")

        # Criterio de repetición
        continuar = input("\n¿Desea ingresar otro equipo? (s/n): ")

    print("\nPrograma finalizado. ¡Gracias por usar el sistema!")


# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    procesar_registro()
    