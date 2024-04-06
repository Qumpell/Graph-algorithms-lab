# def read_graph_from_file(filename: str) -> dict[int, list[int]]:
#     graph = dict()
#     vertex_number = 1
#     with open(filename, 'r') as file:
#         for line in file:
#             row = line.strip().split(" ")
#             if vertex_number not in graph.keys():
#                 graph[vertex_number] = [[], []]
#                 # graph[vertex_number] = []
#
#             for i in range(len(row)):
#                 if row[i] != "-":
#                     # graph[vertex_number][0].append(i + 1)
#                     graph[vertex_number][0].append(i + 1)
#                     graph[vertex_number][1].append(row[i])
#             # for v in graph[vertex_number][0]:
#             #     if v not in graph.keys():
#             #         graph[v] = [[], []]
#             #     graph[v][1].append(vertex_number)
#             vertex_number += 1
#     return graph
from typing import Dict, Any


def read_graph_from_file_with_weights(filename: str) -> dict[int | Any, dict[int, float | str]]:
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


def print_sublists(list):
    for sublista in list:
        print(" ".join(map(str, sublista)))


def floyd_warshall(graph):
    n = len(graph.keys())
    w = [[0 if i == j else graph[i + 1][j + 1] if (j + 1) in graph[i + 1] else float('inf') for j in range(n)] for i in
         range(n)]
    p = [[i + 1 if i == j else i + 1 if (j + 1) in graph[i + 1] else None for j in range(n)] for i in range(n)]
    print(f'W 0:=')
    print_sublists(w)
    print()
    print(f'P 0:=')
    print_sublists(p)
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
            print_sublists(w)
            print()
            print("Ostateczna macierz poprzednikow:")
            print_sublists(p)
            print()
            if negative_cycle:
                print("Ujemny cykl. Nie ma rozwiazania.")
        else:
            print(f'W {t + 1}:=')
            print_sublists(w)
            print()
            print(f'P {t + 1}:=')
            print_sublists(p)
            print()
        if negative_cycle:
            break

    print_shortest_path(1, p, n)


def print_shortest_path(source, p, vertices):
    # for v in range(vertices):
    #     path = [v]
    #     x = v + 1
    #     i = 0
    #     while x != i:
    #         # print("JESTEN")
    #         x = p[i][x]
    #         # print(f'x {x}')
    #         # print(f'i {i}')
    #         path.append(x + 1)
        # print(path)
    L = [2]
    i = 1
    x = 2
    while x != i:
        vk = p[i][x]
        L.append(vk)
        x = vk
    print(L)

def main() -> None:
    graph = read_graph_from_file_with_weights("graph05bez.txt")
    print(graph)
    floyd_warshall(graph)


if __name__ == "__main__":
    main()
