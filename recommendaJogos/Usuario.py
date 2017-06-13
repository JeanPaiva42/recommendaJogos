class Usuario(object):


    def __init__(self, nome):
        self._nome = nome
        self._listaJogos = {}
        self._somaPref = []



    def getNome(self):
        return self._nome

    def adicionaJogo(self, nome, nota):
        self._listaJogos[nome.upper()] = nota

    def removeJogo(self, nome):
        del self._listaJogos[nome.upper()]

    def getJogos(self):
        return self._listaJogos

    def getNota(self, nome):
        return self._listaJogos[nome.upper()]

    def printaJogos(self):
        for keys in self._listaJogos.iterkeys():
            print keys

    def printaJogosENotas(self):
        for keys, valor in self._listaJogos.iteritems():
            print keys, valor

    def calculaPreferencias(self, a):
        for i in range(len(a)):
            self._somaPref.append(a[i])

    def getPreferencias(self):
        return self._somaPref


