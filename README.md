# ASD_RECURSIVO_JUANLOZANO

## Requisitos del Sistema:

1. **Python 3.x**
2. No se requieren librerías externas (solo módulos estándar de Python).

## Instalación:

Al ser una implementación nativa en Python, solo necesitas clonar el repositorio y asegurarte de estar en la carpeta raíz:

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

## Guía de Uso Rápido:

1. **Definir la Gramática:**
   Las gramáticas se encuentran preconfiguradas en el archivo `gramatica.py`. Puedes editar el diccionario para probar nuevas reglas siguiendo este formato:
   ```python
   'NO_TERMINAL': [['produccion', '1'], ['produccion', '2'], ['ε']]
   ```

2. **Ejecutar el programa:**
   Desde la terminal, ejecuta el script principal:
   ```bash
   python3 main.py
   ```

3. **Ver los resultados:**
   El programa imprimirá en consola de forma organizada:
   * **FIRST:** Conjunto de terminales que inician las producciones de cada No Terminal.
   * **FOLLOW:** Conjunto de terminales que pueden aparecer inmediatamente a la derecha de un No Terminal.
   * **PREDICT:** Conjunto de terminales que determinan qué regla de producción debe elegir el parser.

## Estructura del Proyecto:

* **`algoritmos.py`**: Contiene la lógica recursiva para el cálculo de conjuntos y el manejo de la cadena vacía (epsilon).
* **`gramatica.py`**: Archivo de configuración donde se definen las producciones de los ejercicios 1 y 2 vistos en clase.
* **`main.py`**: Punto de entrada que orquesta la ejecución y formatea la salida en consola.

## Notas de Implementación:

* **Manejo de Epsilon:** Se utiliza el carácter `ε` (o `e`) para representar la cadena vacía. Los algoritmos filtran este símbolo durante el cálculo de `FOLLOW` según las reglas del curso.
* **Recursividad Izquierda:** Se incluyó un bloque `try-except` para manejar la **Gramática 1** de las diapositivas, ya que contiene recursividad izquierda directa (`S -> S dos`), lo cual genera un bucle infinito en algoritmos ASD estándar sin previa factorización.
* **Símbolo de Parada:** El símbolo `$` se añade automáticamente al conjunto `FOLLOW` del símbolo inicial de la gramática.

---
