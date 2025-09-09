# atividade_2.py
# Nome: Rafael De Freitas Fiel
# Disciplina: Estrutura de Dados II

from graphviz import Digraph
import random

# Classe para representar cada nó da árvore
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Classe da Árvore Binária de Busca
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserir um novo valor na árvore
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

    # Buscar um valor na árvore
    def search(self, value):
        def _search(node, value):
            if node is None:
                return None
            if value == node.value:
                return node
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    # Remover um valor da árvore
    def delete(self, value):
        def _delete(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # Caso 1: nó folha
                if node.left is None and node.right is None:
                    return None
                # Caso 2: nó com apenas um filho
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Caso 3: nó com dois filhos
                else:
                    successor = self._min_value(node.right)
                    node.value = successor.value
                    node.right = _delete(node.right, successor.value)
            return node

        self.root = _delete(self.root, value)

    # Achar o menor valor a partir de um nó (usado na remoção)
    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Calcular a altura total da árvore
    def height(self):
        def _height(node):
            if node is None:
                return -1  # árvore vazia = -1, nó folha = 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    # Calcular a profundidade de um valor específico
    def depth(self, value):
        def _depth(node, value, level):
            if node is None:
                return -1
            if value == node.value:
                return level
            elif value < node.value:
                return _depth(node.left, value, level + 1)
            else:
                return _depth(node.right, value, level + 1)
        return _depth(self.root, value, 0)

    # Visualizar a árvore usando Graphviz
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

    bst_fixed.visualize("bst_fixed_initial")

    # Demonstração de busca
    print("Buscando valor 45:", "Encontrado" if bst_fixed.search(45) else "Não encontrado")

    # Remoção
    bst_fixed.delete(30)
    bst_fixed.visualize("bst_fixed_after_delete")

    # Nova inserção
    bst_fixed.insert(60)
    bst_fixed.visualize("bst_fixed_after_insert")

    # Altura e profundidade
    print("Altura da árvore fixa:", bst_fixed.height())
    print("Profundidade do nó 45:", bst_fixed.depth(45))

    print("\n=== Árvore Randômica ===")
    bst_random = BinarySearchTree()
    random_values = random.sample(range(1, 200), 15)  # 15 números aleatórios únicos
    print("Valores inseridos na árvore randômica:", random_values)

    for v in random_values:
        bst_random.insert(v)

    bst_random.visualize("bst_random")
    print("Altura da árvore randômica:", bst_random.height())
