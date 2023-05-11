import math

# Función heurística para estimar la distancia a la meta
def heuristic(state):
    x, y = state
    goal_x, goal_y = (10, 5) # Coordenadas del punto de montaje A
    return math.sqrt((x - goal_x)**2 + (y - goal_y)**2)

# Función para generar los sucesores del estado actual
def successors(state):
    x, y = state
    delta_h = 0.1 # Incremento en la dirección horizontal
    # Movimiento hacia la izquierda
    new_state_left = (x - delta_h, y)
    # Movimiento hacia la derecha
    new_state_right = (x + delta_h, y)
    return [new_state_left, new_state_right]

# Algoritmo de búsqueda heurística
def search(initial_state):
    visited = set() # Conjunto de estados visitados
    queue = [(initial_state, 0)] # Cola de estados por visitar, con su valor f
    while queue:
        state, f = queue.pop(0)
        if state in visited:
            continue
        visited.add(state)
        if state == (10, 5): # Si el estado actual es la meta, retornar la secuencia de movimientos
            path = [state]
            while queue:
                parent, _ = queue.pop(0)
                if parent == path[-1]:
                    path.append(parent)
            return path
        for successor in successors(state):
            if successor not in visited:
                g = f + 1 # Costo de llegar al sucesor desde el estado actual
                h = heuristic(successor) # Estimación de la distancia a la meta
                queue.append((successor, g + h)) # Agregar el sucesor a la cola de estados por visitar
        queue.sort(key=lambda x: x[1]) # Ordenar la cola de estados por valor f
    return None # Si no se encuentra una solución, retornar None

# Ejemplo de uso
initial_state = (0, 5) # Coordenadas del punto de partida B
path = search(initial_state)
if path:
    print("Secuencia de movimientos:")
    for state in path:
        print(state)
else:
    print("No se encontró una solución.")
