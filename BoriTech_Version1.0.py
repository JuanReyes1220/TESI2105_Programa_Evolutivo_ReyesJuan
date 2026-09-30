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


def demostrar_laboratorio():
    """Muestra de manera sencilla los arreglos y cadenas del laboratorio."""
    print("\n" + "=" * 40)
    print(" DEMOSTRACIÓN DE ARREGLOS Y CADENAS ")
    print("=" * 40)

    # 1. Arreglo Unidimensional
    equipos = ["Laptop", "Monitor", "Teclado", "Mouse", "Impresora"]
    print("Arreglo completo:", equipos)
    print("Primer elemento:", equipos[0])
    print("Tercer elemento:", equipos[2])
    
    equipos[1] = "Monitor Samsung" # Modificar elemento
    print("Modificado (índice 1):", equipos)
    
    print("Recorrido del arreglo:")
    for eq in equipos:
        print("-", eq)

    # 2. Arreglo Multidimensional (Matriz)
    inventario_matriz = [
        ["Laptop", 5, 600.00],
        ["Tablet", 10, 250.00]
    ]
    print("\nMatriz multidimensional:")
    for fila in inventario_matriz:
        print(f"Equipo: {fila[0]} | Cantidad: {fila[1]} | Precio: ${fila[2]:.2f}")

    # 3. Cadenas de Caracteres
    texto = "Laptop Gamer"
    print(f"\nOperaciones con cadena ('{texto}'):")
    print("- Longitud:", len(texto))
    print("- Primer carácter:", texto[0])
    print("- ¿Contiene 'Gamer'?:", "Gamer" in texto)
    print("- En mayúsculas:", texto.upper())
    print("=" * 40)


def procesar_registro():
    """Función principal que controla el flujo del programa."""
    continuar = "s"

    while continuar.lower() == "s":
        print("\n--- REGISTRO DE NUEVO EQUIPO ---")
        
        nombre_equipo, precio_unitario, cantidad = solicitar_datos_equipo()

        if precio_unitario > 0 and cantidad > 0:
            subtotal = precio_unitario * cantidad

            descuento, subtotal_desc, monto_impuesto, costo_total = calcular_totales_inventario(
                subtotal, IMPUESTO_IVU
            )

            mostrar_resumen(
                nombre_equipo, cantidad, precio_unitario, subtotal, 
                descuento, monto_impuesto, costo_total
            )
        else:
            print("\n[ERROR] El precio y la cantidad deben ser valores mayores a cero.")

        continuar = input("\n¿Desea ingresar otro equipo? (s/n): ")

    # Al terminar el inventario, ejecuta la demostración del laboratorio
    demostrar_laboratorio()
    print("\nPrograma finalizado. ¡Gracias por usar el sistema!")


# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    procesar_registro()