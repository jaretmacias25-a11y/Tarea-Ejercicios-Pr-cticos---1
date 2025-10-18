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

#codigo
def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de un número usando recursividad.
    Parámetros:
        n (int): número entero no negativo
    Retorna:
        int: factorial de n
    """
    if n <= 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Prueba
import unittest

class TestFactorialRecursivo(unittest.TestCase):

    def test_factorial_cero(self):
        self.assertEqual(factorial_recursivo(0), 1)

    def test_factorial_uno(self):
        self.assertEqual(factorial_recursivo(1), 1)

    def test_factorial_positivo(self):
        self.assertEqual(factorial_recursivo(5), 120)

    def test_factorial_numero_mayor(self):
        self.assertEqual(factorial_recursivo(7), 5040)

    def test_factorial_tipo_invalido(self):
        with self.assertRaises(TypeError):
            factorial_recursivo("texto")

if __name__ == '__main__':
    unittest.main()
    
# ANALISIS DE COMPLEJIDAD
Complejidad temporal:

En cada llamada recursiva se reduce el problema en 1 unidad (n - 1).

Por lo tanto, hay n llamadas recursivas.

Cada llamada realiza una multiplicación constante.
  Complejidad temporal: O(n)

  Complejidad espacial:

Debido a la recursión, se crean n marcos de pila (stack frames) hasta llegar al caso base.
   Complejidad espacial: O(n)
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
       
# Codigo
class Pila:
    """Implementa una pila simple usando una lista."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("No se puede hacer pop en una pila vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")


class InversorCadena:
    """Usa una pila para invertir una cadena de texto."""

    def __init__(self, texto: str):
        self.texto = texto

    def invertir(self) -> str:
        pila = Pila()
        # Apilar cada carácter
        for caracter in self.texto:
            pila.push(caracter)

        # Desapilar para formar la cadena invertida
        resultado = ""
        while not pila.is_empty():
            resultado += pila.pop()

        return resultado
# Prueba Unnitest
# --- Pruebas unitarias ---
def test_inversor_cadena():
    """Pruebas unitarias para la clase InversorCadena."""
    assert InversorCadena("hola").invertir() == "aloh", "Error: caso 1"
    assert InversorCadena("Python").invertir() == "nohtyP", "Error: caso 2"
    assert InversorCadena("").invertir() == "", "Error: caso 3"
    print("✅ Todos los tests pasaron correctamente.")


# --- Ejecución principal ---
if __name__ == "__main__":
    texto = "Estructuras de Datos"
    inversor = InversorCadena(texto)
    print("Texto original :", texto)
    print("Texto invertido:", inversor.invertir())
    test_inversor_cadena()

Análisis de Complejidad (fuera del programa)
1. Complejidad Temporal:
El recorrido de la cadena tiene complejidad O(n), donde n es la longitud del texto.
El desapilado también recorre todos los caracteres, por lo que en total sigue siendo O(n).
2. Complejidad Espacial:
La pila almacena n caracteres del texto → O(n).
La cadena resultado también tiene n caracteres → O(n).
En conjunto, el algoritmo usa O(n) espacio adicional.
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

#Codigo
class Pila:
    """Implementa una pila simple usando una lista."""

    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def push(self, elemento):
        """
        Agrega un elemento a la pila.

        Parámetros:
            elemento: valor que se agregará a la pila.
        """
        self.items.append(elemento)

    def pop(self):
        """
        Elimina y retorna el elemento superior de la pila.

        Retorna:
            El elemento que estaba en la parte superior, o None si la pila está vacía.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self) -> bool:
        """
        Verifica si la pila está vacía.

        Retorna:
            bool: True si está vacía, False en caso contrario.
        """
        return len(self.items) == 0


class ValidadorDelimitadores:
    """Valida si los delimitadores en una expresión están balanceados."""

    def __init__(self):
        """Inicializa los conjuntos de delimitadores de apertura y cierre."""
        self.aperturas = {'(', '[', '{'}
        self.cierres = {')', ']', '}'}
        self.pares = {')': '(', ']': '[', '}': '{'}

    def validar(self, expresion: str) -> bool:
        """
        Verifica si los delimitadores de la expresión están correctamente balanceados.

        Parámetros:
            expresion (str): La cadena que contiene delimitadores.

        Retorna:
            bool: True si los delimitadores están balanceados, False en caso contrario.

        Ejemplo:
            >>> validar("{[()]}")
            True
        """
        pila = Pila()

        for caracter in expresion:
            if caracter in self.aperturas:
                pila.push(caracter)
            elif caracter in self.cierres:
                if pila.is_empty():
                    return False
                if pila.pop() != self.pares[caracter]:
                    return False

        return pila.is_empty()

# --- Pruebas unitarias ---
def test_validador_delimitadores():
    """Pruebas unitarias para la clase ValidadorDelimitadores."""
    validador = ValidadorDelimitadores()
    assert validador.validar("{[()]}") is True, "Error: caso 1"
    assert validador.validar("{[(])}") is False, "Error: caso 2"
    assert validador.validar("{[}") is False, "Error: caso 3"
    assert validador.validar("((()))") is True, "Error: caso 4"
    assert validador.validar("") is True, "Error: caso 5"
    print("✅ Todos los tests pasaron correctamente.")


# --- Ejecución principal ---
if __name__ == "__main__":
    validador = ValidadorDelimitadores()
    expresion = "{[()]}"

    print("Expresión:", expresion)
    print("¿Está balanceada?:", validador.validar(expresion))
    test_validador_delimitadores()

# Análisis de Complejidad (fuera del programa)
1. Complejidad Temporal:
El algoritmo recorre cada carácter de la expresión una sola vez → O(n), donde n es la longitud de la cadena.
Cada operación push y pop en la pila tiene costo O(1).
👉 Por tanto, la complejidad total es O(n).
2. Complejidad Espacial:
En el peor de los casos, la pila almacena todos los caracteres de apertura → O(n) espacio adicional.
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
#Codigo
import re

def infija_a_postfija(expresion: str) -> str:
    """
    Convierte una expresión matemática en notación infija a notación postfija.

    Parámetros:
        expresion (str): Expresión matemática (por ejemplo: "3 + 4 * 2 / ( 1 - 5 )").

    Retorna:
        str: Expresión equivalente en notación postfija.

    Ejemplo:
        >>> infija_a_postfija("3 + 4 * 2 / ( 1 - 5 )")
        '3 4 2 * 1 5 - / +'
    """
    salida = []
    pila = []
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Dividir la expresión en tokens (números y operadores)
    tokens = re.findall(r'\d+|[+\-*/()]', expresion)

    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            # Desapilar hasta encontrar '('
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar '('
        else:
            # Operadores: aplicar precedencia
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia[token]:
                salida.append(pila.pop())
            pila.append(token)

    # Vaciar la pila restante
    while pila:
        salida.append(pila.pop())

    return ' '.join(salida)


# --- Pruebas unitarias ---
def test_infija_a_postfija():
    """Pruebas unitarias para la función infija_a_postfija."""
    assert infija_a_postfija("3 + 4") == "3 4 +", "Error: caso 1"
    assert infija_a_postfija("3 + 4 * 2") == "3 4 2 * +", "Error: caso 2"
    assert infija_a_postfija("( 1 + 2 ) * 3") == "1 2 + 3 *", "Error: caso 3"
    assert infija_a_postfija("3 + 4 * 2 / ( 1 - 5 )") == "3 4 2 * 1 5 - / +", "Error: caso 4"
    print("✅ Todos los tests pasaron correctamente.")


# --- Ejecución principal ---
if __name__ == "__main__":
    expresion = "3 + 4 * 2 / ( 1 - 5 )"
    print("Expresión infija  :", expresion)
    print("Expresión postfija:", infija_a_postfija(expresion))
    test_infija_a_postfija()

#Análisis de Complejidad (fuera del programa)
1. Complejidad Temporal:
Se recorre cada token una sola vez: O(n).
Las operaciones de pila (push, pop) son O(1) cada una.
👉 En total, el algoritmo tiene complejidad O(n).
2. Complejidad Espacial:
La pila y la lista de salida pueden almacenar hasta n elementos en el peor caso → O(n).

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
#Codigo
class Navegador:
    """Simula la navegación entre páginas web mediante dos pilas."""

    def __init__(self):
        """Inicializa las pilas y la página actual."""
        self.pilaAtras = []
        self.pilaAdelante = []
        self.paginaActual = None

    def visitar(self, url: str) -> None:
        """
        Visita una nueva página y actualiza las pilas de navegación.

        Parámetros:
            url (str): La dirección de la nueva página web.
        """
        if self.paginaActual is not None:
            self.pilaAtras.append(self.paginaActual)
        self.paginaActual = url
        self.pilaAdelante.clear()
        print(f"Visiting: {self.paginaActual}")

    def atras(self) -> None:
        """
        Regresa a la página anterior en la pila de navegación.
        """
        if not self.pilaAtras:
            print("⚠️ No hay páginas anteriores.")
            return
        self.pilaAdelante.append(self.paginaActual)
        self.paginaActual = self.pilaAtras.pop()
        print(f"Volviendo a: {self.paginaActual}")

    def adelante(self) -> None:
        """
        Avanza a la siguiente página en la pila de navegación.
        """
        if not self.pilaAdelante:
            print("⚠️ No hay páginas siguientes.")
            return
        self.pilaAtras.append(self.paginaActual)
        self.paginaActual = self.pilaAdelante.pop()
        print(f"Avanzando a: {self.paginaActual}")


# --- Pruebas unitarias ---
def test_navegador():
    """Pruebas unitarias para la clase Navegador."""
    nav = Navegador()

    nav.visitar("google.com")
    nav.visitar("youtube.com")
    nav.visitar("github.com")
    assert nav.paginaActual == "github.com"

    nav.atras()  # Debería volver a youtube
    assert nav.paginaActual == "youtube.com"

    nav.atras()  # Debería volver a google
    assert nav.paginaActual == "google.com"

    nav.adelante()  # Avanza a youtube
    assert nav.paginaActual == "youtube.com"

    nav.visitar("openai.com")  # Nueva visita borra el historial hacia adelante
    assert nav.paginaActual == "openai.com"
    assert not nav.pilaAdelante  # pilaAdelante vacía

    print("✅ Todos los tests pasaron correctamente.")


# --- Ejecución principal ---
if __name__ == "__main__":
    navegador = Navegador()
    navegador.visitar("google.com")
    navegador.visitar("youtube.com")
    navegador.visitar("github.com")

    navegador.atras()
    navegador.atras()
    navegador.adelante()
    navegador.visitar("openai.com")

    test_navegador()

#Análisis de Complejidad (fuera del programa)
1. Complejidad Temporal:
Cada operación (visitar, atras, adelante) realiza un número constante de operaciones append y pop.
👉 Complejidad temporal: O(1) por operación.
2. Complejidad Espacial:
Las pilas pueden crecer hasta n, donde n es el número total de páginas visitadas.
👉 Complejidad espacial: O(n).
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

#Codigo
"""
def es_palindromo(texto: str) -> bool:
    """
    Determina si un texto es un palíndromo utilizando una pila.

    Parámetros:
        texto (str): Cadena de texto a evaluar.

    Retorna:
        bool: True si el texto es palíndromo, False en caso contrario.
    """
    pila = []

    # Normaliza el texto (minúsculas y sin espacios)
    texto_limpio = ''.join(texto.lower().split())

    longitud = len(texto_limpio)
    mitad = longitud // 2

    # Agrega la primera mitad de los caracteres a la pila
    for i in range(mitad):
        pila.append(texto_limpio[i])

    # Si la longitud es impar, salta el carácter del medio
    inicio = mitad if longitud % 2 == 0 else mitad + 1

    # Compara los caracteres de la segunda mitad con los de la pila
    for i in range(inicio, longitud):
        if not pila or texto_limpio[i] != pila.pop():
            return False

    return True


# --- Pruebas unitarias ---
def test_palindromo():
    """Pruebas para verificar el funcionamiento de es_palindromo()."""
    assert es_palindromo("anita lava la tina") == True
    assert es_palindromo("Amo la paloma") == True
    assert es_palindromo("Hola mundo") == False
    assert es_palindromo("Reconocer") == True
    assert es_palindromo("Python") == False
    print("✅ Todas las pruebas pasaron correctamente.")


# --- Ejecución principal ---
if __name__ == "__main__":
    texto = input("Ingrese una palabra o frase: ")
    if es_palindromo(texto):
        print("✅ Es un palíndromo.")
    else:
        print("❌ No es un palíndromo.")
    test_palindromo()

Análisis fuera del programa
1. Descripción del algoritmo:
El programa usa una pila para almacenar la primera mitad del texto, y luego compara los caracteres restantes (de derecha a izquierda) con los que va sacando de la pila.
Si todos coinciden, el texto es un palíndromo.
2. Complejidad Temporal:
Cada carácter del texto se procesa una sola vez.
👉 Complejidad temporal: O(n)
3. Complejidad Espacial:
La pila almacena solo la mitad del texto.
👉 Complejidad espacial: O(n/2) ≈ O(n)
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

#Codigo
class EditorTexto:
    """
    Clase que simula un editor de texto con operaciones de
    escribir, deshacer y rehacer, utilizando pilas.
    """

    def __init__(self) -> None:
        """
        Inicializa el editor con contenido vacío y pilas
        para manejar deshacer y rehacer.
        """
        self.contenido: str = ""
        self.pilaDeshacer: list[str] = []
        self.pilaRehacer: list[str] = []

    def escribir(self, texto: str) -> None:
        """
        Agrega texto al contenido actual.

        Args:
            texto (str): Texto que se desea añadir al contenido.
        """
        self.pilaDeshacer.append(self.contenido)
        self.contenido += texto
        self.pilaRehacer.clear()

    def deshacer(self) -> None:
        """
        Revierte la última acción realizada.
        Mueve el estado actual a la pila de rehacer.
        """
        if not self.pilaDeshacer:
            return
        self.pilaRehacer.append(self.contenido)
        self.contenido = self.pilaDeshacer.pop()

    def rehacer(self) -> None:
        """
        Recupera una acción previamente deshecha.
        Mueve el estado actual a la pila de deshacer.
        """
        if not self.pilaRehacer:
            return
        self.pilaDeshacer.append(self.contenido)
        self.contenido = self.pilaRehacer.pop()

    def mostrar(self) -> None:
        """
        Imprime el contenido actual del editor.
        """
        print(f"Contenido actual: '{self.contenido}'")

#Pruebas unitarias
import unittest
from io import StringIO
import sys

# ---------------------------
# 1. EditorTexto
# ---------------------------
class EditorTexto:
    def __init__(self) -> None:
        self.contenido: str = ""
        self.pilaDeshacer: list[str] = []
        self.pilaRehacer: list[str] = []

    def escribir(self, texto: str) -> None:
        self.pilaDeshacer.append(self.contenido)
        self.contenido += texto
        self.pilaRehacer.clear()

    def deshacer(self) -> None:
        if not self.pilaDeshacer:
            return
        self.pilaRehacer.append(self.contenido)
        self.contenido = self.pilaDeshacer.pop()

    def rehacer(self) -> None:
        if not self.pilaRehacer:
            return
        self.pilaDeshacer.append(self.contenido)
        self.contenido = self.pilaRehacer.pop()

    def mostrar(self) -> str:
        return f"Contenido actual: '{self.contenido}'"


class TestEditorTexto(unittest.TestCase):
    def test_escribir_y_mostrar(self):
        editor = EditorTexto()
        editor.escribir("Hola")
        self.assertEqual(editor.mostrar(), "Contenido actual: 'Hola'")

    def test_deshacer(self):
        editor = EditorTexto()
        editor.escribir("Hola")
        editor.escribir(" Mundo")
        editor.deshacer()
        self.assertEqual(editor.contenido, "Hola")

    def test_rehacer(self):
        editor = EditorTexto()
        editor.escribir("Hola")
        editor.escribir(" Mundo")
        editor.deshacer()
        editor.rehacer()
        self.assertEqual(editor.contenido, "Hola Mundo")

#Análisis de complejidad
Tiempo:
escribir: O(1) amortizado (concatenar string depende del tamaño, pero en Python puede considerarse O(len(texto))).
deshacer y rehacer: O(1) porque solo hacen operaciones de pila.
mostrar: O(1).
Espacio:
Se almacenan copias del contenido en pilas, por lo que en el peor caso el espacio crece en O(n·m), donde n es el número de operaciones y m el tamaño promedio del contenido guardado en cada acción.
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
#codigo
def mover(origen: list[int], destino: list[int], nombre_origen: str, nombre_destino: str) -> None:
    """
    Mueve el disco superior de la torre origen a la torre destino.

    Args:
        origen (list[int]): Torre origen representada como lista (pila).
        destino (list[int]): Torre destino representada como lista (pila).
        nombre_origen (str): Nombre de la torre origen (para mostrar en pantalla).
        nombre_destino (str): Nombre de la torre destino (para mostrar en pantalla).
    """
    disco = origen.pop()
    destino.append(disco)
    print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")


def hanoi(n: int, origen: list[int], destino: list[int], auxiliar: list[int],
          nombre_origen: str, nombre_destino: str, nombre_auxiliar: str) -> None:
    """
    Resuelve el problema de la Torre de Hanoi usando recursión.

    Args:
        n (int): Número de discos a mover.
        origen (list[int]): Torre origen.
        destino (list[int]): Torre destino.
        auxiliar (list[int]): Torre auxiliar.
        nombre_origen (str): Nombre de la torre origen.
        nombre_destino (str): Nombre de la torre destino.
        nombre_auxiliar (str): Nombre de la torre auxiliar.
    """
    if n == 1:
        mover(origen, destino, nombre_origen, nombre_destino)
        return

    hanoi(n - 1, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino)
    mover(origen, destino, nombre_origen, nombre_destino)
    hanoi(n - 1, auxiliar, destino, origen, nombre_auxiliar, nombre_destino, nombre_origen)

# pruebas
def mover(origen, destino, nombre_origen, nombre_destino):
    disco = origen.pop()
    destino.append(disco)
    print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")

def hanoi(n, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar):
    if n == 1:
        mover(origen, destino, nombre_origen, nombre_destino)
        return
    hanoi(n - 1, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino)
    mover(origen, destino, nombre_origen, nombre_destino)
    hanoi(n - 1, auxiliar, destino, origen, nombre_auxiliar, nombre_destino, nombre_origen)

class TestHanoi(unittest.TestCase):
    def test_hanoi_con_3_discos(self):
        origen = [3, 2, 1]
        destino = []
        auxiliar = []

        captured_output = StringIO()
        sys.stdout = captured_output  # redirigir print

        hanoi(3, origen, destino, auxiliar, "A", "C", "B")

        sys.stdout = sys.__stdout__  # restaurar print

        self.assertEqual(destino, [3, 2, 1])  # todos los discos en torre C

#Complejidad de la Torre de Hanoi
Tiempo:
Número de movimientos = 2n - 1
Crece exponencialmente → para pocos discos es rápido, pero para muchos se vuelve impracticable.
Espacio:
Se necesitan 3 torres con n discos en total → O(n).
La recursión alcanza una profundidad máxima de n llamadas → O(n).
➡️ Resumen final:
Tiempo: O(2^n)
Espacio: O(n)
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
#codigo
import re

def validar_html(codigo):
    """
    Valida si un código HTML simplificado tiene etiquetas balanceadas
    y correctamente anidadas usando una pila.

    Reglas:
    - Solo se consideran etiquetas de apertura <tag> y cierre </tag>.
    - No se contemplan atributos dentro de las etiquetas.
    - No se contemplan etiquetas autocerradas (<br/>).

    Args:
        codigo (str): Cadena con el código HTML a validar.

    Returns:
        bool: True si las etiquetas están balanceadas y anidadas, 
              False en caso contrario.

    Ejemplos:
        >>> validar_html("<html><body><h1>Título</h1></body></html>")
        True
        >>> validar_html("<html><body></html></body>")
        False
    """
    pila = []

    for etiqueta in re.finditer(r'</?([a-zA-Z0-9]+)>', codigo):
        nombre = etiqueta.group(1)

        # Si la etiqueta es de apertura
        if codigo[etiqueta.start() + 1] != '/':
            pila.append(nombre)
        else:  # Etiqueta de cierre
            if not pila or pila.pop() != nombre:
                return False

    return not pila

#Complejidad
import re

def validar_html(codigo: str) -> bool:
    pila = []
    for etiqueta in re.finditer(r'</?([a-zA-Z0-9]+)>', codigo):
        nombre = etiqueta.group(1)
        if codigo[etiqueta.start() + 1] != '/':  # apertura
            pila.append(nombre)
        else:  # cierre
            if not pila or pila.pop() != nombre:
                return False
    return not pila

class TestValidadorHTML(unittest.TestCase):
    def test_html_valido(self):
        codigo = "<html><body><h1>Titulo</h1></body></html>"
        self.assertTrue(validar_html(codigo))

    def test_html_invalido(self):
        codigo = "<html><body></html></body>"
        self.assertFalse(validar_html(codigo))

    def test_html_vacio(self):
        codigo = ""
        self.assertTrue(validar_html(codigo))  # no hay etiquetas, está balanceado

#complejidad algoritmica
Tiempo:
El regex recorre el string completo → O(m), donde m = longitud del código.
Cada etiqueta se procesa en O(1).
Complejidad total: O(m).
Espacio:
En la pila se almacenan a lo sumo todas las etiquetas abiertas → O(n), donde n = número de etiquetas.

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
