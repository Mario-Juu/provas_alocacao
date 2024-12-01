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

            # Primeira linha contém informações sobre o grafo
            header = lines[0].split()
            num_nodes = int(header[2])

            # Adiciona todos os nós ao grafo
            G.add_nodes_from(range(1, num_nodes + 1))

            # Lê as arestas
            for line in lines[1:]:
                # Verifica se a linha começa com 'e' para arestas
                if line.startswith('e '):
                    # Divide a linha e converte para inteiros, ignorando o 'e'
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
        # Reinicia a alocação
        self.node_types = {}

        # Conjunto de nós não alocados
        unassigned_nodes = set(self.graph.nodes())

        while unassigned_nodes:
            # Escolhe o nó com maior pontuação
            current_node = max(unassigned_nodes, key=lambda n: self.get_node_score(n, strategy))

            # Encontra o primeiro tipo de prova disponível
            used_types = set()
            for neighbor in self.graph.neighbors(current_node):
                if neighbor in self.node_types:
                    used_types.add(self.node_types[neighbor])

            # Escolhe o menor tipo de prova não usado pelos vizinhos
            prova_type = 1
            while prova_type in used_types:
                prova_type += 1

            # Atribui o tipo de prova ao nó
            self.node_types[current_node] = prova_type

            # Remove o nó do conjunto de não alocados
            unassigned_nodes.remove(current_node)

        return len(set(self.node_types.values()))

class ProvaAllocatorV4(ProvaAllocator):
    def allocate_provas(self):
        # Reinicia a alocação
        self.node_types = {}

        # Inicializa a saturação de cada nó (todos começam com saturação 0)
        saturation = {node: 0 for node in self.graph.nodes()}

        # Inicializa o grau de cada nó
        degrees = {node: self.graph.degree(node) for node in self.graph.nodes()}

        # Conjunto de nós não alocados
        unassigned_nodes = set(self.graph.nodes())

        while unassigned_nodes:
            # Seleciona o nó com maior saturação. Em caso de empate, usa o grau.
            current_node = max(
                unassigned_nodes,
                key=lambda n: (saturation[n], degrees[n])
            )

            # Encontra o primeiro tipo de prova disponível
            used_types = set(self.node_types[neighbor] for neighbor in self.graph.neighbors(current_node) if neighbor in self.node_types)
            prova_type = 1
            while prova_type in used_types:
                prova_type += 1

            # Atribui o tipo de prova ao nó
            self.node_types[current_node] = prova_type

            # Atualiza a saturação dos vizinhos
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in self.node_types:
                    neighbor_used_types = set(self.node_types[n] for n in self.graph.neighbors(neighbor) if n in self.node_types)
                    saturation[neighbor] = len(neighbor_used_types)

            # Remove o nó do conjunto de não alocados
            unassigned_nodes.remove(current_node)

        # Retorna o número de tipos de prova usados
        return len(set(self.node_types.values()))

def main():
    # Verifica os argumentos de linha de comando
    if len(sys.argv) != 3:
        print("Uso: python script.py <estrategia> <arquivo_sala>")
        sys.exit(1)

    # Converte os argumentos para os tipos corretos
    try:
        strategy = int(sys.argv[1])
        input_file = sys.argv[2]
    except ValueError:
        print("Erro: A estratégia deve ser um número inteiro.")
        sys.exit(1)

    # Valida a estratégia
    if strategy not in [1, 2, 3, 4]:
        print("Erro: Estratégia inválida. Use 1, 2, 3 ou 4.")
        sys.exit(1)

    # Cria o alocador e resolve o problema
    num_tipos_prova = 0
    if strategy == 4:
        allocator = ProvaAllocatorV4(input_file)
        num_tipos_prova = allocator.allocate_provas()
    else:
        allocator = ProvaAllocator(input_file)
        num_tipos_prova = allocator.allocate_provas(strategy)

    # Imprime o número de tipos de prova usados
    print(f"Número de tipos de prova: {num_tipos_prova}")


if __name__ == "__main__":
    main()