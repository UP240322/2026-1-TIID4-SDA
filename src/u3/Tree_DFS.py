# DFS Depth First Search = Busqueda en profundidad
# arbol en profundidad: preorden, inorden y postorden.
import os

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
       return str(self.left.data if self.left else None) + "<-" + str(self.data) + "->" + str(self.right.data if self.right else None)
    
def showTree(nodo_actual, prefix="", is_left=True):
    def _showTree(nodo_actual, prefix="", is_left=True):
        if nodo_actual is not None:
            _showTree(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
            _showTree(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)
    _showTree(nodo_actual, prefix="", is_left=True)
    print()        

def preOrder(node): # Nid +ab
    if node: 
        print(node.data, end=", ")
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node): # iNd  a+b
    if node:
        inOrder(node.left)
        print(node.data, end=", ")
        inOrder(node.right)

def postOrder(node): # idN ab+
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end=", ")

def inOrderArray(node): # iNd a+b
    global array
    if node:
        inOrderArray(node.left)
        array.append(node.data)
        inOrderArray(node.right)

def inOrderStr(node): # iNd a+b
    if node is None:
        return []
    return inOrderStr(node.left) + [str(node.data)] + inOrderStr(node.right)

def main():
    root = TreeNode(13)
    node7 = TreeNode(7)
    node15 = TreeNode(15)
    node3 = TreeNode(3)
    node8 = TreeNode(8)
    node14 = TreeNode(14)
    node19 = TreeNode(19)
    node18 = TreeNode(18)

    root.left = node7
    root.right = node15

    node7.left = node3
    node7.right = node8

    node15.left = node14
    node15.right = node19

    node19.left = node18

    # Test
    print("Nodo:", root)
    
    
    print("root.right.left.data:", root.right.left.data)
    showTree(root)
    # Traverse
    inOrder(root)

    inOrderArray(root)
    print("\nArray:", array)
    
    cadena = " ".join(inOrderStr(root))
    print("\nCadena:", cadena)

if __name__ == "__main__":
    os.system("cls")
    array=[]
    main()
    print()
    os.system("pause")
