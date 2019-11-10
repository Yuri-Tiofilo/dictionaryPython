#Trabalho de Algoritmo e Lógica de programação relacionado com dicionario.
#Aluno: Yuri Tiofilo Silva código: 21853

nome = input('Insira o nome do arquivo: ')
arquivo = open(nome, 'r')
stopwords = open('stopwords.txt', 'r').read().split('\n')
print(stopwords)
print(type(stopwords))
x = dict()
vet = []

for linha in stopwords:
    words = linha.split()
    for word in words:
        vet.append(word)


for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        existe = False

        for stop in vet:
            if(palavra == stop):
                existe = True

        if not existe:
            if x.get(palavra):
                x[palavra] = x[palavra] + 1
            else:
                x[palavra] = 1
texto =''
maior = 0
for i in x:
    if(x[i]>maior):
        maior = x[i]
        texto = i

print(x)
print("Palavra mais repetida: " + texto)
print("Quantidade: " + str(x[texto]))
