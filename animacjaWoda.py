import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ustawienia animacji
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Lista kropli
raindrops = []

# Funkcja inicjująca
def init():
    return []

# Funkcja aktualizująca animację
def update(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    # Dodaj nową kroplę z większym prawdopodobieństwem
    if np.random.rand() < 0.3:  # Zwiększona wartość dla częstszych kropli
        raindrops.append([np.random.rand() * 10, 10])
    
    # Aktualizuj pozycje kropli, zwiększając prędkość spadania
    for drop in raindrops:
        drop[1] -= 0.3  # Zwiększona wartość, aby przyspieszyć
    
    # Usuń krople, które spadły poniżej dolnej krawędzi
    raindrops[:] = [drop for drop in raindrops if drop[1] > 0]
    
    # Rysuj krople
    for drop in raindrops:
        circle = plt.Circle((drop[0], drop[1]), 0.1, color='blue', alpha=0.5)
        ax.add_artist(circle)
    
    return []

# Tworzenie animacji
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=False)
plt.show()
