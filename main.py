
class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
# Teste 1
Pilha = Pilha()
# Adicionando
Pilha.push('A')
Pilha.push('B')
Pilha.push('C')
# Verificando
print("Topo da pilha:", Pilha.peek())
# Removendo
Pilha.pop()
Pilha.pop()
Pilha.pop()

