import pandas as pd
import os
os.system('mystem -l text.txt test1.txt') #Opens mystem in the ternimal and creats file with lemmas

file = open('test1.txt', 'r', encoding='utf8') #Reads the new file
lemmasString = file.read()

#Creating a list of lemmas and deleting all extra symbols
lemmas = lemmasString.split('}')
newLemmas = []
for lemma in lemmas:
    newLemmas.append(lemma.replace('{', ''))
newLemmas.pop()

#Creating a list of lemmas without repetions and a list that counts the times a given lemma appears in the text
counts = []
finalLemmas = []

for newlemma in newLemmas:
    if newlemma not in finalLemmas:
        finalLemmas.append(newlemma)
        i=0
        for otherLemma in newLemmas:
            if newlemma == otherLemma:
                i=i+1
        counts.append(i)

#Creating a dataframe out of the lists and writing it to an excel spreadshit       
df = pd.DataFrame({'count': counts, 'lemma': finalLemmas})
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()