class Jogos(object):
    gameplay = 0
    narrativa = 0
    esporte = 0
    acao = 0


    def __init__(self, nome, f1, f2,f3,f4):
        self._nomeDoJogo = nome
        self._gameplay = f1
        self._narrativa = f2
        self._esporte = f3
        self._acao = f4


    def getGameplayVal(self):
        return self._gameplay

    def getNarrativaVal(self):
        return self._narrativa

    def getEsporteVal(self):
        return self._narrativa

    def getAcaoVal(self):
        return self._esporte

    def getNomeJogo(self):
        return self._nomeDoJogo

    def setNomeJogo(self, nome):
        self._nomeDoJogo = nome
