import networkx as nx
import heapq

G = nx.Graph()

stations = ["Lime Street", "Moorfields", "Liverpool Central", "James Street", 
            "Brunswick", "Edge Hill", "Sandhills", "Hamilton Square", "Birkenhead", "Conway Park"]

G.add_nodes_from(stations)

connections_with_weights = [
    ("Lime Street", "Moorfields", 5), 
    ("Lime Street", "Liverpool Central", 7), 
    ("Liverpool Central", "James Street", 3),
    ("Moorfields", "James Street", 4),
    ("James Street", "Brunswick", 6),
    ("Lime Street", "Edge Hill", 9),
    ("Moorfields", "Sandhills", 5),
    ("Sandhills", "Hamilton Square", 7),
    ("Hamilton Square", "Birkenhead", 2),
    ("Birkenhead", "Conway Park", 4)
]

G.add_weighted_edges_from(connections_with_weights)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0  # Відстань до початкової вершини 0
    priority_queue = [(0, start)]  # Черга для опрацювання вершин

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більше за відому, продовжуємо
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо всіх сусідів поточної вершини
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Виведемо найкоротші шляхи для кожної вершини
start_station = "Lime Street"

# Виконуємо алгоритм Дейкстри для кожної вершини
shortest_paths = dijkstra(G, start_station)

# Виведемо результати
print(f"Найкоротші шляхи від станції {start_station}:")
for station, distance in shortest_paths.items():
    print(f"Станція {station}: Відстань = {distance}")

#Алгоритм Дейкстри гарантує, що ми знайдемо найкоротший шлях від початкової вершини до всіх інших вершин графа.
#Виведені відстані показують мінімальні шляхи між станцією "Lime Street" і всіма іншими станціями у транспортній мережі.
