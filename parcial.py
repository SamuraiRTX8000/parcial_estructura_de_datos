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

for nodo in grafo:
    print(f"{nodo} -> ", end="")

    for vecino in grafo[nodo]:
        peso = grafo[nodo][vecino]["weight"]
        print(f"{vecino}({peso}) ", end="")

    print()