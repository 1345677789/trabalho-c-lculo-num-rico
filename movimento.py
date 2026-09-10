import math

class MovimentoFisico:
    """
    Representa o problema físico do Tema 2.

    Por padrão:
        f(d) = a * e^d - 4*d²
        f'(d) = a * e^d - 8*d

    As funções podem ser alteradas facilmente na apresentação.
    """

    def __init__(self, a, funcao=None, derivada=None):
        self.a = float(a)
        self.funcao_personalizada = funcao
        self.derivada_personalizada = derivada

    def f(self, d):
        if self.funcao_personalizada is not None:
            return self.funcao_personalizada(self.a, d)
        return self.a * math.exp(d) - 4 * d**2

    def df(self, d):
        if self.derivada_personalizada is not None:
            return self.derivada_personalizada(self.a, d)
        return self.a * math.exp(d) - 8 * d
