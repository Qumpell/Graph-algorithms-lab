from collections import deque


def read_graph_from_file(filename: str):
    X = dict()
    Y = dict()
    with open(filename, "r") as file:
        c = 1
        for line in file:
            Y[c] = []

            row = line.strip().split(" ")
            row = [float('inf') if x == "-" else x for x in row]
            for i in range(0, len(row)):
                if row[i] != float('inf'):
                    Y[c].append(i + 1)
                    if i + 1 not in X.keys():
                        X[i + 1] = [c]
                    else:
                        X[i + 1].append(c)
            c = c + 1

    return X, Y


def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        try:
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
        except KeyError:
            graph[node] = []
    return None


def hungarian_algorithm(X, Y):
    Tx = {}
    Ty = {}
    skoj = True
    S = []
    T = []
    while len(Tx) != len(X) and skoj:

        u = 0
        for e in sorted(X.keys()):
            if e not in Tx.keys():
                u = e
                break
        visited = [False for _ in range(len(X))]
        S = [u]
        T = []

        is_exit = False
        local_tree = {}
        while skoj and not is_exit:
            x = None
            i = 0
            for s in S:
                i += 1

                if not visited[s - 1]:
                    x = s
                    visited[s - 1] = True
                    break

                elif i == len(S):
                    skoj = False
                    break

            if not skoj:
                break

            for y in X[x]:
                if y in T:
                    continue

                T.append(y)

                if x not in local_tree.keys():
                    local_tree[x] = []
                local_tree[x].append(str(y) + "y")
                if y not in Ty.keys():

                    path = bfs(local_tree, u, str(y) + "y")

                    for i in range(0, len(path) - 1, 2):
                        Tx[path[i]] = int(path[i + 1][:-1])
                        Ty[int(path[i + 1][:-1])] = path[i]
                        path[i+1] = int(path[i + 1][:-1])

                    is_exit = True
                    print(f'Sciezka M-zasilona:= {path}')
                    print(f'Aktualne skojarzenie:={Tx}')
                    break
                else:
                    S.append(Ty[y])
                    if str(y) + "y" not in local_tree.keys():
                        local_tree[str(y) + "y"] = []
                    local_tree[str(y) + "y"].append(Ty[y])
                    visited[Ty[y] - 1] = False

    if len(Tx) == len(X) or skoj:
        print(f'Znalezlismy skojarzenie nasycajace zbior X:= {Tx}')
    else:
        print("Nie ma skojarzenia w grafie.")
        print(f'Dla S:= {S} i T:= {T} mamy |N(S)| < |S|, czyli {len(T)} < {len(S)}')


def main() -> None:
    X, Y = read_graph_from_file(filename="graph11.txt")
    hungarian_algorithm(X, Y)


if __name__ == "__main__":
    main()
