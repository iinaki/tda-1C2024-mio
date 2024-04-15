# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

# (i) aumentar el valor del operando en 1;

# (ii) duplicar el valor del operando.

# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

# Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'


def operaciones(k):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = dp[i - 1] + 1
    
    # Reconstruir las operaciones
    operaciones = []
    while k > 0:
        if k % 2 == 0 and dp[k] == dp[k // 2] + 1:
            operaciones.append('por2')
            k //= 2
        else:
            operaciones.append('mas1')
            k -= 1
    
    return operaciones[::-1]

# Ejemplo de uso
k = 10
print(f"Mínima cantidad de operaciones para llegar a {k}: {operaciones(k)}")



Para resolver este problema utilizando programación dinámica, podemos seguir estos pasos:

Creamos un arreglo dp de tamaño K+1 para almacenar la cantidad mínima de operaciones necesarias para llegar desde 0 a cada número hasta K.
Inicializamos dp[0] = 0, ya que no se necesita ninguna operación para llegar a 0.
Para cada número i desde 1 hasta K, calculamos dp[i] como el mínimo entre dp[i-1] + 1 (incrementar en 1) y dp[i//2] + 1 (duplicar), teniendo en cuenta que si i es impar, solo podemos llegar a él a través de i-1 y luego incrementar en 1.
Al final, reconstruimos las operaciones necesarias para llegar a K siguiendo los valores de dp.
Aquí tienes una implementación en Python:

python
Copy code
def operaciones(k):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = dp[i - 1] + 1
    
    # Reconstruir las operaciones
    operaciones = []
    while k > 0:
        if k % 2 == 0 and dp[k] == dp[k // 2] + 1:
            operaciones.append('por2')
            k //= 2
        else:
            operaciones.append('mas1')
            k -= 1
    
    return operaciones[::-1]

# Ejemplo de uso
k = 10
print(f"Mínima cantidad de operaciones para llegar a {k}: {operaciones(k)}")
La ecuación de recurrencia para este algoritmo es:

�
�
[
�
]
=
{
0
si 
�
=
0
min
⁡
(
�
�
[
�
−
1
]
+
1
,
�
�
[
�
/
/
2
]
+
1
)
si 
�
>
0
 y 
�
 es par
�
�
[
�
−
1
]
+
1
si 
�
>
0
 y 
�
 es impar
dp[i]= 
⎩
⎨
⎧
​
  
0
min(dp[i−1]+1,dp[i//2]+1)
dp[i−1]+1
​
  
si i=0
si i>0 y i es par
si i>0 y i es impar
​
 


\[ dp[i] = \begin{cases} 
      0 & \text{si } i = 0 \\
      \min(dp[i-1] + 1, dp[i//2] + 1) & \text{si } i > 0 \text{ y } i \text{ es par} \\
      dp[i-1] + 1 & \text{si } i > 0 \text{ y } i \text{ es impar}
   \end{cases}
\]

Esta ecuación representa cómo se calcula la cantidad mínima de operaciones necesarias para llegar a cada número desde 0 hasta \(K\).
La complejidad de este algoritmo es O(K), donde K es el número al que queremos llegar. Esto se debe a que llenamos la matriz dp una vez, y para cada número i calculamos su valor en (1) O(1) operaciones, basándonos en los valores anteriores de dp.

