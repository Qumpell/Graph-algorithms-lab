def read_graph_from_file_with_weights(filename: str) -> dict[int, dict[int, int]]:
    graph_with_weights = dict()
    with open(filename, "r") as file:
        c = 1
        for line in file:
            row = line.strip().split(" ")
            row = [float('inf') if x == "-" else x for x in row]
            tmp = dict()
            for i in range(0, len(row)):
                if row[i] != float('inf'):
                    tmp[i + 1] = int(row[i])
            graph_with_weights[c] = tmp
            c = c + 1
    return graph_with_weights


def print_all_sublist(source_list: list[list[int]]) -> None:
    for sublist in source_list:
        print(" ".join(map(str, sublist)))


def floyd_warshall(graph: dict[int, dict[int, int]]) -> None:
    n = len(graph.keys())
    w = [[0 if i == j else graph[i + 1][j + 1] if (j + 1) in graph[i + 1] else float('inf') for j in range(n)] for i in
         range(n)]
    p = [[i + 1 if i == j else i + 1 if (j + 1) in graph[i + 1] else None for j in range(n)] for i in range(n)]
    print(f'W 0:=')
    print_all_sublist(w)
    print()
    print(f'P 0:=')
    print_all_sublist(p)
    print()
    negative_cycle = False
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if w[i][j] > w[i][t] + w[t][j]:
                    w[i][j] = w[i][t] + w[t][j]
                    p[i][j] = p[t][j]
                elif w[i][i] < 0:
                    negative_cycle = True
                    break
            if negative_cycle:
                break

        if t == n - 1 or negative_cycle:
            print("Ostateczna macierz odleglosci:")
            print_all_sublist(w)
            print()
            print("Ostateczna macierz poprzednikow:")
            print_all_sublist(p)
            print()
            if negative_cycle:
                print("Ujemny cykl. Nie ma rozwiazania.")
        else:
            print(f'W {t + 1}:=')
            print_all_sublist(w)
            print()
            print(f'P {t + 1}:=')
            print_all_sublist(p)
            print()
        if negative_cycle:
            break

    if not negative_cycle:
        print_shortest_path(predecessor_matrix=p, vertices_max_index=n)


def print_shortest_path(predecessor_matrix: list[list[int]], vertices_max_index: int) -> None:
    print("Najkrotsze sciezki:")

    for i in range(1, vertices_max_index + 1):
        for j in range(1, vertices_max_index + 1):
            path = [j]
            path_exits = True
            x = j
            while x != i:
                vk = predecessor_matrix[i - 1][x - 1]
                if vk is None:
                    path_exits = False
                    break
                path.append(vk)
                x = vk
            if path_exits:
                print(f'z {i} do {j} : {" ".join(map(str, list(reversed(path))))}')
            else:
                print(f'z {i} do {j} : Nie ma sciezki')


def main() -> None:
    graph = read_graph_from_file_with_weights(filename="MatrixPaths.txt")
    floyd_warshall(graph)


if __name__ == "__main__":
    main()
