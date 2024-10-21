from collections import namedtuple
import csv
from matplotlib import pyplot as plt


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    res = []
    with open(ruta_fichero,encoding="utf-8") as f:
        lector = csv.reader(f)
        for pais,codigo,año,censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            res.append(tupla)
    return res


def calcula_paises(poblaciones: list[RegistroPoblacion]):
    lista_ordenada = set()
    for e in poblaciones:
        lista_ordenada.add(e.pais)
    lista_ordenada2 = sorted(lista_ordenada)
    return lista_ordenada2

def filtrar_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo):
    lista_filtrada = []
    for e in poblaciones:
        if nombre_o_codigo in e.pais or nombre_o_codigo in e.codigo:
            tupla = (e.año,e.censo)
            lista_filtrada.append(tupla)
        
    return lista_filtrada


def filtra_por_paises_y_año(poblaciones: list[RegistroPoblacion], año: int, paises: set[str])->list[tuple]:
    lista_filtrada_año = []
    for e in poblaciones:
        if e.pais in paises and e.año == año:
            tupla = (e.pais,e.censo)
            lista_filtrada_año.append(tupla)
    return lista_filtrada_año

def muestra_evolucion_poblacion(poblaciones: list[RegistroPoblacion], nombre_o_codigo):
    titulo = nombre_o_codigo
    lista_años = []
    lista_habitantes = []
    for e in poblaciones:
        if nombre_o_codigo == e.pais or nombre_o_codigo in e.codigo:
            lista_años.append(e.año)
            lista_habitantes.append(e.censo)
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()