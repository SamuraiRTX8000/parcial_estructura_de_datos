import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de los nodos y la matriz de adyacencia exacta extraída del grafo
nodos = ['A', 'B', 'C', 'D', 'E']
matriz_adyacencia = np.array([
    [0, 4, 0, 6, 0],  # Conexiones del nodo A
    [4, 0, 7, 7, 0],  # Conexiones del nodo B
    [0, 7, 0, 2, 5],  # Conexiones del nodo C
    [6, 7, 2, 0, 3],  # Conexiones del nodo D
    [0, 0, 5, 3, 0]   # Conexiones del nodo E
])

# 2. Configuración de la figura y el lienzo
fig, ax = plt.subplots(figsize=(7, 7))

# Renderizado de la matriz como un mapa de calor (Heatmap)
# Se usa 'Blues' para dar un aspecto profesional y analítico
cax = ax.matshow(matriz_adyacencia, cmap='Blues', vmin=0, vmax=7)

# 3. Formateo de los ejes (Filas y Columnas)
ax.set_xticks(np.arange(len(nodos)))
ax.set_yticks(np.arange(len(nodos)))
ax.set_xticklabels(nodos, fontsize=12, fontweight='bold')
ax.set_yticklabels(nodos, fontsize=12, fontweight='bold')

# Mover las etiquetas del eje X a la parte inferior para facilitar la lectura estilo tabla
ax.xaxis.set_ticks_position('bottom')

# 4. Inserción de los valores (pesos y ceros) dentro de la cuadrícula
for i in range(len(nodos)):
    for j in range(len(nodos)):
        valor = matriz_adyacencia[i, j]
        # Lógica de contraste: Si la celda es muy oscura (valores > 4), el texto es blanco
        color_texto = "white" if valor > 4 else "black"
        ax.text(j, i, str(valor), va='center', ha='center', 
                color=color_texto, fontsize=14, fontweight='bold')

# 5. Ajustes estéticos finales
plt.title('Matriz de Adyacencia del Grafo Ponderado', pad=20, fontsize=14, fontweight='bold')

# Barra lateral como leyenda de la intensidad de los pesos
cbar = fig.colorbar(cax, fraction=0.046, pad=0.04)
cbar.set_label('Peso de la conexión', rotation=270, labelpad=15, fontsize=12)

# Ocultar los bordes negros externos de la gráfica para un diseño moderno
for edge, spine in ax.spines.items():
    spine.set_visible(False)

plt.tight_layout()
plt.show()