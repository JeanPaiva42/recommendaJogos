from numpy import *
import numpy as np

numJogos = 10
numUsuarios = 5


#criando uma matriz que vai guardar valores aleatorios que sao as notas dos jogos de cada usuario

notas = random.randint(11, size=(numJogos, numUsuarios))

#print notas


'''se a nota de um usuario para um jogo for igual a zero isso significa que esse jogo nao
foi avaliado pelo usuario em questao. 5 colunas representando os usuarios, 10 linhas repreentando o numero de jogos'''

deuNota = (notas!= 0 ) * 1

print deuNota

#zerando a primeira coluna da matriz para como se eu nao tivesse avaliado nenhum jogo
notasJean = zeros((numJogos, 1))


#vou avaliar alguns jogos

notasJean[0] = 9
notasJean[5] = 6
notasJean[9] = 10

print notasJean
#deletando a primeira coluna
notas = np.delete(notas, [0,0], axis=1)

#readicionando minhas notas na primeira coluna

notas = append(notasJean, notas, axis=1)
deuNota = (notas!= 0 ) * 1

print notas

print deuNota


#funcao que normaliza os dados, precisamos dela para ficar mais facil identificar elementos acima da media e abaixo.
# val - media = normalizo

def normalizaNotas(notas, deuNota):
    numJogos = notas.shape[0]

    notasMedia = zeros(shape = (numJogos,1))
    notasNorma = zeros(shape = notas.shape)

    for i in range(numJogos):
        #pegando todos os elementos onde tem um 1
        idx = where(deuNota[i]==1)[0]
        #calcula media das notas dos usuarios que deram nota, ou seja != 0
        notasMedia[i] = mean(notas[i, idx])
        notasNorma[i, idx] = notas[i, idx] - notasMedia[i]

    return notasNorma, notasMedia

notas, notasMedia = normalizaNotas(notas, deuNota)
#features dos jogos, como por exemplo elementos que o distingue e tal

numFeatures = 3

jogoFeatures = random.randn(numJogos, numFeatures)

usuarioPref = random.randn(numUsuarios, numFeatures)
#a ideia do nome dessa variavel vem da formula de uma regressao linar, ainda nao compreendo totalmente o conceito
xInicialEteta = r_[jogoFeatures.T.flatten(), usuarioPref.T.flatten()]


# as 3 proximas funcoes nao foram desenvolvidas por mim

def unroll_params(xInicialEteta, numUsuarios, numJogos, numFeatures):
    # Retorna as matrizes x e o teta do xInicialEteta, baseado nas suas dimensoes (numFeatures, numJogos, numJogos)
    # --------------------------------------------------------------------------------------------------------------
    # Pega as primeiras 30 (10 * 3) linhas in the 48 X 1 vetor coluna
    first_30 = xInicialEteta[:numJogos * numFeatures]
    # Reshape this column vector into a 10 X 3 matrix
    X = first_30.reshape((numFeatures, numJogos)).transpose()
    # Get the rest of the 18 the numbers, after the first 30
    last_18 = xInicialEteta[numJogos * numFeatures:]
    # Reshape this column vector into a 6 X 3 matrix
    theta = last_18.reshape(numFeatures, numUsuarios).transpose()
    return X, theta



def calculate_gradient(xInicialEteta, notas, deuNota, numUsuarios, numJogos, numFeatures, reg_param):
    X, theta = unroll_params(xInicialEteta, numUsuarios, numJogos, numFeatures)

    # we multiply by deuNota because we only want to consider observations for which a rating was given
    difference = X.dot(theta.T) * deuNota - notas
    X_grad = difference.dot(theta) + reg_param * X
    theta_grad = difference.T.dot(X) + reg_param * theta

    # wrap the gradients back into a column vector
    return r_[X_grad.T.flatten(), theta_grad.T.flatten()]



def calculate_cost(xInicialEteta, notas, deuNota, numUsuarios, numJogos, numFeatures, reg_param):
    X, theta = unroll_params(xInicialEteta, numUsuarios, numJogos, numFeatures)

    # we multiply (element-wise) by deuNota because we only want to consider observations for which a rating was given
    cost = sum((X.dot(theta.T) * deuNota - notas) ** 2) / 2
    # '**' means an element-wise power
    regularization = (reg_param / 2) * (sum(theta ** 2) + sum(X ** 2))
    return cost + regularization


from scipy import optimize

regParam = 10


custoMin_e_paramOtimizados = optimize.fmin_cg(calculate_cost, fprime=calculate_gradient, x0=xInicialEteta, args=(notas, deuNota, numUsuarios, numJogos, numFeatures, regParam), maxiter=100, disp=True, full_output=True)

cost, optimal_movie_features_and_user_prefs = custoMin_e_paramOtimizados[1], custoMin_e_paramOtimizados[0]
jogoFeatures, usuarioPref = unroll_params(optimal_movie_features_and_user_prefs, numUsuarios, numJogos, numFeatures)


#Na real as recomendacoes nao farao muito sentido dado ao fato de os features de cada filme serem aleatorios e tal
#print jogoFeatures

allPrev = jogoFeatures.dot(usuarioPref.T)

print allPrev
previsoesJean = allPrev[:, 0:1] + notasMedia

print previsoesJean