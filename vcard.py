from dbfread import DBF
from collections import OrderedDict

print ('Sto caricando le schede in memoria, attendere...')
# --- caricati dbf ---
table = DBF('SCHEDA.dbf', encoding='iso-8859-1', load=True)

print()
print()
print('Caricati numero di schede su ATTUALE: ' + str(len(table)))
print()
print()

i = input('Stampare le ultime schede, inserire numero di inserimenti dall ultima: ')
lung = len(table)
i = lung - int(i)
prima = i

while i < lung:
    od = OrderedDict(table.records[i])
    print (i)
    file = open("rubrica_"+str(OrderedDict(table.records[prima])["SCHEDA"]) + "-" + str(OrderedDict(table.records[lung-1])["SCHEDA"])+".vcf","a")
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:2.1\n")
    file.write("N:" + str(od["DESCCLI"]) + "\n")
    file.write("FN:" + str(od["DESCCLI"]) + "\n")
    file.write("TEL;CELL;PREF:" + str(od['TEL_MITT']) + "\n")
    file.write("END:VCARD\n")
    file.close()
    i = i + 1
    