import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()
grafo.add_edges_from ([("A","B",{ "weight": 4 }),
                     ("A","D",{"weight": 6}),
                    ("B", "A", {"weight": 4}),
                    ("B","C", {"weight": 7}),
                    ("B","D", {"weight": 7}),
                    ("C","B", {"weight": 7}),
                    ("C","D", {"weight": 2}),
                    ("C","E", {"weight": 5}),
                    ("D","A", {"weight": 6}),
                    ("D","B", {"weight": 7}),
                    ("D","C", {"weight": 2}),
                    ("D","E", {"weight": 3}),
                    ("E","C", {"weight": 5}),
                    ("E","D", {"weight": 3})])

# Posición de los nodos
# Posiciones EXACTAS de los nodos
pos = {
    "A": (0, 1),
    "B": (1, 2),
    "C": (2, 1.5),
    "D": (0.7, 0),
    "E": (2, 0)
}

# Dibujar grafo
nx.draw(
    grafo,
    pos,
    with_labels=True,
    node_color="dodgerblue",
    node_size=1000,
    font_color="white",
    font_weight="bold",
    edge_color="gray",
    width=1.5
)

# Obtener pesos
pesos = nx.get_edge_attributes(grafo, "weight")

# Mostrar pesos
nx.draw_networkx_edge_labels(
    grafo,
    pos,
    edge_labels=pesos,
    font_size=12,
    font_weight="bold"
)

# Título
plt.title("GRAFO PONDERADO\nCON 5 NODOS", fontweight="bold")

plt.axis("off")
plt.show()