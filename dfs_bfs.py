import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

stations = ["Lime Street", "Moorfields", "Liverpool Central", "James Street", 
            "Brunswick", "Edge Hill", "Sandhills", "Hamilton Square", "Birkenhead", "Conway Park"]

G.add_nodes_from(stations)

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
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Мережа метро Ліверпуля (10 станцій)")
plt.show()
# DFS алгоритм 
def dfs(graph, start, goal):
    stack = [(start, [start])]  
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

# BFS 
def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # черга
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in set(graph[vertex]) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

# Введемо дві станції для пошуку шляху
start_station = "Lime Street"
goal_station = "Birkenhead"

# Виконання DFS і BFS
dfs_path = dfs(G, start_station, goal_station)
bfs_path = bfs(G, start_station, goal_station)

# Виведення результатів
print(f"Шлях за допомогою DFS (Глибина): {dfs_path}")
print(f"Шлях за допомогою BFS (Ширина): {bfs_path}")

#DFS (Глибина): досліджує одну гілку максимально глибоко, перш ніж повернутись до іншої гілки.DFS обирає спочатку шлях через станції "Liverpool Central", потім "James Street", "Brunswick" і досліджує інші станції.
# Шлях, що будується DFS довший, оскільки алгоритм іде в глибину (досліджує всю гілку), і не обов'язково знаходить найкоротший шлях.

#BFS (Ширина): гарантує, що знайдений шлях буде найкоротшим у кількості ребер.Алгоритм перевіряє всі сусідні станції на першому рівні, потім переходить до другого і так далі.
# В даному випадку BFS знаходить найкоротший шлях між "Lime Street" і "Birkenhead" через "Moorfields", "Sandhills" та "Hamilton Square".

# Висновок
#DFS знаходить один із можливих шляхів, але він не обов'язково є найкоротшим.BFS знаходить найкоротший шлях (за кількістю ребер) між двома вершинами.
#В нашому випадку, BFS підходить краще. 7 станцій проти 5.