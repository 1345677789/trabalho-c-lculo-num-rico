class ResultadoMetodo:
    """Guarda o resultado final e o histórico de um método numérico."""

    def __init__(self, metodo, raiz=None, erro=None, iteracoes=0,
                 historico=None, convergiu=False, mensagem=""):
        self.metodo = metodo
        self.raiz = raiz
        self.erro = erro
        self.iteracoes = iteracoes
        self.historico = historico if historico is not None else []
        self.convergiu = convergiu
        self.mensagem = mensagem


class MetodoBissecao:
    """Implementação própria do método da Bisseção."""

    def resolver(self, movimento, a, b, epsilon, max_iter=100):
        fa = movimento.f(a)
        fb = movimento.f(b)

        # O método exige mudança de sinal no intervalo.
        if fa * fb > 0:
            return ResultadoMetodo(
                "Bisseção", mensagem="Não há mudança de sinal no intervalo.",
                historico=[], convergiu=False
            )

        historico = []
        x_anterior = None

        for i in range(1, max_iter + 1):
            x = (a + b) / 2
            fx = movimento.f(x)

            # Tema 2 pede erro relativo.
            erro = None if x_anterior is None else abs((x - x_anterior) / x) if x != 0 else abs(x - x_anterior)

            historico.append({
                "iteracao": i, "a": a, "b": b, "x": x,
                "f(a)": fa, "f(x)": fx, "erro_relativo": erro
            })

            if fx == 0 or (erro is not None and erro < epsilon):
                return ResultadoMetodo("Bisseção", x, erro, i, historico, True,
                                       "Convergência atingida.")

            # Mantém o subintervalo que continua contendo mudança de sinal.
            if fa * fx < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx

            x_anterior = x

        return ResultadoMetodo("Bisseção", x, erro, max_iter, historico, False,
                               "Número máximo de iterações atingido.")


class MetodoNewtonRaphson:
    """Implementação própria do método de Newton-Raphson."""

    def resolver(self, movimento, x0, epsilon, max_iter=100):
        historico = []
        x = x0

        for i in range(1, max_iter + 1):
            fx = movimento.f(x)
            dfx = movimento.df(x)

            # Evita divisão por zero ou valores extremamente pequenos.
            if abs(dfx) < 1e-14:
                return ResultadoMetodo(
                    "Newton-Raphson", x, None, i - 1, historico, False,
                    "Derivada igual ou muito próxima de zero."
                )

            x_novo = x - fx / dfx
            erro = abs((x_novo - x) / x_novo) if x_novo != 0 else abs(x_novo - x)

            historico.append({
                "iteracao": i, "x_n": x, "f(x_n)": fx,
                "f'(x_n)": dfx, "x_novo": x_novo,
                "erro_relativo": erro
            })

            if erro < epsilon or abs(movimento.f(x_novo)) < epsilon:
                return ResultadoMetodo("Newton-Raphson", x_novo, erro, i,
                                       historico, True, "Convergência atingida.")

            x = x_novo

        return ResultadoMetodo("Newton-Raphson", x, erro, max_iter, historico,
                               False, "Número máximo de iterações atingido.")
