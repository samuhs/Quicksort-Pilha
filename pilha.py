class Pilha:

    def __init__(self):
        self.pilha= []
    def vazia(self):
        return self.pilha == []
    def topo(self):
        return self.pilha[len(self.pilha) - 1]
    def push(self,x):
        self.pilha.append(x)
    def pop_pilha(self):
        return self.pilha.pop()
    def pilha_nao_vazia (self):
        if self.pilha == []:
            return False
        else:
            return True
