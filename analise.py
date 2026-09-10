class AnalisadorMovimentos:
    """Coordena os métodos e analisa a existência de raízes."""

    def __init__(self, bissecao, newton):
        self.bissecao = bissecao
        self.newton = newton

    def executar(self, movimento, inicio, fim, epsilon):
        # O ponto médio do isolamento é usado como chute inicial do Newton.
        chute_inicial = (inicio + fim) / 2

        resultado_bissecao = self.bissecao.resolver(
            movimento, inicio, fim, epsilon
        )
        resultado_newton = self.newton.resolver(
            movimento, chute_inicial, epsilon
        )

        return resultado_bissecao, resultado_newton

    def existe_deslocamento_no_intervalo(self, movimento, inicio, fim):
        """
        Verifica se há isolamento por mudança de sinal no intervalo informado.
        É uma análise numérica do intervalo escolhido.
        """
        return movimento.f(inicio) * movimento.f(fim) <= 0
