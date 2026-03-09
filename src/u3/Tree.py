import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Agrega el directorio raíz al path
# from src.u3.Node import Node

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  
# from u3.Node import Node   # Importa la clase Node

from Node import Node

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
       return str(self.left.data if self.left else None) + "<-" + str(self.data) + "->" + str(self.right.data if self.right else None)
'''

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def show(self, nodo_actual, prefix="", is_left=True):
        if nodo_actual:
            self.show(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
            self.show(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)
  
    '''
    def inorder(self, node=None): # usado con parametro
         if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    '''
    
    def inorder(self, node=None): # usado sin parametro
        # Si no se pasa nodo, empezamos desde la raíz
        if node is None:
            node = self.root

        # Caso base: si el nodo es None, no hacemos nada
        if node is None:
            return

        # Recursión: izquierda -> nodo -> derecha
        if node.left:
            self.inorder(node.left)
        print(node.data, end=" ")
        if node.right:
            self.inorder(node.right)

    def search(self, node, data):  # Return True or False
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def insert(self, data): # No regresa nada
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            return node

        self.root = _insert(self.root, data)
        self.size += 1

    
    def minValueNode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
  
    def delete(self, data):
        def _delete(node, data):
            if not node:
                return None

            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                self.size -= 1
                # Node with only one child or no child
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp

                # Node with two children, get the in-order successor
                node.data = self.minValueNode(node.right).data
                node.right = _delete(node.right, node.data)

            return node     
        self.root = _delete(self.root, data)
        print("size:", self.size)
            
        

    

