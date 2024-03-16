import fitz

doc = fitz.open("nota_redacao.pdf") # open document

notasIniciais = {}
notasEdInfantil = {}
anosIniciais = True
educacaoInfantil = False

for page in doc :
   
    tabs = page.find_tables() # locate and extract any tables on page
    print(f"{len(tabs.tables)} found on {page}") # display number of found tables
    if tabs.tables:  # at least one table found? 
         for rows in tabs[0].extract():

            # CONDIÇÃO PARA PARAR PEGAR NOTAS DE ANOS INICIAIS
            if(rows[0] == "PROFESSOR - ARTE (EDUC INFANTIL AO ENSINO FUNDAMENTAL)"): 
                anosIniciais = False

            # CONDIÇÃO PARA COMEÇAR PEGAR NOTAS DE EDUCAÇÃO INFANTIL 
            if(rows[0] == 'PROFESSOR - EDUCAÇÃO INFANTIL'):
                educacaoInfantil = True
            
            # CONDIÇÃO PARA PARAR DE PEGAR NOTAS DE EDUCAÇÃO INFANTIL 
            if(rows[0] == 'PROFESSOR - GEOGRAFIA (ANOS FINAIS DO ENSINO FUNDAMENTAL)'):
                educacaoInfantil = False

            # validando dados 
            stringNota = str(rows[2])
            if(stringNota[0].isdigit()):
                notaFloat = float(rows[2].replace(',','.'))
                rows[2] = notaFloat
 
                if(anosIniciais):
                    notasIniciais[rows[1]] = rows
                if(educacaoInfantil):
                  
                    notasEdInfantil[rows[1]] = rows 

objetivaEdInfantil = True
objetivaAnosIniciais = False

# DADOS PROVA OBJETIVA
docProvaObjetiva = fitz.open('nota_objetiva.pdf')

for page in docProvaObjetiva:

    tabsObjetiva = page.find_tables() # locate and extract any tables on page
    print(f"{len(tabsObjetiva.tables)} found on {page}")
   
    if((objetivaEdInfantil == False) and (objetivaAnosIniciais == False)):
        break
    if(tabsObjetiva.tables):
        for row in tabsObjetiva[0].extract():
            if(row[0] == '402 - PROFESSOR - ANOS INICIAIS DO ENSINO FUNDAMENTAL'):
                objetivaEdInfantil = False 
                objetivaAnosIniciais = True

            # PARAR DE PEGAR DADOS OBJETIVA INICIAL 
            if(row[0] == '403 - PROFESSOR - ARTE (EDUC INFANTIL AO ENSINO FUNDAMENTAL)'): 
                objetivaAnosIniciais = False

            if(objetivaEdInfantil):
                if(row[4] in notasEdInfantil):
                    # print(notasEdInfantil[row[4]])
                    notasEdInfantil[row[4]].append(row[22])
                    strNotaRed = str(row[22])
                    notasEdInfantil[row[4]].append(notasEdInfantil[row[4]][2] + float(strNotaRed) )
                    # print(notasEdInfantil[row[4]])

            if(objetivaAnosIniciais):
                if(row[4] in notasIniciais):
                    # print(notasIniciais[row[4]])
                    notasIniciais[row[4]].append(row[22])
                    strNotaRed = str(row[22])
                    notasIniciais[row[4]].append(notasIniciais[row[4]][2] + float(strNotaRed) )
                    # print(notasIniciais[row[4]])
            
chaves_para_removerEdInfantil = []

for chave,valor in notasEdInfantil.items():
    if(len(valor) != 5):
        chaves_para_removerEdInfantil.append(chave)
for chave in chaves_para_removerEdInfantil:
    del notasEdInfantil[chave]

chaves_para_removerIniciais = [] 

for chave,valor in notasIniciais.items():
    if(len(valor) != 5):
        chaves_para_removerIniciais.append(chave)
for chave in chaves_para_removerIniciais:
    del notasIniciais[chave]

# SORTED PARA ORGANIZAR 
notasEdInfantil =  sorted(notasEdInfantil.items() , key=lambda x: x[1][4], reverse=True)
notasIniciais =  sorted(notasIniciais.items() , key=lambda x: x[1][4], reverse=True)
 
count = 1
out = open("output.txt", "wb") # create a text output

headerIniciais = '============== PROFESSOR - EDUCAÇÃO INFANTIL ==============\n\n'.encode("utf8")
out.write(headerIniciais)
out.write(bytes((12,)))

for i in notasEdInfantil:
    
    if(len(i[1]) == 5):
        text = f"{count}° - {i[1][0]} [{i[0]}] - {i[1][4]}\n".encode("utf8")
        out.write(text) 
        out.write(bytes((12,)))  
        count +=1

headerIniciais = '\n\n============== PROFESSOR - ANOS INICIAIS DO ENSINO FUNDAMENTAL ==============\n\n'.encode("utf8")
out.write(headerIniciais)
out.write(bytes((12,))) 

count = 1 

for i in notasIniciais:
    
    if(len(i[1]) == 5):
        text = f"{count}° - {i[1][0]} [{i[0]}] - {i[1][4]}\n".encode("utf8")
        out.write(text) 
        out.write(bytes((12,)))  
        count +=1 

out.close()
 