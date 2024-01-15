import networkx as nx
import matplotlib.pyplot as plt
import random
import requests

def first():
    edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()


def second():
    G = nx.cubical_graph()
    print(G)
    nx.draw(G)
    plt.show()
    print(' В кубическом графе')
    print(nx.cycle_basis(G, 0))

def third():
    G = nx.DiGraph()
    G.add_edges_from([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                      (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
                      (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)])

    nx.draw(G)
    print(sorted(nx.simple_cycles(G)))
    plt.show()

def fourth():

    G = nx.Graph()


    G.add_nodes_from(range(10))

    # Проходим по каждой паре вершин
    for i in range(10):
        for j in range(i + 1, 10):
            # Генерируем случайное число от 0 до 1
            probability = random.random()

            # Если случайное число меньше или равно 0.1,
            # то добавляем ребро между вершинами i и j
            if probability <= 0.1:
                G.add_edge(i, j)

    nx.draw(G)

    plt.show()

    print(G.edges)


def fifth():
    probabilities = []
    largest_component_sizes = []
    for _ in range(1000):
        p_i = random.uniform(0.005, 0.03)
        probabilities.append(p_i)
        G = nx.erdos_renyi_graph(100, p_i)
        connected_components = list(nx.connected_components(G))
        largest_component_size = max(len(component) for component in connected_components)
        largest_component_sizes.append(largest_component_size)
    plt.scatter(probabilities, largest_component_sizes)
    plt.xlabel("p_i")
    plt.ylabel("best s_i")

    # Отображение графика
    plt.show()

def get_friends_ids(user_id):
    friends_url = f"https://api.vk.com/method/friends.get?user_id={user_id}&v=5.199&access_token=???"
    json_response = requests.get(friends_url.format(user_id)).json()
    if json_response.get("error"):
        print(json_response.get("error"))
        return list()
    return json_response[u"response"]


def six():
    graph = {}
    friend_ids = get_friends_ids(1405906)  # ваш user id, для которого вы хотите построить граф друзей.
    for friend_id in friend_ids:
        print('Processing id: ', friend_id)
        graph[friend_id] = get_friends_ids(friend_id)

    g = nx.Graph(directed=False)
    for i in graph:
        g.add_node(i, label=i)
        for j in graph[i]:
            if i != j and i in friend_ids and j in friend_ids:
                g.add_edge(i, j)

    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True)
    plt.tight_layout()
    plt.show()


#first()
#second()
#third()
#fourth()
#fifth()
#six()


