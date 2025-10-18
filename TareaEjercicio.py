===============================================================================
           25 EJERCICIOS DE PRÁCTICA - ESTRUCTURA DE DATOS
     Contenidos: TAD, Complejidad Algorítmica y Pilas (Grupos 1-4)
===============================================================================

===============================================================================
SECCIÓN 1: TIPOS ABSTRACTOS DE DATOS (TAD)
Grupos 1 y 2 - Ejercicios 1 al 6
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 1 [BÁSICO]: TAD Punto2D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un TAD Punto2D que represente un punto en el plano cartesiano 
con coordenadas (x, y). Debe incluir operaciones para calcular la distancia 
al origen y la distancia entre dos puntos.

🔹 PSEUDOCÓDIGO:
   TAD Punto2D
      - Atributos: x, y (números reales)
      - Operaciones:
         * crear(x, y) → Punto2D
         * distanciaOrigen() → real
         * distanciaA(otroPunto) → real

✅ EJEMPLO RESUELTO:

```python
import math

class Punto2D:
    """TAD que representa un punto en el plano cartesiano"""
    
    def __init__(self, x: float, y: float):
        """
        Crea un nuevo punto con coordenadas (x, y)
        Precondición: x, y son números reales
        """
        self._x = x
        self._y = y
    
    def distancia_origen(self) -> float:
        """
        Calcula la distancia del punto al origen (0, 0)
        Postcondición: retorna un valor >= 0
        """
        return math.sqrt(self._x**2 + self._y**2)
    
    def distancia_a(self, otro: 'Punto2D') -> float:
        """
        Calcula la distancia entre este punto y otro punto
        Precondición: otro es un Punto2D válido
        Postcondición: retorna un valor >= 0
        """
        dx = self._x - otro._x
        dy = self._y - otro._y
        return math.sqrt(dx**2 + dy**2)
    
    def __str__(self):
        return f"({self._x}, {self._y})"
# ============================================================
# 🧪 PRUEBAS UNITARIAS
# ============================================================

class TestPunto2D(unittest.TestCase):

    def test_distancia_origen(self):
        p = Punto2D(3, 4)
        self.assertAlmostEqual(p.distancia_origen(), 5.0)

    def test_distancia_a_otro(self):
        p1 = Punto2D(3, 4)
        p2 = Punto2D(0, 0)
        self.assertAlmostEqual(p1.distancia_a(p2), 5.0)

    def test_distancia_cero(self):
        p = Punto2D(0, 0)
        self.assertEqual(p.distancia_origen(), 0.0)

    def test_str(self):
        p = Punto2D(1.5, -2.3)
        self.assertEqual(str(p), "(1.5, -2.3)")


# ============================================================
# 💡 EJEMPLO DE USO
# ============================================================
if __name__ == "__main__":
    # Ejecución de ejemplo
    p1 = Punto2D(3, 4)
    p2 = Punto2D(0, 0)
    print(f"Punto 1: {p1}")
    print(f"Distancia al origen: {p1.distancia_origen()}")   # 5.0
    print(f"Distancia entre puntos: {p1.distancia_a(p2)}")   # 5.0

    # Ejecutar pruebas unitarias
    unittest.main(argv=[''], exit=False)

```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 2 [BÁSICO]: TAD Rectangulo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Crear un TAD Rectangulo con base y altura. Implementar operaciones para 
calcular área, perímetro y verificar si es un cuadrado.

🔹 PSEUDOCÓDIGO:
   TAD Rectangulo
      - Atributos: base, altura (números reales positivos)
      - Operaciones:
         * crear(base, altura) → Rectangulo
         * calcularArea() → real
         * calcularPerimetro() → real
         * esCuadrado() → booleano

- CODIGO
import unittest

class Rectangulo:
    """
    TAD que representa un rectángulo en el plano cartesiano.

    Atributos:
        base (float): Longitud de la base del rectángulo.
        altura (float): Longitud de la altura del rectángulo.
    """

    def __init__(self, base: float, altura: float):
        """
        Inicializa un rectángulo con la base y la altura dadas.

        Precondición:
            - base > 0 y altura > 0.
        Complejidad:
            - Tiempo: O(1)
            - Espacio: O(1)
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Calcula el área del rectángulo.

        Returns:
            float: Área = base * altura

        Complejidad:
            - Tiempo: O(1)
            - Espacio: O(1)
        """
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del rectángulo.

        Returns:
            float: Perímetro = 2 * (base + altura)

        Complejidad:
            - Tiempo: O(1)
            - Espacio: O(1)
        """
        return 2 * (self.base + self.altura)

    def es_cuadrado(self) -> bool:
        """
        Verifica si el rectángulo es un cuadrado.

        Returns:
            bool: True si base == altura, False en caso contrario.

        Complejidad:
            - Tiempo: O(1)
            - Espacio: O(1)
        """
        return self.base == self.altura

    def __str__(self) -> str:
        """
        Retorna una representación en texto del rectángulo.

        Complejidad:
            - Tiempo: O(1)
            - Espacio: O(1)
        """
        return f"Rectángulo(base={self.base}, altura={self.altura})"


# ============================================================
# 🧪 PRUEBAS UNITARIAS
# ============================================================

class TestRectangulo(unittest.TestCase):

    def test_area(self):
        r = Rectangulo(4, 5)
        self.assertEqual(r.calcular_area(), 20)

    def test_perimetro(self):
        r = Rectangulo(3, 7)
        self.assertEqual(r.calcular_perimetro(), 20)

    def test_es_cuadrado_true(self):
        r = Rectangulo(5, 5)
        self.assertTrue(r.es_cuadrado())

    def test_es_cuadrado_false(self):
        r = Rectangulo(4, 6)
        self.assertFalse(r.es_cuadrado())


# ============================================================
# 💡 EJEMPLO DE USO
# ============================================================

if __name__ == "__main__":
    r1 = Rectangulo(4, 5)
    print(r1)
    print("Área:", r1.calcular_area())          # 20
    print("Perímetro:", r1.calcular_perimetro()) # 18
    print("¿Es cuadrado?", r1.es_cuadrado())     # False

    unittest.main(argv=[''], exit=False)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 3 [INTERMEDIO]: TAD Fraccion con Sobrecarga de Operadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un TAD Fraccion con numerador y denominador. Sobrecargar los 
operadores +, -, *, / para operar entre fracciones. Incluir método para 
simplificar la fracción.

🔹 PSEUDOCÓDIGO:
   TAD Fraccion
      - Atributos: numerador, denominador (enteros)
      - Invariante: denominador ≠ 0
      - Operaciones:
         * crear(num, den) → Fraccion
         * sumar(otraFraccion) → Fraccion
         * restar(otraFraccion) → Fraccion
         * multiplicar(otraFraccion) → Fraccion
         * dividir(otraFraccion) → Fraccion
         * simplificar() → Fraccion

✅ EJEMPLO RESUELTO:

```python
from math import gcd

class Fraccion:
    """TAD que representa una fracción matemática"""
    
    def __init__(self, numerador: int, denominador: int):
        """
        Crea una fracción num/den
        Precondición: denominador != 0
        """
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self._numerador = numerador
        self._denominador = denominador
        self._simplificar()
    
    def _simplificar(self):
        """Simplifica la fracción usando el MCD"""
        mcd = gcd(abs(self._numerador), abs(self._denominador))
        self._numerador //= mcd
        self._denominador //= mcd
        # Mantener el signo en el numerador
        if self._denominador < 0:
            self._numerador = -self._numerador
            self._denominador = -self._denominador
    
    def __add__(self, otra: 'Fraccion') -> 'Fraccion':
        """Suma dos fracciones: a/b + c/d = (a*d + b*c)/(b*d)"""
        num = self._numerador * otra._denominador + self._denominador * otra._numerador
        den = self._denominador * otra._denominador
        return Fraccion(num, den)
    
    def __sub__(self, otra: 'Fraccion') -> 'Fraccion':
        """Resta dos fracciones"""
        num = self._numerador * otra._denominador - self._denominador * otra._numerador
        den = self._denominador * otra._denominador
        return Fraccion(num, den)
    
    def __mul__(self, otra: 'Fraccion') -> 'Fraccion':
        """Multiplica dos fracciones: (a/b) * (c/d) = (a*c)/(b*d)"""
        return Fraccion(self._numerador * otra._numerador, 
                       self._denominador * otra._denominador)
    
    def __truediv__(self, otra: 'Fraccion') -> 'Fraccion':
        """Divide dos fracciones: (a/b) / (c/d) = (a*d)/(b*c)"""
        return Fraccion(self._numerador * otra._denominador, 
                       self._denominador * otra._numerador)
    
    def __str__(self):
        return f"{self._numerador}/{self._denominador}"

# Ejemplo de uso:
f1 = Fraccion(1, 2)
f2 = Fraccion(1, 3)

print(f"{f1} + {f2} = {f1 + f2}")  # 1/2 + 1/3 = 5/6
print(f"{f1} * {f2} = {f1 * f2}")  # 1/2 * 1/3 = 1/6
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 4 [INTERMEDIO]: TAD CuentaBancaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un TAD CuentaBancaria con número de cuenta, titular y saldo.
Incluir operaciones para depositar, retirar y consultar saldo. Validar que
no se pueda retirar más del saldo disponible.

🔹 PSEUDOCÓDIGO:
   TAD CuentaBancaria
      - Atributos: numeroCuenta, titular, saldo
      - Invariante: saldo >= 0
      - Operaciones:
         * crear(numero, titular, saldoInicial) → CuentaBancaria
         * depositar(monto) → void
         * retirar(monto) → booleano
         * consultarSaldo() → real
         * obtenerTitular() → cadena

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 5 [INTERMEDIO]: TAD Conjunto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Crear un TAD Conjunto que represente un conjunto matemático (sin elementos
duplicados). Implementar operaciones de unión, intersección y diferencia.

🔹 PSEUDOCÓDIGO:
   TAD Conjunto
      - Atributos: elementos (colección sin duplicados)
      - Operaciones:
         * crear() → Conjunto
         * agregar(elemento) → void
         * eliminar(elemento) → booleano
         * contiene(elemento) → booleano
         * tamaño() → entero
         * union(otroConjunto) → Conjunto
         * interseccion(otroConjunto) → Conjunto
         * diferencia(otroConjunto) → Conjunto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 6 [INTERMEDIO]: TAD Fecha
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un TAD Fecha con día, mes y año. Validar que la fecha sea válida
(considerar años bisiestos). Implementar operación para calcular días entre
dos fechas y verificar si una fecha es anterior a otra.

🔹 PSEUDOCÓDIGO:
   TAD Fecha
      - Atributos: dia, mes, año (enteros)
      - Invariante: fecha válida según calendario gregoriano
      - Operaciones:
         * crear(dia, mes, año) → Fecha
         * esValida() → booleano
         * esBisiesto() → booleano
         * esAnterior(otraFecha) → booleano
         * diasEntre(otraFecha) → entero


===============================================================================
SECCIÓN 2: ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA
Grupo 3 - Ejercicios 7 al 13
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 7 [BÁSICO]: Análisis de Búsqueda Lineal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal y espacial del siguiente algoritmo de
búsqueda lineal. Determinar el mejor caso, caso promedio y peor caso.

🔹 PSEUDOCÓDIGO:
   Función busquedaLineal(lista, elemento):
       Para i desde 0 hasta longitud(lista) - 1:
           Si lista[i] == elemento:
               Retornar i
       Retornar -1

✅ EJEMPLO RESUELTO:

```python
import unittest

def busqueda_lineal(lista, elemento):
    """
    Realiza una búsqueda lineal (secuencial) de un elemento dentro de una lista.

    Args:
        lista (list): Lista de elementos donde se buscará.
        elemento (any): Elemento que se desea encontrar.

    Returns:
        int: El índice donde se encuentra el elemento, o -1 si no está presente.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# ANÁLISIS DE COMPLEJIDAD:

"""
COMPLEJIDAD TEMPORAL:
- Mejor caso: O(1) - El elemento está en la primera posición
- Caso promedio: O(n/2) = O(n) - El elemento está en alguna posición intermedia
- Peor caso: O(n) - El elemento no está o está en la última posición

EXPLICACIÓN:
En el peor caso, debemos recorrer todos los n elementos de la lista.
Cada iteración realiza una comparación (operación constante O(1)).
Por lo tanto, n iteraciones × O(1) = O(n)

COMPLEJIDAD ESPACIAL:
O(1) - Solo usamos variables auxiliares (i) independientes del tamaño de entrada

JUSTIFICACIÓN MATEMÁTICA:
Sea n = longitud(lista)
T(n) = 1 + 1 + 1 + ... + 1 (n veces) = n
Por lo tanto, T(n) = O(n)
"""

# Ejemplo de medición:
import time

lista_grande = list(range(100000))

# Mejor caso:
inicio = time.time()
busqueda_lineal(lista_grande, 0)
print(f"Mejor caso: {time.time() - inicio:.6f} segundos")

# Peor caso:
inicio = time.time()
busqueda_lineal(lista_grande, 99999)
print(f"Peor caso: {time.time() - inicio:.6f} segundos")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 8 [BÁSICO]: Análisis de Suma de Elementos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad del siguiente algoritmo que suma todos los elementos
de una lista.

🔹 PSEUDOCÓDIGO:
   Función sumaElementos(lista):
       suma ← 0
       Para cada elemento en lista:
           suma ← suma + elemento
       Retornar suma

"python"
import unittest

def suma_elementos(lista):
    """
    Calcula la suma de todos los elementos de una lista.

    Precondición:
        - La lista contiene solo números (enteros o flotantes).

    Postcondición:
        - Retorna la suma total de los elementos de la lista.
    """
    suma = 0
    for x in lista:
        suma += x
    return suma

Análisis de Complejidad del Algoritmo suma_elementos

Descripción general:
El algoritmo recorre la lista sumando cada valor en una variable acumuladora (suma).

Análisis temporal:

En cada iteración se realiza una suma simple.

Si la lista tiene n elementos, se realizan n sumas.
➡ Complejidad temporal: O(n)

Análisis espacial:

Solo se usa una variable adicional (suma), independientemente del tamaño de la lista.
➡ Complejidad espacial: O(1)

# ============================================================
# 🧪 PRUEBAS UNITARIAS
# ============================================================

class TestSumaElementos(unittest.TestCase):

    def test_lista_normal(self):
        self.assertEqual(suma_elementos([1, 2, 3, 4]), 10)

    def test_lista_vacia(self):
        self.assertEqual(suma_elementos([]), 0)

    def test_lista_negativos(self):
        self.assertEqual(suma_elementos([-1, -2, -3]), -6)

    def test_lista_flotantes(self):
        self.assertAlmostEqual(suma_elementos([1.5, 2.5, 3.0]), 7.0)


# ============================================================
# 💡 EJEMPLO DE USO
# ============================================================

if __name__ == "__main__":
    numeros = [5, 10, 15, 20]
    print(f"Lista: {numeros}")
    print(f"Suma total: {suma_elementos(numeros)}")

    # Ejecutar pruebas unitarias
    unittest.main(argv=[''], exit=False)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 9 [BÁSICO]: Comparar Complejidades
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Ordenar las siguientes complejidades de menor a mayor eficiencia:
O(n²), O(1), O(log n), O(n log n), O(2ⁿ), O(n), O(n³)

Además, indicar cuál sería preferible para un dataset de 1 millón de elementos.

🔹 PSEUDOCÓDIGO:
   Función ordenar_complejidades(lista):
       Ordenar lista por tasa de crecimiento(menor a mayor)
       Retorna lista_ordenada
   Funcion recomendacion_para(n)
           Si se va a procesar 1_000_000 elementos:
              Retoirnar "usar 0(n), 0(n log n) o mejores: evitar 0(n2) y peor "

'''python

def buscar_duplicados(lista):
    """
    Determina si existen elementos duplicados en una lista.

    Parámetros:
    -----------
    lista : list
        Lista de elementos a analizar.

    Retorna:
    --------
    bool
        True si hay elementos duplicados, False en caso contrario.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


# --- Casos de prueba ---
def pruebas_buscar_duplicados():
    """
    Pruebas unitarias básicas para la función buscar_duplicados.
    """
    assert buscar_duplicados([1, 2, 3, 4]) == False
    assert buscar_duplicados([1, 2, 3, 1]) == True
    assert buscar_duplicados([]) == False
    assert buscar_duplicados(['a', 'b', 'c', 'a']) == True
    assert buscar_duplicados([10]) == False
    print("✅ Todas las pruebas pasaron correctamente.")


# Ejecutar pruebas
if __name__ == "__main__":
    pruebas_buscar_duplicados()
'''


# ANÁLISIS DE COMPLEJIDAD:

Complejidad temporal (T(n)):

En el peor de los casos, la función compara cada elemento con todos los demás.

Esto produce un comportamiento cuadrático: T(n)=O(n2)

En el mejor de los casos (si encuentra duplicado temprano), la función puede terminar antes → O(1).

Complejidad espacial (S(n)):

No utiliza estructuras auxiliares adicionales, solo variables de control.

Por tanto:S(n)=O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 10 [INTERMEDIO]: Análisis de Bucles Anidados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal del siguiente código con bucles anidados:

🔹 PSEUDOCÓDIGO:
   Función buscarDuplicados(lista):
       Para i desde 0 hasta longitud(lista) - 1:
           Para j desde i + 1 hasta longitud(lista) - 1:
               Si lista[i] == lista[j]:
                   Retornar Verdadero
       Retornar Falso

✅ EJEMPLO RESUELTO:

```python
def buscar_duplicados(lista):
    """
    Busca elementos duplicados en una lista
    """
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False

# ANÁLISIS DE COMPLEJIDAD:

"""
COMPLEJIDAD TEMPORAL:

Análisis del bucle externo:
- Se ejecuta n veces (donde n = len(lista))

Análisis del bucle interno:
- Primera iteración (i=0): se ejecuta n-1 veces
- Segunda iteración (i=1): se ejecuta n-2 veces
- Tercera iteración (i=2): se ejecuta n-3 veces
- ...
- Última iteración (i=n-2): se ejecuta 1 vez

Total de comparaciones:
(n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2

Aplicando notación Big O:
T(n) = n(n-1)/2 = (n² - n)/2
T(n) = O(n²)

MEJOR CASO: O(1) - Si encuentra duplicados en las primeras posiciones
PEOR CASO: O(n²) - Si no hay duplicados o están al final

COMPLEJIDAD ESPACIAL:
O(1) - Solo usa variables i, j independientes del tamaño de entrada
"""

# Comparación con solución más eficiente:
def buscar_duplicados_optimizado(lista):
    """Versión O(n) usando conjunto"""
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return True
        vistos.add(elemento)
    return False

# Esta versión es O(n) temporal pero O(n) espacial
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 11 [INTERMEDIO]: Búsqueda Binaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad del algoritmo de búsqueda binaria. Explicar por qué
es O(log n) y en qué casos es más eficiente que la búsqueda lineal.

🔹 PSEUDOCÓDIGO:
   Función busquedaBinaria(listaOrdenada, elemento):
       izq ← 0
       der ← longitud(listaOrdenada) - 1
       
       Mientras izq <= der:
           medio ← (izq + der) / 2
           Si listaOrdenada[medio] == elemento:
               Retornar medio
           SiNo Si listaOrdenada[medio] < elemento:
               izq ← medio + 1
           SiNo:
               der ← medio - 1
       
       Retornar -1
'''python
import unittest

def busqueda_binaria(arreglo, elemento):
    """
    Realiza una búsqueda binaria para encontrar un elemento dentro de una lista ordenada.

    Parámetros:
    -----------
    arreglo : list
        Lista ordenada de elementos.
    elemento : any
        Elemento a buscar dentro de la lista.

    Retorna:
    --------
    int
        Índice del elemento si se encuentra en la lista; -1 en caso contrario.
    """
    izquierda, derecha = 0, len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arreglo[medio] == elemento:
            return medio
        if arreglo[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


class TestBusquedaBinaria(unittest.TestCase):
    """Casos de prueba para la función busqueda_binaria."""

    def test_elemento_presente(self):
        self.assertEqual(busqueda_binaria([1, 2, 3, 4, 5], 3), 2)

    def test_primero(self):
        self.assertEqual(busqueda_binaria([10, 20, 30, 40, 50], 10), 0)

    def test_elemento_inexistente(self):
        self.assertEqual(busqueda_binaria([10, 20, 30, 40, 50], 55), -1)

    def test_lista_vacia(self):
        self.assertEqual(busqueda_binaria([], 5), -1)

    def test_unico_elemento(self):
        self.assertEqual(busqueda_binaria([1], 1), 0)


if __name__ == "__main__":
    unittest.main()
'''

# ANÁLISIS DE COMPLEJIDAD:
Complejidad temporal (T(n))

Cada vez que el algoritmo compara el elemento buscado con el valor medio, descarta la mitad del arreglo.
Por tanto, el número de pasos crece logarítmicamente con el tamaño del arreglo.

Complejidad espacial (S(n))

La implementación iterativa solo usa unas pocas variables (izquierda, derecha, medio), por lo que su uso de memoria es constante:

S(n)=O(1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 12 [INTERMEDIO]: Complejidad con Estructuras de Datos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Comparar la complejidad de las siguientes operaciones en listas vs diccionarios
en Python:
- Buscar un elemento
- Insertar un elemento
- Eliminar un elemento

Indicar cuándo conviene usar cada estructura de datos.

#Codigo
import unittest
import timeit


def probar_busqueda_lista(lista, elemento):
    """Busca un elemento en una lista usando el operador 'in'."""
    return elemento in lista


def probar_busqueda_diccionario(diccionario, clave):
    """Busca una clave en un diccionario."""
    return clave in diccionario


def probar_insercion_lista(lista, elemento):
    """Inserta un elemento al final de una lista."""
    lista.append(elemento)
    return lista


def probar_insercion_diccionario(diccionario, clave, valor):
    """Inserta un par clave-valor en un diccionario."""
    diccionario[clave] = valor
    return diccionario


def probar_eliminacion_lista(lista, elemento):
    """Elimina un elemento de una lista si existe."""
    if elemento in lista:
        lista.remove(elemento)
    return lista


def probar_eliminacion_diccionario(diccionario, clave):
    """Elimina una clave de un diccionario si existe."""
    if clave in diccionario:
        del diccionario[clave]
    return diccionario


class TestComparacionEstructuras(unittest.TestCase):
    """Casos de prueba comparativos entre listas y diccionarios."""

    def setUp(self):
        self.lista = list(range(100000))  # Lista con 100 mil elementos
        self.diccionario = {i: None for i in range(100000)}
        self.elemento_existente = 99999
        self.elemento_nuevo = 100001

    def test_busqueda(self):
        """Comparación de búsqueda en lista vs diccionario."""
        tiempo_lista = timeit.timeit(lambda: probar_busqueda_lista(self.lista, self.elemento_existente), number=100)
        tiempo_dict = timeit.timeit(lambda: probar_busqueda_diccionario(self.diccionario, self.elemento_existente), number=100)
        print(f"\n🔍 Búsqueda - Lista: {tiempo_lista:.6f}s | Diccionario: {tiempo_dict:.6f}s")
        self.assertTrue(tiempo_dict < tiempo_lista)

    def test_insercion(self):
        """Comparación de inserción en lista vs diccionario."""
        tiempo_lista = timeit.timeit(lambda: probar_insercion_lista(self.lista.copy(), self.elemento_nuevo), number=100)
        tiempo_dict = timeit.timeit(lambda: probar_insercion_diccionario(self.diccionario.copy(), self.elemento_nuevo, None), number=100)
        print(f"➕ Inserción - Lista: {tiempo_lista:.6f}s | Diccionario: {tiempo_dict:.6f}s")
        self.assertTrue(tiempo_dict <= tiempo_lista)

    def test_eliminacion(self):
        """Comparación de eliminación en lista vs diccionario."""
        tiempo_lista = timeit.timeit(lambda: probar_eliminacion_lista(self.lista.copy(), self.elemento_existente), number=100)
        tiempo_dict = timeit.timeit(lambda: probar_eliminacion_diccionario(self.diccionario.copy(), self.elemento_existente), number=100)
        print(f"❌ Eliminación - Lista: {tiempo_lista:.6f}s | Diccionario: {tiempo_dict:.6f}s")
        self.assertTrue(tiempo_dict < tiempo_lista)


if __name__ == "__main__":
    unittest.main(verbosity=2)


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 13 [INTERMEDIO]: Análisis de Algoritmo Recursivo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal y espacial del algoritmo factorial recursivo.
Comparar con la versión iterativa.

🔹 PSEUDOCÓDIGO:
   Función factorialRecursivo(n):
       Si n <= 1:
           Retornar 1
       SiNo:
           Retornar n * factorialRecursivo(n - 1)


===============================================================================
SECCIÓN 3: PILAS (STACKS)
Grupo 4 - Ejercicios 14 al 25
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 14 [BÁSICO]: Implementación Básica de Pila
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar una clase Pila con las operaciones básicas: push (apilar),
pop (desapilar), peek (ver tope), isEmpty (verificar si está vacía) y
size (obtener tamaño).

🔹 PSEUDOCÓDIGO:
   TAD Pila:
       - Atributos: elementos (lista)
       
       Operaciones:
       * push(elemento) → void
           agregar elemento al tope
       
       * pop() → elemento
           Precondición: pila no vacía
           eliminar y retornar elemento del tope
       
       * peek() → elemento
           Precondición: pila no vacía
           retornar elemento del tope sin eliminarlo
       
       * isEmpty() → booleano
           retornar verdadero si pila vacía
       
       * size() → entero
           retornar cantidad de elementos

✅ EJEMPLO RESUELTO:

```python
class Pila:
    """Implementación de TAD Pila usando lista de Python"""
    
    def __init__(self):
        """Crea una pila vacía"""
        self._elementos = []
    
    def push(self, elemento):
        """
        Apila un elemento en el tope
        Postcondición: size aumenta en 1
        """
        self._elementos.append(elemento)
    
    def pop(self):
        """
        Desapila y retorna el elemento del tope
        Precondición: pila no vacía
        Postcondición: size disminuye en 1
        """
        if self.is_empty():
            raise IndexError("Pop desde pila vacía")
        return self._elementos.pop()
    
    def peek(self):
        """
        Retorna el elemento del tope sin eliminarlo
        Precondición: pila no vacía
        """
        if self.is_empty():
            raise IndexError("Peek en pila vacía")
        return self._elementos[-1]
    
    def is_empty(self) -> bool:
        """Retorna True si la pila está vacía"""
        return len(self._elementos) == 0
    
    def size(self) -> int:
        """Retorna la cantidad de elementos"""
        return len(self._elementos)
    
    def __str__(self):
        return f"Pila: {self._elementos} (tope: {self._elementos[-1] if not self.is_empty() else 'vacía'})"

# Ejemplo de uso:
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print(pila)  # Pila: [10, 20, 30] (tope: 30)
print(f"Tope: {pila.peek()}")  # 30
print(f"Desapilar: {pila.pop()}")  # 30
print(f"Tamaño: {pila.size()}")  # 2
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 15 [BÁSICO]: Invertir una Cadena
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Usar una pila para invertir una cadena de texto. Por ejemplo, "HOLA" debe
convertirse en "ALOH".

🔹 PSEUDOCÓDIGO:
   Función invertirCadena(texto):
       pila ← nueva Pila()
       
       Para cada caracter en texto:
           pila.push(caracter)
       
       resultado ← ""
       Mientras NO pila.isEmpty():
           resultado ← resultado + pila.pop()
       
       Retornar resultado

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 16 [BÁSICO]: Validar Paréntesis Balanceados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar una función que verifique si una expresión tiene los paréntesis
correctamente balanceados usando una pila.
Ejemplos:
- "(())" → Verdadero
- "(()" → Falso
- ")(" → Falso

🔹 PSEUDOCÓDIGO:
   Función validarParentesis(expresion):
       pila ← nueva Pila()
       
       Para cada caracter en expresion:
           Si caracter == '(':
               pila.push(caracter)
           SiNo Si caracter == ')':
               Si pila.isEmpty():
                   Retornar Falso
               pila.pop()
       
       Retornar pila.isEmpty()

✅ EJEMPLO RESUELTO:

```python
def validar_parentesis(expresion: str) -> bool:
    """
    Verifica si los paréntesis están balanceados
    
    Ejemplos:
    >>> validar_parentesis("(())")
    True
    >>> validar_parentesis("(()")
    False
    >>> validar_parentesis(")(")
    False
    """
    pila = []
    
    for caracter in expresion:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:  # Pila vacía
                return False
            pila.pop()
    
    return len(pila) == 0  # Verdadero si no quedan paréntesis sin cerrar

# Casos de prueba:
casos = [
    ("()", True),
    ("(())", True),
    ("(()())", True),
    ("(()", False),
    ("())", False),
    (")(", False),
    ("", True),
]

for expresion, esperado in casos:
    resultado = validar_parentesis(expresion)
    estado = "✓" if resultado == esperado else "✗"
    print(f"{estado} '{expresion}' → {resultado} (esperado: {esperado})")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 17 [INTERMEDIO]: Validar Múltiples Tipos de Delimitadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Extender el ejercicio anterior para validar paréntesis (), corchetes [] y
llaves {}. Los delimitadores deben cerrarse en el orden correcto.
Ejemplos:
- "{[()]}" → Verdadero
- "{[(])}" → Falso (orden incorrecto)
- "{[}" → Falso (falta cerrar)

🔹 PSEUDOCÓDIGO:
   Función validarDelimitadores(expresion):
       pila ← nueva Pila()
       aperturas ← {'(', '[', '{'}
       cierres ← {')', ']', '}'}
       pares ← {')': '(', ']': '[', '}': '{'}
       
       Para cada caracter en expresion:
           Si caracter está en aperturas:
               pila.push(caracter)
           SiNo Si caracter está en cierres:
               Si pila.isEmpty():
                   Retornar Falso
               Si pila.pop() != pares[caracter]:
                   Retornar Falso
       
       Retornar pila.isEmpty()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 18 [INTERMEDIO]: Evaluador de Expresiones Postfijas (RPN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un evaluador de expresiones en notación postfija (Reverse Polish
Notation). En RPN, los operadores van después de los operandos.
Ejemplo: "3 4 + 2 *" equivale a (3 + 4) * 2 = 14

🔹 PSEUDOCÓDIGO:
   Función evaluarPostfija(expresion):
       pila ← nueva Pila()
       tokens ← dividir expresion por espacios
       
       Para cada token en tokens:
           Si token es número:
               pila.push(convertir token a número)
           SiNo:  // token es operador
               operando2 ← pila.pop()
               operando1 ← pila.pop()
               resultado ← aplicar operador(operando1, operando2, token)
               pila.push(resultado)
       
       Retornar pila.pop()

✅ EJEMPLO RESUELTO:

```python
def evaluar_postfija(expresion: str) -> float:
    """
    Evalúa una expresión en notación postfija (RPN)
    
    Ejemplos:
    >>> evaluar_postfija("3 4 +")
    7.0
    >>> evaluar_postfija("3 4 + 2 *")
    14.0
    >>> evaluar_postfija("15 7 1 1 + - / 3 * 2 1 1 + + -")
    5.0
    """
    pila = []
    tokens = expresion.split()
    
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    
    for token in tokens:
        if token in operadores:
            # Desapilar dos operandos (orden importa)
            operando2 = pila.pop()
            operando1 = pila.pop()
            # Aplicar operación y apilar resultado
            resultado = operadores[token](operando1, operando2)
            pila.append(resultado)
        else:
            # Es un número, apilar
            pila.append(float(token))
    
    # El resultado final está en la cima
    return pila.pop()

# Ejemplos de uso:
expresiones = [
    ("3 4 +", 7.0),
    ("3 4 + 2 *", 14.0),
    ("5 1 2 + 4 * + 3 -", 14.0),
]

for expr, esperado in expresiones:
    resultado = evaluar_postfija(expr)
    print(f"'{expr}' = {resultado} (esperado: {esperado})")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 19 [INTERMEDIO]: Convertir Infija a Postfija
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar el algoritmo Shunting Yard para convertir expresiones infijas
(notación normal) a postfijas. Considerar precedencia de operadores y paréntesis.
Ejemplo: "3 + 4 * 2" → "3 4 2 * +"

🔹 PSEUDOCÓDIGO:
   Función infijaAPostfija(expresion):
       salida ← lista vacía
       pila ← nueva Pila()
       precedencia ← {'+': 1, '-': 1, '*': 2, '/': 2}
       
       tokens ← tokenizar(expresion)
       
       Para cada token en tokens:
           Si token es número:
               agregar token a salida
           SiNo Si token es '(':
               pila.push(token)
           SiNo Si token es ')':
               Mientras pila.peek() != '(':
                   agregar pila.pop() a salida
               pila.pop()  // eliminar '('
           SiNo:  // token es operador
               Mientras NO pila.isEmpty() Y 
                        pila.peek() != '(' Y
                        precedencia[pila.peek()] >= precedencia[token]:
                   agregar pila.pop() a salida
               pila.push(token)
       
       Mientras NO pila.isEmpty():
           agregar pila.pop() a salida
       
       Retornar unir salida con espacios

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 20 [INTERMEDIO]: Historial de Navegación
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un sistema de historial de navegación web usando dos pilas:
una para "atrás" y otra para "adelante". Implementar las funciones:
- visitar(url): visitar nueva página
- atras(): volver a la página anterior
- adelante(): ir a la página siguiente

🔹 PSEUDOCÓDIGO:
   Clase Navegador:
       Atributos:
           pilaAtras ← nueva Pila()
           pilaAdelante ← nueva Pila()
           paginaActual ← null
       
       Función visitar(url):
           Si paginaActual != null:
               pilaAtras.push(paginaActual)
           paginaActual ← url
           limpiar pilaAdelante
       
       Función atras():
           Si pilaAtras.isEmpty():
               error "No hay páginas anteriores"
           pilaAdelante.push(paginaActual)
           paginaActual ← pilaAtras.pop()
       
       Función adelante():
           Si pilaAdelante.isEmpty():
               error "No hay páginas siguientes"
           pilaAtras.push(paginaActual)
           paginaActual ← pilaAdelante.pop()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 21 [INTERMEDIO]: Verificar Palíndromos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Usar una pila para verificar si una palabra es un palíndromo (se lee igual
de izquierda a derecha que de derecha a izquierda). Ignorar espacios y
mayúsculas/minúsculas.
Ejemplos: "anilina", "radar", "reconocer"

🔹 PSEUDOCÓDIGO:
   Función esPalindromo(texto):
       pila ← nueva Pila()
       textoLimpio ← eliminar espacios y convertir a minúsculas
       
       // Apilar primera mitad
       Para i desde 0 hasta longitud(textoLimpio)/2 - 1:
           pila.push(textoLimpio[i])
       
       // Comparar segunda mitad
       inicio ← Si longitud(textoLimpio) es impar entonces longitud/2 + 1 
                SiNo longitud/2
       
       Para i desde inicio hasta fin:
           Si pila.isEmpty() O textoLimpio[i] != pila.pop():
               Retornar Falso
       
       Retornar Verdadero

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 22 [INTERMEDIO]: Sistema Deshacer/Rehacer (Undo/Redo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar un editor de texto simple con funcionalidad de deshacer y rehacer
usando dos pilas. Debe soportar:
- escribir(texto): agregar texto
- deshacer(): deshacer última acción
- rehacer(): rehacer acción deshecha

🔹 PSEUDOCÓDIGO:
   Clase EditorTexto:
       Atributos:
           contenido ← ""
           pilaDeshacer ← nueva Pila()
           pilaRehacer ← nueva Pila()
       
       Función escribir(texto):
           pilaDeshacer.push(contenido)
           contenido ← contenido + texto
           limpiar pilaRehacer
       
       Función deshacer():
           Si pilaDeshacer.isEmpty():
               retornar
           pilaRehacer.push(contenido)
           contenido ← pilaDeshacer.pop()
       
       Función rehacer():
           Si pilaRehacer.isEmpty():
               retornar
           pilaDeshacer.push(contenido)
           contenido ← pilaRehacer.pop()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 23 [INTERMEDIO]: Torre de Hanoi
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Implementar el juego de la Torre de Hanoi usando pilas. El problema consiste
en mover n discos de una torre origen a una torre destino usando una torre
auxiliar, con las reglas:
- Solo se puede mover un disco a la vez
- Un disco más grande no puede estar sobre uno más pequeño

🔹 PSEUDOCÓDIGO:
   Función hanoi(n, origen, destino, auxiliar):
       Si n == 1:
           mover disco de origen a destino
           retornar
       
       hanoi(n-1, origen, auxiliar, destino)
       mover disco de origen a destino
       hanoi(n-1, auxiliar, destino, origen)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 24 [INTERMEDIO]: Validar Sintaxis HTML Simplificada
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Usar una pila para verificar si las etiquetas HTML están correctamente
balanceadas y anidadas. Considerar solo etiquetas de apertura <tag> y
cierre </tag>.
Ejemplo válido: "<html><body><h1>Título</h1></body></html>"
Ejemplo inválido: "<html><body></html></body>"

🔹 PSEUDOCÓDIGO:
   Función validarHTML(codigo):
       pila ← nueva Pila()
       etiquetas ← extraer todas las etiquetas del código
       
       Para cada etiqueta en etiquetas:
           Si etiqueta es de apertura:
               pila.push(nombre de etiqueta)
           SiNo:  // etiqueta de cierre
               Si pila.isEmpty():
                   Retornar Falso
               Si pila.pop() != nombre de etiqueta:
                   Retornar Falso
       
       Retornar pila.isEmpty()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 25 [INTERMEDIO]: Pila con Mínimo en O(1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Diseñar una pila que además de las operaciones normales (push, pop, peek),
pueda retornar el elemento mínimo en tiempo constante O(1). Implementar:
- push(elemento)
- pop()
- peek()
- getMin() → retorna el mínimo actual en O(1)

🔹 PSEUDOCÓDIGO:
   Clase PilaMinimo:
       Atributos:
           pilaElementos ← nueva Pila()
           pilaMinimos ← nueva Pila()
       
       Función push(elemento):
           pilaElementos.push(elemento)
           
           Si pilaMinimos.isEmpty() O elemento <= pilaMinimos.peek():
               pilaMinimos.push(elemento)
       
       Función pop():
           Si pilaElementos.isEmpty():
               error
           
           elemento ← pilaElementos.pop()
           Si elemento == pilaMinimos.peek():
               pilaMinimos.pop()
           
           Retornar elemento
       
       Función getMin():
           Si pilaMinimos.isEmpty():
               error
           Retornar pilaMinimos.peek()

✅ EJEMPLO RESUELTO:

```python
class PilaMinimo:
    """
    Pila que mantiene el mínimo en tiempo O(1)
    Usa dos pilas: una para elementos y otra para mínimos
    """
    
    def __init__(self):
        self._elementos = []
        self._minimos = []
    
    def push(self, elemento):
        """Apila elemento y actualiza mínimo si es necesario"""
        self._elementos.append(elemento)
        
        # Si es el primer elemento o es menor/igual al mínimo actual
        if not self._minimos or elemento <= self._minimos[-1]:
            self._minimos.append(elemento)
    
    def pop(self):
        """Desapila elemento y actualiza mínimo si es necesario"""
        if not self._elementos:
            raise IndexError("Pop desde pila vacía")
        
        elemento = self._elementos.pop()
        
        # Si el elemento desapilado era el mínimo, también lo quitamos
        if elemento == self._minimos[-1]:
            self._minimos.pop()
        
        return elemento
    
    def peek(self):
        """Retorna el tope sin desapilar"""
        if not self._elementos:
            raise IndexError("Peek en pila vacía")
        return self._elementos[-1]
    
    def get_min(self):
        """Retorna el mínimo actual en O(1)"""
        if not self._minimos:
            raise IndexError("Pila vacía")
        return self._minimos[-1]
    
    def is_empty(self):
        return len(self._elementos) == 0

# Demostración:
pila = PilaMinimo()
operaciones = [
    ('push', 5),
    ('push', 3),
    ('push', 7),
    ('push', 1),
    ('push', 4),
]

print("Operación\tPila\t\tMínimo")
print("-" * 40)

for op, valor in operaciones:
    pila.push(valor)
    print(f"push({valor})\t\t{pila._elementos}\t{pila.get_min()}")

print("\nDesapilando...")
while not pila.is_empty():
    elemento = pila.pop()
    minimo = pila.get_min() if not pila.is_empty() else "N/A"
    print(f"pop() → {elemento}\t{pila._elementos}\t{minimo}")

"""
ANÁLISIS DE COMPLEJIDAD:
- push(): O(1) - solo apila en ambas pilas
- pop(): O(1) - solo desapila de una o ambas pilas
- get_min(): O(1) - solo consulta el tope de pilaMinimos
- Complejidad espacial: O(n) en peor caso si todos los elementos son mínimos decrecientes
"""
```


===============================================================================
FIN DE LOS 25 EJERCICIOS
===============================================================================

📌 NOTAS IMPORTANTES:

1. Los ejercicios están ordenados por dificultad dentro de cada sección
2. Se recomienda resolver los ejercicios en orden
3. Los ejercicios marcados como RESUELTOS incluyen código completo
4. Para los demás ejercicios, seguir el pseudocódigo proporcionado
5. Practicar el análisis de complejidad en todos los algoritmos

💡 RECOMENDACIONES:

- Implementar todos los ejercicios en Python
- Agregar casos de prueba (unit tests)
- Documentar el código con docstrings
- Analizar la complejidad de cada solución
- Comparar diferentes enfoques cuando sea posible

===============================================================================
