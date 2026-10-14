import time


def torre_hanoi(n, origen, auxiliar, destino):
    """Resuelve recursivamente la Torre de Hanoi."""
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    torre_hanoi(n - 1, origen, destino, auxiliar)
    print(f"Mover disco {n} de {origen} a {destino}")
    torre_hanoi(n - 1, auxiliar, origen, destino)


def contar_movimientos(n):
    return 2**n - 1


def medir_tiempo(discos):
    inicio = time.perf_counter()

    movimientos = contar_movimientos(discos)

    fin = time.perf_counter()
    tiempo = fin - inicio

    print(f"Discos: {discos}")
    print(f"Movimientos necesarios: {movimientos:,}")
    print(f"Tiempo de cálculo: {tiempo:.8f} segundos")
    print("-" * 40)


def main():
    cantidades = [5, 10, 30, 64]

    for discos in cantidades:
        medir_tiempo(discos)


if __name__ == "__main__":
    main()
