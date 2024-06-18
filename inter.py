import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def encontrar_interseccoes(y1_, y2_, num_pontos=10, num_interpolacoes=1000, tol=1e-5):
    y1 = np.array(y1_)
    y2 = np.array(y2_)
    x = np.linspace(0, num_pontos - 1, num_pontos)

    # Funções de interpolação linear
    f1 = interp1d(x, y1, kind='linear')
    f2 = interp1d(x, y2, kind='linear')

    # Encontrar os pontos de intersecção
    x_new = np.linspace(0, num_pontos - 1, num_interpolacoes)  # Mais pontos para maior precisão
    y1_new = f1(x_new)
    y2_new = f2(x_new)

    # Encontrar os pontos onde as funções se cruzam
    idx = np.where(np.isclose(y1_new, y2_new, atol=tol))[0]

    y_intersections = y1_new[idx]
    
    return y_intersections
