import sys
import networkx as nx


class ProvaAllocator:
    def __init__(self, input_file):
        self.graph = self.read_graph(input_file)
        self.node_types = {}

    def read_graph(self, input_file):
        G = nx.Graph()
        with open(input_file, 'r') as f:
            lines = f.readlines()

            header = lines[0].split()
            num_nodes = int(header[2])

            G.add_nodes_from(range(1, num_nodes + 1))

            for line in lines[1:]:
                if line.startswith('e '):
                    _, u, v = line.split()
                    u, v = int(u), int(v)
                    G.add_edge(u, v)

        return G

    def get_node_score(self, node, strategy):
        if strategy == 1:  # Grau do vértice
            return self.graph.degree(node)

        elif strategy == 2:  # Número de vizinhos com tipo de prova atribuído
            return sum(1 for neighbor in self.graph.neighbors(node) if neighbor in self.node_types)

        elif strategy == 3:  # Número de vizinhos sem tipo de prova atribuído
            return sum(1 for neighbor in self.graph.neighbors(node) if neighbor not in self.node_types)

    def allocate_provas(self, strategy):
        self.node_types = {}

        unassigned_nodes = set(self.graph.nodes())

        while unassigned_nodes:
            current_node = max(unassigned_nodes, key=lambda n: self.get_node_score(n, strategy))

            used_types = set()
            for neighbor in self.graph.neighbors(current_node):
                if neighbor in self.node_types:
                    used_types.add(self.node_types[neighbor])

            prova_type = 1
            while prova_type in used_types:
                prova_type += 1

            self.node_types[current_node] = prova_type

            unassigned_nodes.remove(current_node)

        return len(set(self.node_types.values()))

class ProvaAllocatorV4(ProvaAllocator):
    def allocate_provas(self):
        self.node_types = {}

        saturation = {node: 0 for node in self.graph.nodes()}

        degrees = {node: self.graph.degree(node) for node in self.graph.nodes()}

        unassigned_nodes = set(self.graph.nodes())

        while unassigned_nodes:
            current_node = max(
                unassigned_nodes,
                key=lambda n: (saturation[n], degrees[n])
            )

            used_types = set(self.node_types[neighbor] for neighbor in self.graph.neighbors(current_node) if neighbor in self.node_types)
            prova_type = 1
            while prova_type in used_types:
                prova_type += 1

            self.node_types[current_node] = prova_type

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in self.node_types:
                    neighbor_used_types = set(self.node_types[n] for n in self.graph.neighbors(neighbor) if n in self.node_types)
                    saturation[neighbor] = len(neighbor_used_types)

            unassigned_nodes.remove(current_node)

        return len(set(self.node_types.values()))

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <estrategia> <arquivo_sala>")
        sys.exit(1)

    try:
        strategy = int(sys.argv[1])
        input_file = sys.argv[2]
    except ValueError:
        print("Erro: A estratégia deve ser um número inteiro.")
        sys.exit(1)

    if strategy not in [1, 2, 3, 4]:
        print("Erro: Estratégia inválida. Use 1, 2, 3 ou 4.")
        sys.exit(1)

    num_tipos_prova = 0
    if strategy == 4:
        allocator = ProvaAllocatorV4(input_file)
        num_tipos_prova = allocator.allocate_provas()
    else:
        allocator = ProvaAllocator(input_file)
        num_tipos_prova = allocator.allocate_provas(strategy)

    print(f"Número de tipos de prova: {num_tipos_prova}")


if __name__ == "__main__":
    main()