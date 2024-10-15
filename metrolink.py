import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф для моделювання мережі метро
G = nx.Graph()

# Додаємо вершини (станції метро)
stations = ["Lime Street", "Moorfields", "Liverpool Central", "James Street", 
            "Brunswick", "Edge Hill", "Sandhills", "Hamilton Square", "Birkenhead", "Conway Park"]

G.add_nodes_from(stations)

# Додаємо ребра (шляхи між станціями)
connections = [("Lime Street", "Moorfields"), 
               ("Lime Street", "Liverpool Central"), 
               ("Liverpool Central", "James Street"),
               ("Moorfields", "James Street"),
               ("James Street", "Brunswick"),
               ("Lime Street", "Edge Hill"),
               ("Moorfields", "Sandhills"),
               ("Sandhills", "Hamilton Square"),
               ("Hamilton Square", "Birkenhead"),
               ("Birkenhead", "Conway Park")]

G.add_edges_from(connections)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Стиль для позиціювання графа
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Мережа метро Ліверпуля (10 станцій)")
plt.show()

# Аналіз основних характеристик графа
print(f"Кількість вершин (станцій): {G.number_of_nodes()}")
print(f"Кількість ребер (шляхів): {G.number_of_edges()}")

# Ступінь вершин (кількість з'єднань для кожної станції)
degrees = dict(G.degree())
print("\nСтупінь вершин (кількість з'єднань для кожної станції):")
for station, degree in degrees.items():
    print(f"{station}: {degree}")
