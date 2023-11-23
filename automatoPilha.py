class AutomatoDePilha:
    def __init__(self, transicoes):
        self.transicoes = transicoes
        self.pilha = []

    def adicionar_transicao(self, estado_atual, entrada, novo_estado, simbolo_empilhar, simbolo_desempilhar):
        self.transicoes.append({
            'estadoAtual': estado_atual,
            'entrada': entrada,
            'novoEstado': novo_estado,
            'simboloEmpilhar': simbolo_empilhar,
            'simboloDesempilhar': simbolo_desempilhar
        })

    def run(self, estado_atual, entrada, n=0):
        entrada_atual = list(entrada)
   
        print(f"Estado Atual: {estado_atual}, Entrada: {entrada_atual[n] if n < len(entrada_atual) else 'Fim'}")
        print(self.pilha)
        if n >= len(entrada_atual):
            if not self.pilha:
                print("\nPALAVRA ACEITA!")
            else:
                print("\nPALAVRA RECUSADA!")
            return

        for transicao in self.transicoes:
            if transicao['estadoAtual'] == estado_atual and transicao['entrada'] == entrada_atual[n]:
                novo_estado = transicao['novoEstado']
                simbolo_empilhar = transicao['simboloEmpilhar']
                simbolo_desempilhar = transicao['simboloDesempilhar']

                if simbolo_empilhar != '':
                    self.pilha.append(simbolo_empilhar)

                if simbolo_desempilhar != '':
                    if not self.pilha:
                        self.pilha.append('X')
                    else:
                        self.pilha.pop()

                if n + 1 >= len(entrada_atual):
                    if not self.pilha:
                        novo_estado = "q3"

                self.run(novo_estado, entrada, n + 1)

# Linguagem programada (a^n b^m c^n+m)
# Exemplo de uso:
transicoes = [
    {'estadoAtual': 'q0', 'entrada': 'a', 'novoEstado': 'q0', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estadoAtual': 'q0', 'entrada': 'b', 'novoEstado': 'q1', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estadoAtual': 'q1', 'entrada': 'b', 'novoEstado': 'q1', 'simboloEmpilhar': 'X', 'simboloDesempilhar': ''},
    {'estadoAtual': 'q1', 'entrada': 'c', 'novoEstado': 'q2', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
    {'estadoAtual': 'q2', 'entrada': 'c', 'novoEstado': 'q2', 'simboloEmpilhar': '', 'simboloDesempilhar': 'X'},
]

automato = AutomatoDePilha(transicoes)

# Inicia a busca em profundidade a partir do estado inicial 'q0' e entrada 'abc'
automato.run('q0', 'aabbcccc')
