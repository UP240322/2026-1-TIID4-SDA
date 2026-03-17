# pip install networkx matplotlib
# Para graphviz:
# pip install graphviz
    
from graphviz import Digraph
import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
    
    def __repr__(self, nivel=0):  # parecido a __str__, pero con nivel para indentación
        ret = "  " * nivel + str(self.valor) + "\n"
        if self.izquierdo:
            ret += self.izquierdo.__repr__(nivel + 1)
        if self.derecho:
            ret += self.derecho.__repr__(nivel + 1)
        return ret
    
    def graficarArbol(self, nodo_actual, prefix="", is_left=True):
        if nodo_actual is not None:
            self.graficarArbol(nodo_actual.derecho, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.valor))
            self.graficarArbol(nodo_actual.izquierdo, prefix + ("    " if is_left else "│   "), True)

    # a + b - c * d - e / f + g - h
    def inorder(self, node):
        if node:
            self.inorder(node.izquierdo)
            print(node.valor, end=' ')
            self.inorder(node.derecho)

    def inorder2(self, node):
        if node is None:
            return []
        return (
            self.inorder2(node.izquierdo) +
            [str(node.valor)] +
            self.inorder2(node.derecho)
        )
    

# Función para visualizar el árbol usando Graphviz

def visualizar_arbol_graphviz(nodo, dot=None, parent=None, contador=[0]):
    if dot is None:
        dot = Digraph(comment='Árbol de Expresión')
        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

    if nodo is not None:
        # ID único para cada nodo
        nodo_id = f"n{contador[0]}"
        contador[0] += 1
        
        # Color diferente para operadores y operandos
        if nodo.valor in ['+', '-', '*', '/']:
            dot.node(nodo_id, nodo.valor, fillcolor='lightcoral')
        else:
            dot.node(nodo_id, nodo.valor, fillcolor='lightgreen')
        
        if parent is not None:
            dot.edge(parent, nodo_id)
        
        visualizar_arbol_graphviz(nodo.izquierdo, dot, nodo_id, contador)
        visualizar_arbol_graphviz(nodo.derecho, dot, nodo_id, contador)
    
    return dot

# Función para convertir el árbol a un grafo de NetworkX
def arbol_a_grafo(nodo, G=None, pos=None, x=0, y=0, layer=1, parent=None, contador=[0]):
    if G is None:
        G = nx.DiGraph()
        pos = {}
    
    if nodo is not None:
        # Crear un ID único para cada nodo
        nodo_id = f"{nodo.valor}_{contador[0]}"
        contador[0] += 1
        
        G.add_node(nodo_id, label=nodo.valor)
        pos[nodo_id] = (x, y)
        
        if parent is not None:
            G.add_edge(parent, nodo_id)
        
        # Calcular posiciones para los hijos
        dx = 1.5 / layer  # Espaciado horizontal que disminuye con la profundidad
        
        if nodo.izquierdo:
            arbol_a_grafo(nodo.izquierdo, G, pos, x - dx, y - 1, layer + 1, nodo_id, contador)
        
        if nodo.derecho:
            arbol_a_grafo(nodo.derecho, G, pos, x + dx, y - 1, layer + 1, nodo_id, contador)
    
    return G, pos



# Construcción del árbol para: [a+(b-c)]*[(d-e)/(f+g-h)]
# Raíz: multiplicación
raiz = Nodo('*')

# Subárbol izquierdo: a+(b-c)
raiz.izquierdo = Nodo('+')
raiz.izquierdo.izquierdo = Nodo('a')
raiz.izquierdo.derecho = Nodo('-')
raiz.izquierdo.derecho.izquierdo = Nodo('b')
raiz.izquierdo.derecho.derecho = Nodo('c')

# Subárbol derecho: (d-e)/(f+g-h)
raiz.derecho = Nodo('/')
raiz.derecho.izquierdo = Nodo('-')
raiz.derecho.izquierdo.izquierdo = Nodo('d')
raiz.derecho.izquierdo.derecho = Nodo('e')

# f+g-h se evalúa de izquierda a derecha
raiz.derecho.derecho = Nodo('-')
raiz.derecho.derecho.izquierdo = Nodo('+')
raiz.derecho.derecho.izquierdo.izquierdo = Nodo('f')
raiz.derecho.derecho.izquierdo.derecho = Nodo('g')
raiz.derecho.derecho.derecho = Nodo('h')

# Visualizar el árbol
print(raiz)

raiz.graficarArbol(raiz)

raiz.inorder(raiz)
print()

resultado = " ".join(raiz.inorder2(raiz))
print("\nRecorrido inorder:", resultado)

# Guarda y abre la imagen del árbol O para ver en Jupyter: # dot
dot = visualizar_arbol_graphviz(raiz)
dot.render('arbol_expresionG', format='png', view=True)
print("Imagen guardada como 'arbol_expresionG.png'")

# ---------------------------------------------------------------------------------------------------------
# Visualización con NetworkX y Matplotlib
# Crear el grafo
G, pos = arbol_a_grafo(raiz)
# Obtener etiquetas de los nodos
labels = nx.get_node_attributes(G, 'label')

# Dibujar el grafo
plt.figure(figsize=(10, 6))   # 12,8    10, 6
nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=False)
'''
nx.draw(G, pos, labels=labels, with_labels=True, 
        node_color='lightblue', 
        node_size=2000, 
        font_size=14, 
        font_weight='bold',
        arrows=True,
        arrowsize=20,
        edge_color='gray',
        arrowstyle='->')
'''
# plt.gca().invert_yaxis()  # Invertir el eje y para que la raíz esté arriba
plt.title("Árbol de Expresión: [a+(b-c)]*[(d-e)/(f+g-h)]", fontsize=16)
plt.axis('off')

# GUARDAR LA IMAGEN
plt.savefig('arbol_expresionN.png', dpi=300, bbox_inches='tight')
print("Imagen guardada como 'arbol_expresionN.png'")

# Si estás en Jupyter, usa:
plt.show()

