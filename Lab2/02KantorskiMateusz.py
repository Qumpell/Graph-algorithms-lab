from collections import deque


def read_graph_from_file(filename: str) -> dict[int, list[list[int]]]:
    graph = dict()
    vertex_number = 1
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(" ")
            if vertex_number not in graph.keys():
                graph[vertex_number] = [[], []]

            for i in range(len(row)):
                if row[i] != "-":
                    graph[vertex_number][0].append(i + 1)

            for v in graph[vertex_number][0]:
                if v not in graph.keys():
                    graph[v] = [[], []]
                graph[v][1].append(vertex_number)
            vertex_number += 1
    return graph


def bfs(graph: dict[int, list[list[int]]], l_subset: list[[int]]) -> dict[tuple[int, int], list]:
    queue = deque()
    queue.append(l_subset[0])

    p = {key: [0, 0] for key in l_subset}

    while queue:
        current_node = queue.popleft()
        for neighbour in graph[current_node][0]:
            if neighbour not in l_subset:
                continue
            if p[neighbour][0] == 0:
                p[neighbour][0] = 1
                queue.append(neighbour)

    queue.append(l_subset[0])
    while queue:
        current_node = queue.popleft()
        for neighbour in graph[current_node][1]:
            if neighbour not in l_subset:
                continue
            if p[neighbour][1] == 0:
                p[neighbour][1] = 1
                queue.append(neighbour)

    v_sets = dict()
    v_sets[(0, 0)] = []
    v_sets[(1, 0)] = []
    v_sets[(0, 1)] = []
    v_sets[(1, 1)] = []
    for key, value in p.items():
        v_sets[(value[0], value[1])].append(key)
    return v_sets


def leifman_algorithm(graph: dict[int, list[list[int]]]) -> None:
    l_set = [sorted(list(graph.keys())).copy()]
    c_set = []

    while any(l for l in l_set):

        print(f'Rozpatrujemy:= {l_set[0]}')

        v_set = bfs(graph, l_set.pop(0))

        print(f'V11:={v_set[(1, 1)]}\nV10:={v_set[(1, 0)]}')
        print(f'V01:={v_set[(0, 1)]}\nV00:={v_set[(0, 0)]}')

        if len(v_set[(1, 1)]) != 0:
            c_set.append(v_set[(1, 1)])
        else:
            c_set.append([v_set[(0, 0)][0]])
            v_set[(0, 0)].pop(0)

        l_set.append(v_set[(1, 0)])
        l_set.append(v_set[(0, 0)])
        l_set.append(v_set[(0, 1)])
        l_set = list(filter(None, l_set))

        print(f'C:= {c_set}')
        print(f'L:= {l_set}')


def main() -> None:
    graph = read_graph_from_file("leifman.txt")
    leifman_algorithm(graph)


if __name__ == "__main__":
    main()
