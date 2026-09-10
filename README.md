# Trabalho de Cálculo Numérico – Tema 2

## Objetivo

Implementar, em Python e utilizando Programação Orientada a Objetos, métodos numéricos para encontrar o deslocamento `d` do movimento físico definido pela função:

**f(d) = a * e^d - 4*d²**

## Métodos utilizados

- Método da Bisseção;
- Método de Newton-Raphson;
- Cálculo do erro relativo.

## Entradas

O programa recebe:

- Número de movimentos `n`;
- Valor de `a` para cada movimento;
- Intervalo de isolamento;
- Precisão `ε`.

## Saídas

Para cada movimento, o programa apresenta:

- Intervalo de isolamento;
- Resultado obtido pelo método da Bisseção;
- Resultado obtido pelo método de Newton-Raphson;
- Erro relativo;
- Número de iterações;
- Histórico das iterações.

## Teste padrão

Para o teste padrão definido no enunciado:

- `a = 1`
- Isolamento = `(0, 1)`
- `ε = 10^-4`

## Organização do projeto

```text
trabalho_tema2/
│
├── main.py
├── movimento.py
├── metodos.py
├── analise.py
├── interface.py
├── README.md
└── diagrams/
    └── diagrama_classes.md
    
## Autores

- Emerson
- Delmara
