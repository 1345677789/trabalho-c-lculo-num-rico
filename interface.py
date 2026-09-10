def ler_float(mensagem):
    """Lê um número real e trata entradas inválidas."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_int(mensagem, minimo=1):
    """Lê um número inteiro maior ou igual ao mínimo."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def mostrar_tabela(resultado):
    """Mostra o passo a passo armazenado no histórico."""
    print(f"\n--- PASSO A PASSO: {resultado.metodo.upper()} ---")

    if not resultado.historico:
        print(resultado.mensagem)
        return

    if resultado.metodo == "Bisseção":
        print("Iter |       a |       b |       x |      f(a) |      f(x) | Erro relativo")
        for r in resultado.historico:
            erro = "-" if r["erro_relativo"] is None else f'{r["erro_relativo"]:.8e}'
            print(f'{r["iteracao"]:>4} | {r["a"]:>7.5f} | {r["b"]:>7.5f} | '
                  f'{r["x"]:>7.5f} | {r["f(a)"]:>9.5f} | {r["f(x)"]:>9.5f} | {erro}')
    else:
        print("Iter |      x_n |    f(x_n) |   f'(x_n) |    x_novo | Erro relativo")
        for r in resultado.historico:
            print(f'{r["iteracao"]:>4} | {r["x_n"]:>8.5f} | {r["f(x_n)"]:>9.5f} | '
                  f'{r["f\'(x_n)"]:>9.5f} | {r["x_novo"]:>9.5f} | {r["erro_relativo"]:.8e}')


def mostrar_resultado(resultado):
    print(f"\nMétodo: {resultado.metodo}")
    print(f"Status: {resultado.mensagem}")
    if resultado.raiz is not None:
        print(f"Valor aproximado de d: {resultado.raiz:.10f}")
    if resultado.erro is not None:
        print(f"Erro relativo: {resultado.erro:.10e}")
    print(f"Iterações: {resultado.iteracoes}")
