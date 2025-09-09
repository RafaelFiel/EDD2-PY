# atividade_4.py
# Nome: Rafael De Freitas Fiel
# Disciplina: Estrutura de Dados II

from graphviz import Digraph
import random

# -----------------------------
# Nó da AVL (guarda valor, filhos e altura)
# -----------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # filho esquerdo
        self.right = None  # filho direito
        self.height = 0    # altura do nó (folha = 0)

# -----------------------------
# Classe da Árvore AVL
# -----------------------------
class AVLTree:
    def __init__(self):
        self.root = None

    # --------- Utilitários de altura e balanceamento ---------
    # Retorna a altura de um nó (ou -1 se None)
    def _height(self, node):
        return node.height if node is not None else -1

    # Atualiza a altura de um nó a partir das alturas dos filhos
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # Fator de balanceamento = altura(esquerda) - altura(direita)
    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    # --------- Rotações ---------
    # Rotação simples à direita (Right Rotate) — corrige caso LL
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Executa rotação
        x.right = y
        y.left = T2

        # Atualiza alturas
        self._update_height(y)
        self._update_height(x)

        return x

    # Rotação simples à esquerda (Left Rotate) — corrige caso RR
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Executa rotação
        y.left = x
        x.right = T2

        # Atualiza alturas
        self._update_height(x)
        self._update_height(y)

        return y

    # --------- Inserção com rebalanceamento ---------
    def insert(self, value):
        """Insere e reequilibra a árvore (mantendo propriedades de BST + AVL)."""
        def _insert(node, value):
            # Inserção padrão de BST
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            else:
                # Valores iguais: aqui optamos por ignorar (evita duplicados)
                return node

            # Atualiza altura deste nó
            self._update_height(node)

            # Calcula fator de balanceamento
            bf = self._balance_factor(node)

            # Casos de desbalanceamento:
            # 1) LL: pesado à esquerda e value < node.left.value
            if bf > 1 and value < node.left.value:
                return self._rotate_right(node)

            # 2) RR: pesado à direita e value > node.right.value
            if bf < -1 and value > node.right.value:
                return self._rotate_left(node)

            # 3) LR: pesado à esquerda, mas value > node.left.value
            if bf > 1 and value > node.left.value:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            # 4) RL: pesado à direita, mas value < node.right.value
            if bf < -1 and value < node.right.value:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            # Sem desbalanceamento
            return node

        self.root = _insert(self.root, value)

    # --------- Visualização com Graphviz ---------
    def visualize(self, filename):
        """Gera imagem .png da árvore com valores e alturas."""
        dot = Digraph()
        dot.attr("node", shape="circle")

        def add_nodes(node):
            if node is None:
                return
            # rótulo inclui valor e altura (para evidenciar balanceamento)
            label = f"{node.value}\n(h={node.height})"
            dot.node(str(id(node)), label)
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes(node.right)

        add_nodes(self.root)
        dot.render(filename, format="png", cleanup=True)
        print(f"Árvore salva como {filename}.png")

    # --------- (Opcional) Verificações simples ---------
    def is_balanced(self):
        """Verifica se todos os nós respeitam |bf| <= 1 (AVL válida)."""
        ok = True
        def _check(node):
            nonlocal ok
            if node is None:
                return
            bf = self._balance_factor(node)
            if abs(bf) > 1:
                ok = False
                return
            _check(node.left)
            _check(node.right)
        _check(self.root)
        return ok

    def inorder(self):
        """Retorna a lista de valores em ordem (para checar propriedade de BST)."""
        out = []
        def _in(node):
            if node is None: return
            _in(node.left)
            out.append(node.value)
            _in(node.right)
        _in(self.root)
        return out


# -----------------------------
# Demonstrações solicitadas
# -----------------------------
if __name__ == "__main__":
    # --------- Caso 1: Sequência que força rotação simples ---------
    print("=== AVL com sequência [10, 20, 30] (deve ocorrer rotação simples) ===")
    avl_simple = AVLTree()
    seq_simple = [10, 20, 30]
    for i, val in enumerate(seq_simple, start=1):
        avl_simple.insert(val)
        avl_simple.visualize(f"avl_simple_step_{i}")  # salva após cada inserção
    print("Ordem (inorder):", avl_simple.inorder())
    print("Balanceada?", avl_simple.is_balanced())

    # --------- Caso 2: Sequência que força rotação dupla ---------
    print("\n=== AVL com sequência [10, 30, 20] (deve ocorrer rotação dupla) ===")
    avl_double = AVLTree()
    seq_double = [10, 30, 20]
    for i, val in enumerate(seq_double, start=1):
        avl_double.insert(val)
        avl_double.visualize(f"avl_double_step_{i}")  # salva após cada inserção
    print("Ordem (inorder):", avl_double.inorder())
    print("Balanceada?", avl_double.is_balanced())

    # --------- Caso 3: Árvore com valores randômicos ---------
    print("\n=== AVL com 20 valores randômicos ===")
    avl_random = AVLTree()
    random_values = random.sample(range(1, 300), 20)  # 20 números únicos
    print("Valores inseridos:", random_values)
    for v in random_values:
        avl_random.insert(v)

    avl_random.visualize("avl_random_final")
    print("Ordem (inorder):", avl_random.inorder())
    print("Balanceada?", avl_random.is_balanced())
