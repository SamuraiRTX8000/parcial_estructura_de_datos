
import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
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

# Posiciones de los nodos
pos = {
    "A": (0, 1),
    "B": (1, 2),
    "C": (2, 1.5),
    "D": (0.7, 0),
    "E": (2, 0)
}

# Crear la figura
plt.figure(figsize=(9, 7))

# -------------------------
# DIBUJAR NODOS
# -------------------------

nx.draw_networkx_nodes(
    grafo,
    pos,
    node_color="dodgerblue",
    node_size=1200,
    edgecolors="black",
    linewidths=2
)

# -------------------------
# DIBUJAR ETIQUETAS
# -------------------------

nx.draw_networkx_labels(
    grafo,
    pos,
    font_color="white",
    font_size=14,
    font_weight="bold"
)

# -------------------------
# DIBUJAR ARISTAS
# -------------------------

nx.draw_networkx_edges(
    grafo,
    pos,
    edge_color="gray",
    width=2.5
)

# -------------------------
# MOSTRAR PESOS
# -------------------------

pesos = nx.get_edge_attributes(grafo, "weight")

nx.draw_networkx_edge_labels(
    grafo,
    pos,
    edge_labels=pesos,
    font_size=13,
    font_weight="bold",
    label_pos=0.5,
    bbox=dict(
        facecolor="white",
        edgecolor="none",
        alpha=0.8
    )
)

# -------------------------
# TÍTULO
# -------------------------

plt.title(
    "GRAFO PONDERADO",
    fontsize=18,
    fontweight="bold"
)

# -------------------------
# LEYENDA
# -------------------------

plt.text(
    -0.2,
    -0.45,
    "Vértices: A, B, C, D, E\n"
    "Aristas: conexiones entre vértices\n"
    "Número: peso de la arista",
    fontsize=11,
    bbox=dict(
        facecolor="white",
        edgecolor="gray",
        boxstyle="round,pad=0.5"
    )
)

# Quitar ejes
plt.axis("off")

# Ajustar espacio
plt.tight_layout()

# Mostrar
plt.show()

