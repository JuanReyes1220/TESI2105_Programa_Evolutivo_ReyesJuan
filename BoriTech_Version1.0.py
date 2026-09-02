# --- CONSTANTE ---                                            #--Version 2.0---
IMPUESTO_IVU = 0.115

# --- CICLO PRINCIPAL (Versión 2.0) ---
continuar = "s"

while continuar.lower() == "s":
    print("\n--- REGISTRO DE NUEVO EQUIPO ---")
    nombre_equipo = input("Ingrese el nombre del equipo electrónico: ")
    precio_unitario_texto = input("Ingrese el precio del equipo electrónico ($): ")
    cantidad_texto = input("Ingrese la cantidad de unidades recibidas: ")
    
    # Conversión de datos
    precio_unitario = float(precio_unitario_texto)
    cantidad = int(cantidad_texto)
    
    # Decisión 1: Validación de entrada de datos
    if precio_unitario > 0 and cantidad > 0:
        subtotal = precio_unitario * cantidad
        
        # Decisión 2: Descuento si la compra supera los $500
        if subtotal > 500:
            descuento = subtotal * 0.05
            print("\n¡Se aplicó un 5% de descuento por compra mayor a $500!")
        else:
            descuento = 0.0
            
        subtotal_con_descuento = subtotal - descuento
        monto_impuesto = subtotal_con_descuento * IMPUESTO_IVU
        costo_total_inventario = subtotal_con_descuento + monto_impuesto
        
        # Salida de resultados
        print("\n" + "=" * 40)
        print("   RESUMEN DE REGISTRO DE INVENTARIO   ")
        print("=" * 40)
        print(f"Equipo registrado:       {nombre_equipo}")
        print(f"Cantidad de unidades:    {cantidad}")
        print(f"Precio por unidad:       ${precio_unitario:.2f}")
        print(f"Subtotal inicial:        ${subtotal:.2f}")
        print(f"Descuento aplicado:      ${descuento:.2f}")
        print(f"Impuesto estimado (IVU): ${monto_impuesto:.2f}")
        print(f"Costo total abonado:     ${costo_total_inventario:.2f}")
        print("=" * 40)
    else:
        print("\n[ERROR] El precio y la cantidad deben ser valores mayores a cero.")
    
    # Criterio de repetición
    continuar = input("\n¿Desea ingresar otro equipo? (s/n): ")

print("\nPrograma finalizado. ¡Gracias por usar el sistema!")
