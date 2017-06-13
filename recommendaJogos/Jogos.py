class Jogos(object):
    def __init__(self, nome, a):
        self._nomeDoJogo = nome
        self._listaFeature = []
        for i in range(len(a)):
            self._listaFeature.append(float(a[i]))

    def getFeature(self, a):
        return self._listaFeature[a]

    def getNomeJogo(self):
        return self._nomeDoJogo

    def setNomeJogo(self, nome):
        self._nomeDoJogo = nome

    def getListaFeatures(self):
        return self._listaFeature