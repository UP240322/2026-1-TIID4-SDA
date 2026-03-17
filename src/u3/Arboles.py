# AVL Georgy Adelson-Velsky and Evgenii Landis
# AVL trees are self-balancing
import os
from graphviz import Digraph

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data, end=", ")
    inOrder(node.right)

def inOrderList(node) -> list: # iNd a+b
    if node is None:
        return []
    return inOrderList(node.left) + [node.data] + inOrderList(node.right)

# BFS Breadth-First Search
# regresa una lista de listas, cada sublista representa un nivel del árbol
def niveles_BFS(node) -> list:
    niveles = []
    queue = [node]
    while queue:
        nivel = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node:
                nivel.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        if nivel:
            niveles.append(nivel)

    return niveles

def showTree(nodo_actual, prefix="", is_left=True):
    def _showTree(nodo_actual, prefix="", is_left=True):
        if nodo_actual is not None:
            _showTree(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
            _showTree(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)
    print()        
    _showTree(nodo_actual, prefix="", is_left=True)
    print()        

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print('Rotate right on node',y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    print('Rotate left on node',x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def balancear(node) -> TreeNode:
    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right Left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def insert(node, data): 
    if not node:
        return TreeNode(data)

    if data < node.data:   # <= permitir duplicados, < no permitir duplicados
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    node = balancear(node) # activar si deseo balancear
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data) -> TreeNode:
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node:
        node = balancear(node)
    return node
 
def tree_graphviz(nodo, dot=None, parent=None, contador=[0]):
    if dot is None:
        dot = Digraph(comment='Árbol de Expresión')
        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

    if nodo is not None:
        # ID único para cada nodo
        nodo_id = f"n{contador[0]}"
        contador[0] += 1
        nodo_label = str(nodo.data)
        
        # Color diferente para operadores y operandos
        if nodo.data in ['+', '-', '*', '/']:
            dot.node(nodo_id, nodo_label, fillcolor='lightcoral')
        else:
            dot.node(nodo_id, nodo_label, fillcolor='lightgreen')
        
        if parent is not None:
            dot.edge(parent, nodo_id)
        
        tree_graphviz(nodo.left, dot, nodo_id, contador)
        tree_graphviz(nodo.right, dot, nodo_id, contador)
      
    return dot      

def main():
    letters = 'murcielagas'
    letters = 'zapata_maldonado'
    #letters = [7, 3, 13, 19, 8, 14, 15, 18, 8, 19]

    root = None
    for letter in letters:
        root = insert(root, letter) # insertAVL o insertar o insert

    showTree(root)
    inOrder(root)
    print()
    
    arreglo = inOrderList(root)
    print("In-orderList:", arreglo)
        
    print("---Niveles---")
    niveles = niveles_BFS(root)
    print(niveles)
    
    # Guarda y abre la imagen del árbol O para ver en Jupyter: # dot
    dot = tree_graphviz(root)
    dot.render("arbol", format="png", cleanup=True, view=True)

    '''
    print('\nDeleting 8')
    root = delete(root, 8)
    root = delete(root, 19)
    root = delete(root, 15)
    showTree(root)
    inOrderTraversal(root)
    '''
   
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    print(". . . Hecho.") 

  




