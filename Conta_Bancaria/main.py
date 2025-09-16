from saldo import Saldo
from conta import Conta
from pessoas import Pessoas



p1=Pessoas("Luciano Juba", "79686357981", "filhodokami01@gmail.com", "81986547654")
p2=Pessoas("Lucas Lima", "857431876400", "lucaslima1@gmail.com", "81987654321")
p3=Pessoas("Rodrigo Faro", "64580953217", "rodrigofaro@gmail.com", "81909876543")

c1=Conta("001", "corrente", "665")
c2=Conta("002", "poupança", "654")  
c3=Conta("003", "corrente", "736") 


s1=Saldo("R$10.000")
s2=Saldo("R$13.000")
s3=Saldo("R$16.000")

p1.exibir_pessoas()
c1.exibir_dados()
s1.exibir_saldo()

p2.exibir_pessoas()
c2.exibir_dados()
s3.exibir_saldo()

 
p3.exibir_pessoas()
c3.exibir_dados()
s2.exibir_saldo()





