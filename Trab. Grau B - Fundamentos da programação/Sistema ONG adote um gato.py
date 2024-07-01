import csv
import os.path

registros = 'registros.csv'
header = ['Nome', 'Sexo', 'Idade', 'Raça', 'Cor Predominante', 'Castrado', 'FIV+', 'FELV+', 'Data de Resgate', 'Adotado', 'Lar Temporário', 'Data de Adoção/Hospedagem', 'Tutor', 'Contato', 'Data da Última Vacina', 'Data da Última Desvermifugação', 'Data do Último Antipulgas', 'Informações Extras']

def loadBasicData():
    if not os.path.isfile(registros):
        arqEscrita = open(registros, 'w',newline='')
        writer = csv.writer(arqEscrita)
        writer.writerow(header)
        arqEscrita.close()
    
def loadData(data):
    loadBasicData()
    arqEscrita = open(registros, 'a', newline='')
    writer = csv.writer(arqEscrita)
    writer.writerow(data)

    arqEscrita.close()

def menu():
    print('''
        1) Cadastrar felino
        2) Alterar status de felino
        3) Consultar informações sobre felino
        4) Apresentar estatísticas gerais
        5) Filtragem de dados
        6) Salvar
        7) Sair do programa
        ''')

def catRegistry():
    catName = input('Insira o nome do felino: ')
    catGender = input('Insira o sexo do felino: ')
    catAge = input('Insira a idade do felino: ')
    catRace = input('Insira a raça do felino: ')
    catColor = input('Insira a cor predominante do felino: ')
    catCastrate = input('O felino é castrado? ')
    catFIV = input('O felino possui FIV?  ')
    catFELV = input('O felino possui FELV?  ')
    catRescueDate = input('Insira a data de resgate do felino: ')
    catAdoption = input('O felino foi adotado?  ')
    catTemporaryHome = input('O felino possui lar temporário?  ')

    if catAdoption == 'Sim' or catTemporaryHome == 'Sim':
        catAdoptionOrHostingDate = input('Insira a data de hospedagem/Adoção do felino:  ')
        catTutor = input('Insira o nome do(a) tutor(a) do felino:  ')
        catTutorContact = input('Insira o número de contato do(a) tutor(a): ')
    else:
        catAdoptionOrHostingDate = '-'
        catTutor = '-'
        catTutor = '-'

    catLastVaccineDate = input('Insira a data da última vacina do felino: ')
    catLastDewormingDate = input('Insira a data da última desvermifugação do felino: ')
    catLastAntifleaDate = input('Insira a data do último antipulgas do felino: ')
    catExtraInfo = input('Insira informações extras do felino: ')
    
    catData = [catName, catGender, catAge, catRace, catColor, catCastrate, catFIV, catFELV, catRescueDate, catAdoption, catTemporaryHome, catAdoptionOrHostingDate, catTutor, catTutorContact, catLastVaccineDate, catLastDewormingDate, catLastAntifleaDate, catExtraInfo]

    return loadData(catData)

def catChangeStats():
    if os.path.isfile(registros):
        arqEscrita = open(registros)
        reader = csv.reader(arqEscrita)
        data = list(reader)
        arqEscrita.close()

        while True:
            print('\nEscolha o felino que deseja alterar (Selecione pelo número):')
            for i in range(1, len(data)):
                print(str(i) + ') ' + data[i][0])

            print('\nCaso queira voltar a tela de menu, digite: "sair"')

            catSelected = input('\n')

            if catSelected == 'sair':
                break
            else:
                catSelected = int(catSelected)

            print('\nInformações do felino:')
            for y in range(len(data[catSelected])):
                print(str(y+1) + ') ' + data[0][y] + ': ' + data[catSelected][y])

            print('\nCaso queira voltar a tela de menu, digite: "sair"')

            infoChange = input('\nQual informação você deseja alterar? (Escolha um dos números mostrados) ')

            if infoChange == 'sair':
                break
            else:
                infoChange = int(infoChange)

            print('Valor selecionado = '+ data[0][infoChange - 1] + ': ' + data[catSelected][infoChange - 1])

            TextChange = input('Escreva o novo valor desta informação: ')

            data[catSelected][infoChange - 1] = TextChange

            arqEscrita = open(registros, 'w', newline='')
            escritor = csv.writer(arqEscrita)
            escritor.writerows(data)
    else:
        print('\nNenhum registro encontrado.')

def catConsult():
    if os.path.isfile(registros):
        arqEscrita = open(registros)
        reader = csv.reader(arqEscrita)
        data = list(reader)
        arqEscrita.close()

        while True:
            for i in range(1, len(data)):
                print(str(i) + ') ' + data[i][0])

            print('\nCaso queira voltar a tela de menu, digite: "sair"')

            catSelected = input('\n')

            if catSelected == 'sair':
                break
            else:
                catSelected = int(catSelected)
            for y in range(len(data[catSelected])):
                print(data[0][y] + ': ' + data[catSelected][y])
            break
    else:
        print('\nNenhum registro encontrado.')

def catPercentage():
    if os.path.isfile(registros):
        arqEscrita = open(registros)
        reader = csv.reader(arqEscrita)
        data = list(reader)
        arqEscrita.close()

        fiv = 0
        felv = 0
        fivAndFelv = 0
        NotFivOrFelv = 0
        adopted = 0
        NotAdopted = 0
        Male = 0
        Female = 0
        cats = []

        for i in range(1, len(data)):
            if data[i][6] == 'Sim' and data[i][7] == 'Não':
                fiv += 1
            if data[i][7] == 'Sim' and data[i][6] == 'Não':
                felv += 1
            if data[i][6] == 'Sim' and data[i][7] == 'Sim':
                fivAndFelv += 1
            if data[i][6] == 'Não' and data[i][7] == 'Não':
                NotFivOrFelv += 1
            if data[i][9] == 'Sim':
                adopted += 1
            if data[i][9] == 'Não':
                NotAdopted += 1
            if data[i][1] == 'M':
                Male += 1
            if data[i][1] == 'F':
                Female += 1
            cats.append(data[i][0])
        totalCats = len(cats)

        calcFiv = round((fiv / totalCats) * 100)
        calcFelv = round((felv / totalCats) * 100)
        calcFivAndFelv = round((fivAndFelv / totalCats) * 100)
        calcNotFivAndFelv = round((NotFivOrFelv / totalCats) * 100)
        calcAdopted = round((adopted / totalCats) * 100)
        calcNotAdopted = round((NotAdopted / totalCats) * 100)
        calcMale = round((Male / totalCats) * 100)
        calcFemale = round((Female / totalCats) * 100)
        print('Felinos que possuem FIV ' + '- ' + str(calcFiv) + '%')
        print('Felinos que possuem FELV ' + '- ' + str(calcFelv) + '%')
        print('Felinos que possuem FIV e Felv ' + '- ' + str(calcFivAndFelv) + '%')
        print('Felinos que não possuem FIV ou Felv ' + '- ' + str(calcNotFivAndFelv) + '%')
        print('Felinos foram adotados ' + '- ' + str(calcAdopted) + '%')
        print('Felinos que não foram adotados ' + '- ' + str(calcNotAdopted) + '%')
        print('Felinos fêmeas ' + '- ' + str(calcFemale) + '%')
        print('Felinos machos ' + '- ' + str(calcMale) + '%')
    else:
        print('\nNenhum registro encontrando.')

def CatFilterByDate():
    if os.path.isfile(registros):
        arqEscrita = open(registros)
        reader = csv.reader(arqEscrita)
        data = list(reader)
        arqEscrita.close()

        dataStartStr = input("Insira a data de início (no formato dd/mm/yyyy): ")
        dataEndStr = input("Insira a data de final (no formato dd/mm/yyyy): ")

        dataStart = ConvertData(dataStartStr)
        dataEnd = ConvertData(dataEndStr)

        for i in range(1, len(data)):
            rescueDataStr = data[i][8]
            rescueData = ConvertData(rescueDataStr)

            if dataStart <= rescueData <= dataEnd:
                print(f"\nGato(a) {data[i][0]} resgatado(a) em {rescueDataStr}\n")   
    else:
        print('\nNenhum registro encontrado.')

def ConvertData(dataStr):
    day, month, year = map(int, dataStr.split('/'))

    return year * 10000 + month * 100 + day

while True:
    print('''
        1) Cadastrar felino
        2) Alterar status de felino
        3) Consultar informações sobre felino
        4) Apresentar estatísticas gerais
        5) Filtragem de dados
        6) Salvar
        7) Sair do programa
        ''')
    
    choice = int(input('Insira o número da alternativa que deseja: '))

    if choice == 7:
        break
    elif choice == 1:
        catRegistry()
    elif choice == 2:
        catChangeStats()
    elif choice == 3:
        catConsult()
    elif choice == 4:
        catPercentage()
    elif choice == 5:
        CatFilterByDate()
    elif choice == 6:
        print('\nO arquivo e suas alterações são salvos automaticamente.')

