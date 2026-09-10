from movimento import MovimentoFisico
from metodos import MetodoBissecao, MetodoNewtonRaphson
from analise import AnalisadorMovimentos
from interface import ler_float, ler_int, mostrar_resultado, mostrar_tabela


def main():
    print("=" * 60)
    print("TRABALHO DE CÁLCULO NUMÉRICO - TEMA 2")
    print("f(d) = a * e^d - 4*d²")
    print("Métodos: Bisseção e Newton-Raphson")
    print("=" * 60)

    n = ler_int("\nDigite o número de movimentos: ")
    epsilon = ler_float("Digite a precisão (ex.: 0.0001): ")

    inicio = ler_float("Digite o início do intervalo de isolamento: ")
    fim = ler_float("Digite o fim do intervalo de isolamento: ")

    while inicio >= fim:
        print("O início deve ser menor que o fim.")
        inicio = ler_float("Digite o início do intervalo: ")
        fim = ler_float("Digite o fim do intervalo: ")

    analisador = AnalisadorMovimentos(MetodoBissecao(), MetodoNewtonRaphson())

    for numero in range(1, n + 1):
        print("\n" + "=" * 60)
        print(f"MOVIMENTO {numero}")
        print("=" * 60)

        amplitude = ler_float(f"Digite o valor de a do movimento {numero}: ")
        movimento = MovimentoFisico(amplitude)

        print(f"\nf(d) = {amplitude} * e^d - 4*d²")
        print(f"Intervalo informado: ({inicio}, {fim})")

        if analisador.existe_deslocamento_no_intervalo(movimento, inicio, fim):
            print("Há mudança de sinal no intervalo: existe uma raiz isolada para a Bisseção.")
        else:
            print("Não há mudança de sinal no intervalo informado.")
            print("A Bisseção não pode garantir uma raiz nesse isolamento.")

        bissecao, newton = analisador.executar(
            movimento, inicio, fim, epsilon
        )

        mostrar_resultado(bissecao)
        mostrar_resultado(newton)

        opcao = input("\nDeseja mostrar as tabelas do passo a passo? (s/n): ").strip().lower()
        if opcao == "s":
            mostrar_tabela(bissecao)
            mostrar_tabela(newton)

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
