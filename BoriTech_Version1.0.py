# --- CONSTANTE ---
IMPUESTO_IVU = 0.115  # Constante en mayúsculas para el impuesto (11.5%)

# --- ENTRADA DE DATOS ---
nombre_equipo = input("Ingrese el nombre del equipo electrónico: ")
precio_unitario_texto = input("Ingrese el precio del equipo electrónico ($): ")
cantidad_texto = input("Ingrese la cantidad de unidades recibidas: ")

# --- CONVERSIÓN DE DATOS Y TIPOS DE DATOS ---
# Conversión de texto (str) a decimal (float) y entero (int)
precio_unitario = float(precio_unitario_texto)
cantidad = int(cantidad_texto)

# --- CÁLCULOS ---
subtotal = precio_unitario * cantidad
monto_impuesto = subtotal * IMPUESTO_IVU
costo_total_inventario = subtotal + monto_impuesto

# --- SALIDA DE RESULTADOS ---
print("\n" + "=" * 40)
print("   RESUMEN DE REGISTRO DE INVENTARIO   ")
print("=" * 40)
print(f"Equipo registrado:       {nombre_equipo}")
print(f"Cantidad de unidades:    {cantidad}")
print(f"Precio por unidad:       ${precio_unitario:.2f}")
print(f"Subtotal del inventario: ${subtotal:.2f}")
print(f"Impuesto estimado (IVU): ${monto_impuesto:.2f}")
print(f"Costo total abonado:     ${costo_total_inventario:.2f}")
print("=" * 40)
