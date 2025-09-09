# atividade_1.py
# Nome: Rafael De Freitas Fiel
# Disciplina: Estrutura de Dados II

from graphviz import Digraph
import random

# Classe que representa um nó da árvore de expressão
class Node:
    def __init__(self, value=None, operator=None, left=None, right=None):
        self.value = value       # valor numérico (folha)
        self.operator = operator # operador matemático (+, -, *)
        self.left = left         # filho à esquerda
        self.right = right       # filho à direita

    # Verifica se é nó folha
    def is_leaf(self):
        return self.operator is None


# Função para construir árvore fixa da expressão ((7 + 3) * (5 - 2))
def fixed_expression_tree():
    # Monta manualmente a árvore
    n1 = Node(value=7)
    n2 = Node(value=3)
    n3 = Node(operator="+", left=n1, right=n2)

    n4 = Node(value=5)
    n5 = Node(value=2)
    n6 = Node(operator="-", left=n4, right=n5)

    root = Node(operator="*", left=n3, right=n6)
    return root


# Função para gerar uma expressão aleatória com pelo menos 2 operadores e 3 operandos
def random_expression_tree():
    operators = ["+", "-", "*"]
    # Gerar três operandos aleatórios
    values = [Node(value=random.randint(1, 9)) for _ in range(3)]

    # Combina os dois primeiros operandos com um operador aleatório
    op1 = random.choice(operators)
    sub_tree = Node(operator=op1, left=values[0], right=values[1])

    # Combina o resultado com o terceiro operando e outro operador
    op2 = random.choice(operators)
    root = Node(operator=op2, left=sub_tree, right=values[2])

    return root


# Função para visualizar a árvore usando Graphviz
def visualize(tree, filename):
    dot = Digraph()
    dot.attr("node", shape="circle")

    def add_nodes(node, parent_id=None):
        if node is None:
            return

        # Define rótulo do nó
        label = str(node.value) if node.is_leaf() else node.operator
        node_id = str(id(node))
        dot.node(node_id, label)

        if parent_id:
            dot.edge(parent_id, node_id)

        add_nodes(node.left, node_id)
        add_nodes(node.right, node_id)

    add_nodes(tree)
    dot.render(filename, format="png", cleanup=True)
    print(f"Árvore salva como {filename}.png")


# Programa principal
if __name__ == "__main__":
    print("=== Árvore Fixa ===")
    tree_fixed = fixed_expression_tree()
    visualize(tree_fixed, "expression_fixed")

    print("\n=== Árvore Randômica ===")
    tree_random = random_expression_tree()
    visualize(tree_random, "expression_random")
