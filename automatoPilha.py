class AutomatoDePilha:
    def __init__(self, transicoes):
        self.transicoes = transicoes
        self.pilha = []

    def adicionar_transicao(self, estado_atual, entrada, estado_filho, simbolo_empilhar, simbolo_desempilhar):
        self.transicoes.append({
            'estado': estado_atual,
            'entrada': entrada,
            'estadoFilho': estado_filho,
            'simboloEmpilhar': simbolo_empilhar,
            'simboloDesempilhar': simbolo_desempilhar
        })

    def run(self, estado_atual, entrada, n=0):
        entrada_atual = list(entrada)
   
        print(f"Estado Atual: {estado_atual}, Entrada: {entrada_atual[n] if n < len(entrada_atual) else 'Fim'}")
        print("Estado da pilha: ", self.pilha)
        if n >= len(entrada_atual):
            if not self.pilha:
                print("\nPALAVRA ACEITA!")
            else:
                print("\nPALAVRA RECUSADA!")
            return

        for transicao in self.transicoes:
            if transicao['estado'] == estado_atual and transicao['entrada'] == entrada_atual[n]:
                estado_filho = transicao['estadoFilho']
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
                        estado_filho = "q3"

                self.run(estado_filho, entrada, n + 1)


# Exemplo de uso: escolher uma transição de "transicoes.py"
import transicoes
automato = AutomatoDePilha(transicoes.exemplo)

# Verifica se a palavra é aceita
automato.run('q0', 'aabbcccc')
