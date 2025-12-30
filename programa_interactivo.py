import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.image as mpimg


# -------------------------------
# Función para mostrar secciones del Markdown
# -------------------------------
def mostrar_seccion(seccion, pausa=True):
    encabezados = {
        "1": "Tema, problema y solución",
        "2": "Fuente, definición, estructura, tipos y escala",
        "3": "Pasos, pseudocódigo y diagrama del programa",
        "4": "Estadística",
        "6": "Insights",
        "8": "Aplicación de modelos de Machine Learning",
        "10": "Sugerencias de Copilot",   
        "11": "Regresión Lineal",
        "12": "Clasificación supervisada con Random Forest",
        "13": "Dashboard en Power BI – Tienda Aurelion",
        "14": "Objetivo",
        "15": "General",
        "16": "Clientes",
        "17": "Productos y Categorías",
        "18": "Medios de Pago",
        "19": "Conclusión"
    }

    titulo = encabezados.get(seccion)
    if not titulo:
        print("Opción no válida.")
        return

    try:
        with open("documentacion.md", "r", encoding="utf-8") as archivo:
            mostrar = False
            buffer = []

            for linea in archivo:
                if linea.strip().startswith("##") and titulo in linea:
                    mostrar = True
                    buffer.append(linea)
                    continue
                if mostrar:
                    if linea.strip().startswith("##") and titulo not in linea:
                        break
                    buffer.append(linea)

            if buffer:
                print("\n" + "".join(buffer).strip())
            else:
                print("Sección no encontrada en el archivo.")
    except FileNotFoundError:
        print(" El archivo 'documentacion.md' no fue encontrado.")

    if pausa:
        input("\nPresione Enter para volver al menú ")

#---------------
# Mostrar imágenes
#----------------

def mostrar_imagen(ruta):
    img = mpimg.imread(ruta)
    plt.figure(figsize=(8,5))
    plt.imshow(img)
    plt.axis("off")
    plt.tight_layout()
    plt.show()



# -------------------------------
# Submenú Dashboard
# -------------------------------
def mostrar_dashboard():
    while True:
        print("\n=== Dashboard Power BI ===")
        print("1. Objetivo")
        print("2. General")
        print("3. Clientes")
        print("4. Productos y Categorías")
        print("5. Medios de Pago")
        print("6. Conclusión")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_seccion("14")
        elif opcion == "2":
            mostrar_seccion("15")
        elif opcion == "3":
            mostrar_seccion("16")
        elif opcion == "4":
            mostrar_seccion("17")
        elif opcion == "5":
            mostrar_seccion("18")
        elif opcion == "6":
            mostrar_seccion("19")
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

# -------------------------------
# Estadística
# -------------------------------
def mostrar_estadisticas():

    print("\n=== ESTADÍSTICA DEL DATASET ===\n")

    # Mostrar la sección de documentación correspondiente
    mostrar_seccion("4")   



# -------------------------------
# EDA
# -------------------------------
def mostrar_eda():
    while True:
        print("\n=== Exploratory Data Analysis ===")
        print("1. Heatmap de correlaciones")
        print("2. Pairplot de variables clave")
        print("3. Boxplots en subplots")
        print("4. Explicación breve del EDA")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Heatmap de correlaciones (imagen pregenerada)
            mostrar_imagen("graficos/corr_matrix.png")

        elif opcion == "2":
            # Pairplot de variables clave (imagen pregenerada)
            mostrar_imagen("graficos/relacion_cant_precio_importe.png")

        elif opcion == "3":
            # Boxplots en subplots (imagen pregenerada)
            mostrar_imagen("graficos/distribucion.png")

        elif opcion == "4":
            print("\n Explicación breve del EDA:")
            print("- El heatmap muestra correlaciones numéricas globales.")
            print("- El pairplot enseña cómo se relacionan cantidad, precio e importe, coloreado por categoría.")
            print("- Los boxplots en subplots muestran la dispersión y outliers de cada variable en su propia escala.")
            print(" En conjunto, estos gráficos permiten detectar patrones, relaciones y valores extremos.")

        elif opcion == "0":
            break
        else:
            print(" Opción inválida, intente nuevamente.")

# -------------------------------
# Funciones de gráficos (inicio)
# -------------------------------
def mostrar_viz():
    while True:
        print("\n=== Visualizaciones de Negocio ===")
        print("1. Ventas únicas por mes (barras)")
        print("2. Importe promedio por día del mes (scatter + regresión)")
        print("3. Distribución por medio de pago (torta)")
        print("4. Boxplot de importe por medio de pago")
        print("5. Ventas por ciudad (barplot)")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Ventas por mes
            mostrar_imagen("graficos/dist_temporal.png")

        elif opcion == "2":
            # Importe promedio por día del mes
            mostrar_imagen("graficos/importe_promedio.png")

        elif opcion == "3":
            # Distribución por medio de pago
            mostrar_imagen("graficos/dist_mediosP.png")

        elif opcion == "4":
            # Boxplot de importe por medio de pago
            mostrar_imagen("graficos/dist_mediosP_boxplot.png")

        elif opcion == "5":
            # Ventas por ciudad
            mostrar_imagen("graficos/ventas_ciudad.png")

        elif opcion == "0":
            break

        else:
            print(" Opción inválida, intente nuevamente.")


# -------------------------------
# Modelos de Machine Learning
# -------------------------------
def mostrar_ml():
    while True:
        print("\n=== Modelos de Machine Learning ===")
        print("1. Introducción a ML")
        print("2. Regresión Lineal")
        print("3. Clasificación con Random Forest")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_seccion("8")

        elif opcion == "2":
            mostrar_seccion("11", pausa=False)
            input("\nPresione Enter para ver los gráficos...")

            for ruta in ["graficos/regresion_scatter.png",
                         "graficos/regresion_coef.png"]:
                mostrar_imagen(ruta)

            input("\nPresione Enter para volver al menú ")

        elif opcion == "3":
            mostrar_seccion("12", pausa=False)
            input("\nPresione Enter para ver los gráficos...")

            for ruta in ["graficos/RF_matriz.png",
                         "graficos/RF_featureImportance.png"]:
                mostrar_imagen(ruta)

            input("\nPresione Enter para volver al menú ")

        elif opcion == "0":
            break

        else:
            print("Opción inválida, intente nuevamente.")

# -------------------------------
# Menú principal
# -------------------------------
def menu():
    while True:
        print("\n Menú de Documentación")
        print("1. Ver tema, problema y solución")
        print("2. Ver información del dataset")
        print("3. Ver pseudocódigo y diagrama")
        print("4. Ver EDA")
        print("5. Ver estadísticas")
        print("6. Ver insights")
        print("7. Ver gráficos")
        print("8. Ver modelos de ML")
        print("9. Ver Dashboard Power BI")
        print("10. Ver sugerencias de Copilot")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == "11":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif opcion == "4":
            mostrar_eda()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "7":
            mostrar_viz()
        elif opcion == "8":
            mostrar_ml()
        elif opcion == "9":
            mostrar_dashboard()
        elif opcion in ["1", "2", "3", "6", "10"]:
            mostrar_seccion(opcion)
        else:
            print("Opción no válida.")


# -------------------------------
# Punto de entrada
# -------------------------------
if __name__ == "__main__":
    menu()
        