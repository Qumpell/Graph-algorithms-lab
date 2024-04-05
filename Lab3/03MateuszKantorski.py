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




def main() -> None:
    graph = read_graph_from_file("graph05z.txt")
    print(graph)


if __name__ == "__main__":
    main()
