# atividade_3.py
# Nome: Rafael De Freitas Fiel
# Disciplina: Estrutura de Dados II

from graphviz import Digraph
import random

# Classe que representa um nó da árvore
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Classe da Árvore Binária de Busca
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserir novo valor na árvore
    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    # Travessia In-Order (Esquerda - Raiz - Direita)
    def inorder(self):
        result = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)

        _inorder(self.root)
        return result

    # Travessia Pre-Order (Raiz - Esquerda - Direita)
    def preorder(self):
        result = []

        def _preorder(node):
            if node is None:
                return
            result.append(node.value)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return result

    # Travessia Post-Order (Esquerda - Direita - Raiz)
    def postorder(self):
        result = []

        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.value)

        _postorder(self.root)
        return result

    # Visualizar árvore usando Graphviz
    def visualize(self, filename):
        dot = Digraph()
        dot.attr("node", shape="circle")

        def add_nodes(node):
            if node is None:
                return
            dot.node(str(id(node)), str(node.value))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes(node.right)

        add_nodes(self.root)
        dot.render(filename, format="png", cleanup=True)
        print(f"Árvore salva como {filename}.png")


# Programa principal
if __name__ == "__main__":
    print("=== Árvore Fixa ===")
    bst_fixed = BinarySearchTree()
    fixed_values = [55, 30, 80, 20, 45, 70, 90]
    for v in fixed_values:
        bst_fixed.insert(v)

    bst_fixed.visualize("bst_fixed_traversal")

    # Imprime os resultados das travessias
    print("In-Order (Esquerda - Raiz - Direita):", bst_fixed.inorder())
    print("Pre-Order (Raiz - Esquerda - Direita):", bst_fixed.preorder())
    print("Post-Order (Esquerda - Direita - Raiz):", bst_fixed.postorder())

    print("\n=== Árvore Randômica ===")
    bst_random = BinarySearchTree()
    random_values = random.sample(range(1, 100), 10)  # 10 números aleatórios únicos
    print("Valores inseridos:", random_values)

    for v in random_values:
        bst_random.insert(v)

    bst_random.visualize("bst_random_traversal")

    # Imprime os resultados das travessias
    print("In-Order (Esquerda - Raiz - Direita):", bst_random.inorder())
    print("Pre-Order (Raiz - Esquerda - Direita):", bst_random.preorder())
    print("Post-Order (Esquerda - Direita - Raiz):", bst_random.postorder())
