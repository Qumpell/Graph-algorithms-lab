def print_successors(graph):
    print("Lista nastepnikow:")
    for vertex in graph.keys():
        print(f'{vertex}: {" ".join(map(str, graph[vertex]))}')


def print_degree_and_edges_count(graph):
    print("Ciag stopni:", end=" ")
    list_of_degrees = list()
    for vertex in graph.keys():
        list_of_degrees.append(len(graph[vertex]))
    print(", ".join(map(str, sorted(list_of_degrees, reverse=True))))
    print(f'Liczba krawedzi: {int(sum(list_of_degrees)/2)}')


def print_edges_weight_sum(edge_weight_list):
    sum = 0
    for key in edge_weight_list.keys():
        sum = sum + int(edge_weight_list[key])
    print(f'Suma wag krawedzi: {sum}')


with open("graph0.txt", "r") as file:
    weight_matrix = list()
    graph = dict()
    graph_with_weights = dict()
    edge_weight_list = dict()
    c = 1
    for line in file:
        row = line.strip().split(" ")
        row = [float('inf') if x == "-" else x for x in row]
        graph[c] = list()
        tmp = dict()
        for i in range(0, len(row)):
            if row[i] != float('inf'):
                graph[c].append(i + 1)
                tmp[i + 1] = row[i]
                if (c, i+1) and (i+1, c) not in edge_weight_list.keys():
                    edge_weight_list[(c, i + 1)] = row[i]
        graph_with_weights[c] = tmp
        c = c + 1
        weight_matrix.append(row)

    print(weight_matrix)
    print(graph)
    print(graph_with_weights)
    print(edge_weight_list)
    print_successors(graph)
    print_degree_and_edges_count(graph)
    print_edges_weight_sum(edge_weight_list)
