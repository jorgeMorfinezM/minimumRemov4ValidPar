# -*- coding: utf-8 -*-

"""
This problem was recently asked by Uber:

You are given a string of parenthesis.
Return the minimum number of parenthesis
that would need to be removed in order
to make the string valid. "Valid" means
that each open parenthesis has a matching
closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("
"""


def count_invalid_parenthesis(string_val):
    list_item_string = list(string_val)

    pila = []

    index_par_open = 0
    index_par_close = 0

    numero_par_open = list_item_string.count('(')
    numero_par_close = list_item_string.count(')')

    list_indexes_open = []
    list_indexes_close = []

    stack_add_par = []

    parentesis_invalidos = 0

    if numero_par_open != numero_par_close:
        print("Los parentesis no estan bien balanceados")
        if numero_par_close > numero_par_open:
            parentesis_invalidos = numero_par_close - numero_par_open
        elif numero_par_open > numero_par_close:
            parentesis_invalidos = numero_par_open - numero_par_close
    else:
        for valor in list_item_string:
            if valor == '(':
                pila.append(valor)
            elif valor == ')' and len(pila) > 0:
                pila.pop()

            parentesis_invalidos += pila.count(valor)

        # AGREGAR validacion para llenar los parentesis

    print("Valor de la pila: ", pila)
    print("Valor de par open: ", numero_par_open)
    print("Valor de par close: ", numero_par_close)
    print("List_Indexes open: ", list_indexes_open)
    print("List_Indexes close: ", list_indexes_close)

    # if len(pila) == 0:
    #     print("Parentesis bien balanceados")

    return parentesis_invalidos


if __name__ == "__main__":
    print("Numero de parentesis diferentes: ", count_invalid_parenthesis("()("))
