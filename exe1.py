#1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
#anos ou não. Receba os dados pela console e chame este método. (modifique este
#exercício para receber 5 alunos, 3 notas para cada um e calcule a média mostrando se
#está aprovado ou não)

class MediaAluno():
    def maiorMedia(self):
        nota1 = int(input("Nota 1: "))
        nota2 = int(input("Nota 2: "))
        nota3 = int(input("Nota 3: "))
        media = ((nota1 + nota2 + nota3) / 3)  # Calculo de media

        # Verifica se maior que 18 "Aprovado"
        if media >= 18:
            print("Aprovado")
        else:
            print("Menor que 18")

chama=MediaAluno()

while True:
    opcao=int(input('1-Para começar a inserir suas notas \n'
                    '0-Sair'
                    ))
    if opcao ==1:
        chama.maiorMedia()
    elif opcao ==0:
        exit()
    else:
        print("Opção Invalida")

