{"filter":false,"title":"4.6.py","tooltip":"/4.6.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":54},"action":"insert","lines":["notas = []","for i in range(0, 10):","    notasAluno = []","    for j in range(0, 4):","        notasAluno.append(","            float(raw_input('Informe a nota do aluno %.d: ' % (i + 1))))","    notas.append(notasAluno)","","alunosMedia = 0","for notasAluno in notas:","    somaNotas = 0","    for nota in notasAluno:","        somaNotas += nota","    if ((somaNotas / 4.0) >= 7.0):","        alunosMedia += 1","","print '%d alunos ficaram acima da media' % alunosMedia"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":54},"end":{"row":16,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1597429033201,"hash":"c1e797cb8358eb369a01c61ec4c6d435483ab2b3"}