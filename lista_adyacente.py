import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_edges_from([
    ("A", "B", {"weight": 4}),
    ("A", "D", {"weight": 6}),
    ("B", "C", {"weight": 7}),
    ("B", "D", {"weight": 7}),
    ("C", "D", {"weight": 2}),
    ("C", "E", {"weight": 5}),
    ("D", "E", {"weight": 3})
])

# Crear la lista de adyacencia
lista_adyacencia = {}

for nodo in grafo.nodes():
    lista_adyacencia[nodo] = []

    for vecino in grafo.neighbors(nodo):
        peso = grafo[nodo][vecino]["weight"]
        lista_adyacencia[nodo].append(f"{vecino}({peso})")


# Crear la ventana
fig, ax = plt.subplots(figsize=(8, 5))

ax.axis("off")

# Título
ax.set_title(
    "LISTA DE ADYACENCIA DEL GRAFO",
    fontsize=16,
    fontweight="bold"
)

# Mostrar cada nodo y sus conexiones
y = 0.85

for nodo, vecinos in lista_adyacencia.items():

    texto = f"{nodo}  →  " + ", ".join(vecinos)

    ax.text(
        0.1,
        y,
        texto,
        fontsize=14,
        fontweight="bold",
        transform=ax.transAxes
    )

    y -= 0.15

plt.show()