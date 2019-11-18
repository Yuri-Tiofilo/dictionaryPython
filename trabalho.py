#Segunda questão do trabalho de algoritmo
# Aluno: Yuri Tiofilo Silva código: 21853

def inserir(qtd,alunos):
    for i in range(0,qtd):
        aux = []
        aux.append(input('Nome Aluno: '))
        aux.append(int(input('Matricula: ')))
        aux.append(input('E-mail:'))
        aux.append(int(input('Idade: ')))
        aux.append(float(input('Altura: ')))
        aux.append(int(input('Disciplina: ')))
        aux.append(int(input('Ano de ingresso: ')))
        aux.append(float(input('Nota 1: ')))
        aux.append(float(input('Nota 2: ')))
        aux.append(float(input('Nota 3: ')))
        aux.append(float(input('Nota 4: ')))
        media = (aux[7]+aux[8]+aux[9]+aux[10])/4
        aux.append(media)
        alunos.append(aux)
def escreverArquivo(arquivo,alunos):
    abrir = open(arquivo,'w')
    for i in alunos:
        for j in i:
            abrir.write(str(j)+';')
        abrir.write('\n')
    abrir.close()
def media(dic,alunos):
    mensagem = ''
    for i in alunos:
        nome = i[0]
        media = i[11]
        dic[nome] = media
        primeiro_nome = nome.split()
        mensagem += 'O aluno %s tem como média %.2f\n'%(primeiro_nome[0],media)
    return mensagem


def Saida2(alunos):
    top_alunos = []
    turma = []

    for j in range(6, 10):
        soma = 0
        for i in alunos:
            soma += alunos[i][j]
        turma.append(soma / len(alunos))
    print(turma)

    for y in range(6, 10):
        for x in alunos:
            melhor_aluno = alunos[max(alunos, key=alunos.get[y])]
            top_alunos.append(melhor_aluno)
            if alunos[x][y] not in top_alunos:
                segundo_melhor = alunos[max(alunos[x][y], key=alunos.get)]
                top_alunos.append(segundo_melhor)
            elif alunos[x][y] not in top_alunos:
                terceiro_melhor = alunos[max(alunos[x][y], key=alunos.get)]
                top_alunos.append(terceiro_melhor)

    print(top_alunos)

#entrada do arquivo:
alunos = []
dic = {}
qtd = int(input('Quantidade de alunos: '))
arquivo = input('Arquivo: ')
inserir(qtd,alunos)
escreverArquivo(arquivo,alunos)
saida1 = media(dic,alunos)
Saida2(alunos)
print(saida1)
