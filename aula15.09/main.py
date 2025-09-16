class Aluno: 
    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.media = 0 
        self.situacao = ""
    

    def calcular_media(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
       

    def resultado_media(self):
        print(f"MÉDIA: {self.media}")
        
        

    def resultado_situacao(self):
        if self.media >= 7:
           self.situacao = "APROVADO"
        else:
            self.situacao = "REPROVADO"
        print(f'{self.situacao}')
      

        



