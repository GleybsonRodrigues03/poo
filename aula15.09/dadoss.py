from main import Aluno

aluno1=Aluno()

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))

aluno1.calcular_media(nota1, nota2, nota3)
aluno1.resultado_media()
aluno1.resultado_situacao()

