nome = str(input("Qual o nome do aluno?"))
notaPortugues = float(input("Qual a nota em Português?"))
notaMatematica = float(input("Qual a nota em Matematica?"))
notaCGerais = float(input("Qual a nota em Conhecimentos Gerais?"))

media = (notaPortugues  + notaMatematica + notaCGerais)/3
if (media >= 7 and notaPortugues >= 5 and notaMatematica >= 5 and notaCGerais >=5):
    situacao = "aprovado"
else:
    situacao = "reprovado"

print("O aluno ",nome," se encontra atualmente ",situacao,". Sua nota em matematica foi ", 
notaMatematica, ", sua nota em portugues foi ",notaPortugues,", sua nota em conhecimentos gerais foi ",
notaCGerais,", totalizando uma média de ",media)
