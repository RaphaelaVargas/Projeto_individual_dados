candidatos = [
    ['candidato 1', 'e5_t10_p8_s8'],
    ['candidato 2', 'e10_t7_p7_s8'],
    ['candidato 3', 'e8_t5_p4_s9'],
    ['candidato 4', 'e2_t2_p2_s1'],
    ['candidato 5', 'e10_t10_p8_s9']
]


def verificaaNota(nota):
    while True:
        if nota.isdigit():
            return int(nota)
        else:
            print('Insira uma nota válida!')
            nota = input('Digite a nota novamente: ')
            

def insiraNota(mensagem):
    notaMin = 0
    notaMax = 10
    while True:
        nota = input(mensagem)
        nota = verificaaNota(nota)
        if nota >= notaMin and nota <= notaMax:
            return nota
        else:
            print('Insira uma nota entre 0 e 10!')


def addCandidato(nomeCandidato, entrevista, testeTeorico, testePratico, softSkills): 
    e = 'e'+ str(entrevista)
    t = 't' + str(testeTeorico)
    p = 'p' + str(testePratico)
    s = 's' + str(softSkills)
    nota = [e, t, p, s]
    notas = '_'.join(nota)
    candidato = [nomeCandidato, notas]  
    if candidato not in candidatos:
        candidatos.append(candidato)
        return True
    else:
        return False


def busCandidatos(candidatos, entrevista, teorico, pratico, soft):
    candidatosAprovados = []
    for candidato, resultado in candidatos:
        notas = resultado.split('_')
        e = int(notas[0][1:])
        t = int(notas[1][1:])
        p = int(notas[2][1:])
        s = int(notas[3][1:])
        if e >= entrevista and t >= teorico and p >= pratico and s >= soft:
            candidatosAprovados.append(candidato)
    return candidatosAprovados



menu = """ 
=========================================
        INFORME UMA OPÇÃO ABAIXO:
    [1] - Adicionar candidato
    [2] - Procurar candidato

=>: """

while True:
    opcao = input(menu)
    if opcao == '1':
        nomeCandidato = input(''' 
=========================================
Informe o nome do candidato:                                       
=> ''')
        entrevista = insiraNota(''' 
=========================================
Informe a avaliação da entrevista [e]:                                        
=> ''')
        testeTeorico = insiraNota(''' 
=========================================
Informe a avaliação do teste teórico [t]:                                      
=> ''')
        testePratico = insiraNota(''' 
=========================================
Informe a avaliação do teste prático [p]:                                      
=> ''')
        softSkills = insiraNota('''
=========================================
Informe a avaliação de soft skills [s]:                                  
=> ''')


        if (addCandidato(nomeCandidato,  entrevista, testeTeorico, testePratico, softSkills)):
            print('Candidato adicionado com sucesso!')
        else:
           print('Não foi possivel adicionar candidato.')

    elif opcao == '2':
        entrevista = insiraNota("Digite a nota mínima de entrevista: [e] ")
        teorico = insiraNota("Digite a nota mínima de teste teórico: [t] ")
        pratico = insiraNota("Digite a nota mínima de teste prático: [p] ")
        soft = insiraNota("Digite a nota mínima de avaliação de soft skills: [s] ")
        candidatosApro  = (busCandidatos(candidatos, entrevista, teorico, pratico, soft))    
        if candidatosApro:
            print("Candidatos aprovados: ")
            for candidato in candidatosApro:
                print(candidato)
        else:
            print('Não há candidatos compatíveis.')
    else:
        print('Opção inválida.')