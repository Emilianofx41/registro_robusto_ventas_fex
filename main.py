"""
Diagramado por: Emiliano Rodriguez
Pasado a codigo por: Geminno (Google/Alphabet)
Modificaciones: Estilizacion con Libreria Colorama: Copilot (OpenAI/Microsoft)

Este módulo implementa un sistema de registro de ventas con validación de entrada
y manejo de errores"""

from colorama import Fore, Style, init


init(autoreset=True)

COLOR_TITULO = Fore.CYAN + Style.BRIGHT
COLOR_MENU = Fore.CYAN
COLOR_EXITO = Fore.GREEN
COLOR_ERROR = Fore.RED
COLOR_AVISO = Fore.YELLOW

def registrar_venta(p_unit=0, cant=0):
    """Solicita los datos de la venta al usuario y calcula el total.
    
    Implementa un bucle de reintento mediante try-except-else-finally para
    garantizar que la entrada sea numéricamente válida y cumpla con las
    reglas de negocio (precio mayor o igual a 0 y cantidad mayor a 0).
    
    Returns:
        None
    """

    
    try:
        # Entrada y conversión de datos
        if p_unit == 0 and cant == 0:
            p_unit = float(input(f"{COLOR_MENU}Precio unitario del producto: "))
            if p_unit < 0:
                raise ValueError("Precio inválido")

            cant = int(input(f"{COLOR_MENU}La cantidad vendida: "))
            if cant <= 0:
                raise ValueError("Cantidad inválida")

        # Cálculo de la operación
        total = p_unit * cant

    except ValueError as e:
        # Evaluación de mensajes nativos vs personalizados
        mensaje_error = str(e)
        if "could not convert string to float" in mensaje_error or "invalid literal for int()" in mensaje_error:
            mensaje_error = "No se puede admitir texto como dato válido"
        registro_resultado = "Sin exito"
        print(f"{COLOR_ERROR}Error: {mensaje_error}")

    else:
        # Salida exitosa y actualización de bandera
        print(f"{COLOR_EXITO}Venta registrada con éxito. Total a pagar: ${total:.2f}")
        registro_resultado = "Con éxito"

    finally:
        # Ejecución garantizada incondicionalmente
        color_resultado = COLOR_EXITO if registro_resultado == "Con éxito" else COLOR_ERROR
        print(f"{color_resultado}Operación Finalizada {registro_resultado}\n")
    return total    


def programa_principal():
    """Controla el flujo de ejecución del programa de ventas.
    
    Muestra la bienvenida, invoca la función de registro e interactúa
    con el usuario a través de un submenú con validación de opciones.
    
    Returns:
        None
    """
    print(f"{COLOR_TITULO}=== BIENVENIDO AL SISTEMA DE REGISTRO DE VENTAS ===")
    program = True

    while program == True:
        # Llamada a la función modularizada
        registrar_venta()

        # Control del submenú con su propio bloque de protección
        while True:
            try:
                print(f"{COLOR_MENU}--- Submenú ---")
                print(f"{COLOR_MENU}1. Registrar otra venta")
                print(f"{COLOR_MENU}2. Salir")
                opcion = int(input(f"{COLOR_MENU}Ingrese número de opción: "))

                # Validación de la expresión lógica (distinto de 1 Y distinto de 2)
                if not (opcion == 1 or opcion == 2):
                    print(f"{COLOR_AVISO}Error: Opción inválida. Ingrese 1 o 2.")
                else:
                    if opcion == 1:
                        break  # Continúa el bucle principal (program == True)
                    elif opcion == 2:
                        program = False
                        break

            except ValueError:
                print(f"{COLOR_ERROR}Error: Ingrese un valor numérico válido para la opción.")

    print(f"{COLOR_TITULO}Programa finalizado. ¡Hasta luego!")


programa_principal()