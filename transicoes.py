# Linguagem programada (a^n b^m c^n+m)
exemplo = [
    {'estado': 'q0', 'entrada': 'a', 'estadoFilho': 'q0', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estado': 'q0', 'entrada': 'b', 'estadoFilho': 'q1', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estado': 'q1', 'entrada': 'b', 'estadoFilho': 'q1', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estado': 'q1', 'entrada': 'c', 'estadoFilho': 'q2', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
    {'estado': 'q2', 'entrada': 'c', 'estadoFilho': 'q2', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
]

duploBalanceamento = [
    {'estado': 'q0', 'entrada': 'a', 'estadoFilho': 'q0', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estado': 'q0', 'entrada': 'b', 'estadoFilho': 'q1', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
    {'estado': 'q1', 'entrada': 'b', 'estadoFilho': 'q1', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
]