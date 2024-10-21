from poblacion import *

def imprimir(lista):
    for e in lista:
        print("\t",e)

def test_lee_poblaciones(datos):
    print(f"Se han leido {len(datos)} datos")
    print("Primeros 3 datos:")
    imprimir(datos[0:3])
    print("Ultimos 3 datos:")
    imprimir(datos[-3:])

def test_calcula_paises(datos):
    print("La lista ordenada de los paises es:", calcula_paises(datos))

def test_filtrar(datos):
    print("Los datos y años del pais indicado son:", filtrar_por_pais(datos,"ZWE"))

def test_año(datos):
    print("La lista filtrada por paises y años es:", filtra_por_paises_y_año(datos,1970,["Zambia","Zimbabwe"]))

if __name__ == "__main__":
    datos = lee_poblaciones("data/population.csv")
    #test_lee_poblaciones(datos)
    #test_calcula_paises(datos)
    #test_filtrar(datos)
    #test_año(datos)

    muestra_evolucion_poblacion(datos,"ZWE")