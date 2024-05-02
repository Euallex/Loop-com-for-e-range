notas = []

for x in range(5):
    nome_aluno = input(("nome: "))
    nota_p = float(input("nota: "))
    nota_t = float(input("nota: "))
    nota_tr = float(input("nota: "))
    m = float((nota_p + nota_t + nota_tr)) / 2
    resultado = [nome_aluno, m]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
    nome_aluno = n[0]
    notas = n[1]

    print('O aluno', nome_aluno, 'teve a média:', notas,)

    if notas >= 7:
        print('Aluno aprovado!')
    elif notas < 7 and notas > 6:
        print('Aluno na repescagem!')
    else:
        print('Aluno reprovado!')
   
