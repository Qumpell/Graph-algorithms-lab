from collections import deque


def read_graph_from_file(filename: str) -> dict[int, list[int]]:
    graph = dict()
    with open(filename, "r") as file:
        c = 1
        for line in file:
            graph[c] = []
            row = line.strip().split(" ")
            row = [float('inf') if x == "-" else x for x in row]
            for i in range(0, len(row)):
                if row[i] != float('inf'):
                    graph[c].append(i + 1)
            c = c + 1
    return graph


def prepare_data(graph, starting_vertex):
    edges_list = []
    root = {}
    predecessor = {}
    v_stop = len(graph[starting_vertex]) + 1
    for key in graph.keys():
        adj_vertices = graph[key]
        for v in adj_vertices:
            if (key, v) not in edges_list and (v, key) not in edges_list:
                edges_list.append((key, v))
            root[v] = v
            predecessor[v] = None
    return edges_list, root, predecessor, v_stop


def add_edge(curr_edge, root, graph, predecessor):
    predecessor1 = new_root(curr_edge[1], root, predecessor)
    predecessor[curr_edge[1]] = curr_edge[0]
    x1 = root[curr_edge[1]]
    x2 = root[curr_edge[0]]
    for w in graph.keys():
        if root[w] == x1:
            root[w] = x2
    return predecessor1, root


def find_all_vertex(graph, start_v):
    successors = set()
    visited = set()
    queue = deque([start_v])

    while queue:
        current_vertex = queue.popleft()
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for vertex, successor in graph.items():
            if successor == current_vertex:
                successors.add(vertex)
                queue.append(vertex)

    return successors


def delete_edge(curr_edge, predecessor, root):
    u, v = curr_edge
    v1 = v if predecessor[u] == v else u
    v2 = u if predecessor[u] == v else v

    predecessor[v2] = None
    vertices = find_all_vertex(predecessor, v2)
    vertices.add(v2)
    for v in vertices:
        root[v] = v2
    return predecessor, root


def new_root(v, root, predecessor):
    x_old = root[v]
    if x_old == v:
        return predecessor
    u1 = None
    u2 = v
    while u1 != x_old:
        p = u1
        u1 = u2
        u2 = predecessor[u1]
        predecessor[u1] = p
    return predecessor


def generate_all_spanning_trees(edges_list, root, predecessor, v_stop, graph):
    v_count = len(graph.keys())
    e_count = len(edges_list)
    t_count = 1
    k = 0
    tree = [None for _ in range(len(edges_list))]
    i = -1
    while tree[0] != v_stop:
        e = edges_list[k]
        if root[e[0]] != root[e[1]]:
            predecessor, root = add_edge(curr_edge=e, predecessor=predecessor, root=root, graph=graph)
            i = i + 1
            tree[i] = k
        if tree[0] == v_stop:
            return
        elif i == v_count - 2:
            print(f'Krawedzie drzewa {t_count} :', end="")
            st = []
            for x in tree:
                if x is not None:
                    st.append(edges_list[x])
                    print(f'{edges_list[x]}', end="")
            print()
            t_count = t_count + 1
        if i == v_count - 2 or k == e_count - 1:
            if tree[i] == e_count - 1:
                predecessor, root = delete_edge(curr_edge=e, predecessor=predecessor, root=root)
                i = i - 1

            predecessor, root = delete_edge(curr_edge=edges_list[tree[i]], predecessor=predecessor, root=root)

            k = tree[i] + 1
            i = i - 1
        else:
            k = k + 1


def main() -> None:
    graph = read_graph_from_file(filename="Trees.txt")
    edges_list, root, predecessor, v_stop = prepare_data(graph, 1)
    generate_all_spanning_trees(root=root, graph=graph, predecessor=predecessor, edges_list=edges_list, v_stop=v_stop)


if __name__ == "__main__":
    main()
