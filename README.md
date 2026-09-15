# 🛒 Registro Robusto de Ventas

Programa interactivo en Python desarrollado con una arquitectura modular, aislamiento de dependencias y un sistema integral de **manejo de excepciones** mediante el patrón `try / except / else / finally`.

---

## 📌 Descripción del Proyecto

El sistema permite solicitar la entrada del precio unitario y la cantidad vendida de un producto, calculando el importe total de la transacción. Previene la interrupción inesperada del programa frente a datos erróneos mediante:

* **EAFP (Easier to Ask for Forgiveness than Permission):** Captura de fallos en conversión de tipos de datos.
* **LBYL (Look Before You Leap):** Validación preventiva de reglas de negocio (precio < 0 y cantidad <= 0).
* **Garantía de ejecución:** Bloque `finally` incondicional para notificar el estado del cierre de cada operación.

---

## 🛠️ Tecnologías y Entorno

* **Lenguaje:** Python 3.x
* **Aislamiento:** Entorno virtual (`.venv`)
* **Gestor de paquetes:** `pip`

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone [https://github.com/emilianofx41/registro_robusto_ventas_jer.git](https://github.com/emilianofx41/registro_robusto_ventas_jer.git)
cd registro_robusto_ventas_jer