"""  FORMATI
 OrderedDict([
 -('SCHEDA', 2327), 
 -('ANNO', '2019'), 
 -('DATA', datetime.date(2019, 11, 13)), 
 ('DATA_LAV', None), ('TIPOAPP', '10'), ('DISTINTA', None), ('NOTAGR', None), 
 ('MARCA', 'ZE'), 
 -('MATRICOLA', 'WT22-32111800186'), 
 ('VMATRICOLA', ''), 
 -('SERIALE', ''), 
 ('VSERIALE', ''), 
 -('MODELLO', 'ZV32HD'), 
 -('DESC_MOD', 'TV COLOR'), 
 ('COD_PROD', ''), 
 -('ACCESSORI', 'SCATOLA.TELECOMANDO PIEDI'), 
 ('DIFETTO', ''), ('SINTOMO', ''), 
 -('NOTE', 'linee schermo                                               verificato non rotto'), 
 -('CODCLI', 'CME365'), 
 ('BAM', '275'), 
 -('MITTENTE', 'CME365'), ('RAGIONE', 'MERKANT S.R.L. COMIS'), 
 -('GARANZIA', 'S'), 
 ('NUM_GAR', ''), 
 -('DATA_ACQ', datetime.date(2019, 5, 4)), 
 ('INVEND', ''), ('FAMIGL', ''), ('PRE_SN', 'N'), ('PREVENTIVO', 0.0), ('DT_PREV', None), ('IMPMAT', None), ('IMPOPERA', None), ('SPESA1', None), ('SPESA2', None), ('TOTALE', None), ('FL_STATO', ''), ('DT_FINE', None), ('RICFIS', ''), ('DATA_DOC', None), ('LAB_EST', 'L'), ('RESA', ''), ('DIVISI', ''), ('SOCIETA', 'CO'), ('DIF_RIV', ''), ('FLAG_567', ''), ('FL_TRA', ''), ('N_BOL', ''), ('DT_BOL', None), ('COD_GUA', ''), ('COD_RIP', ''), ('CODTEO', 300), ('FL_REV', ''), ('N_CELL', ''), ('DT_PROD', None), ('RELLAV1', ''), ('RELLAV2', ''), ('RELLAV3', ''), ('RELLAV4', ''), ('REL_LAV', ''), ('IMPMATG', None), ('IMPOPERAG', None), ('TOTALEG', None), ('TOTGEN', None), ('TIPO_INT', ''), ('IMPULG', None), ('IMPULFG', None), ('ULG', None), ('ULFG', None), ('IVAMAT', None), ('TOTALEIC', None), ('FLAG_SEL', ''), ('UBICAZIONE', ''), ('SCONTO', None), ('DT_ATTMAT', None), ('IVAMATG', None), ('SPE_CASA', None), ('DT_INTERV', None), ('IVAMANF', None), ('IVAMANG', None), ('RIENTRO', ''), ('DIFRIS1', ''), ('DIFRIS2', ''), ('DIFRIS3', ''), ('DIFRIS4', ''), ('DT_VAR', '20191113163506'), ('UTENTE', ''), ('LUOGODOC', ''), 
 ('DESCCLI', 'MERKANT S.R.L. COMISO 3'), 
 ('NUMFISC', ''), ('FLAG_DDT', ''), ('ANNODIS', ''), ('ANNOBOL', ''), ('DT_TRASM', None), ('DT_STATO', None), ('ANNOFISC', ''), ('CODIVAMAT', ''), ('CODIVAMAN', ''), ('DATA_BAM', datetime.date(2019, 11, 13)), 
 ('TEL_MITT', '3277769159'), 
 ('RIF_MITT', ''), 
 ('ORA_IN', '16:33:19'), 
 ('ORA_LAV', ''), ('ORA_OUT', ''), ('COD_DEST', ''), 
 -('UT_STATO', 'NN'), 
 ('GAR_MANIC', None), ('GAR_MATIC', None), ('GAR_SPEIC', None), ('GAR_TOTIC', None), ('GAR_DTAGG', None), ('STATUS_TX', ''), ('FLAG_TX', ''), ('FL_TXABIL', ''), ('CODICE_PN', ''), ('CODICE_PN2', ''), ('PER_FATT', ''), ('ORA_INILAV', ''), ('CYCLE_TIME', ''), ('REPAIRTIME', ''), ('TIMELAV', None), ('FL_AGGCH', None), ('TRASP_CASA', None), ('CHIAM_CASA', None), ('CIC_TX', ''), ('ID_TX', ''), ('STATO_TX', ''), ('RIF_EXT', ''), ('TK_UUID', ''), ('TK_UPDATED', ''), ('SENDNOTIFY', ''), ('CIC_TX2', ''), ('CIC_TX3', ''), ('OK_VIS', 'Y')])
 
 
 <schedeTot>
	<scheda>
		<numscheda>2327</numscheda>
		<cod>CME365</cod>
		<nome>MERKANT S.R.L. COMISO 3</nome>
		<mod>ZV32HD</mod>
		<matr>WT22-32111800186</matr>
		<serial />
		<accessori>SCATOLA.TELECOMANDO PIEDI</accessori>
		<difetto>linee schermo                                               verificato non rotto</difetto>
		<stato>NN</stato>
	</scheda>
</schedeTot>
"""
import xml.etree.ElementTree as ET
from dbfread import DBF
from collections import OrderedDict

# --- caricati gli xml ---
#tree = ET.parse('schedeinput.xml')
#root = tree.getroot()

print ('Sto caricando le schede in memoria, attendere...')
# --- caricati dbf ---
table = DBF('SCHEDA.dbf', encoding='iso-8859-1', load=True)

print()
print()
print('Caricati numero di schede su ATTUALE: ' + str(len(table)))
print()
print()

def print_options():
    print ("Scegli:")
    print (" 'p' Visualizza opzioni")
    print (" '1' Stampa a video il contenuto del file dbf")
    print (" '2' Legge una particolare scheda")
    print (" '3' Stampa a video ultime schede")
    print (" '4' Esporta XML")
    print (" 'q' Esce dal programma")


i = input('Stampare le ultime schede, inserire numero di inserimenti dall ultima: ')
xi = i
lung = len(table)
i = lung - int(i)


while i < lung:
    od = OrderedDict(table.records[i])
    print (i)
    print ('Numero scheda: ' + str(od['SCHEDA']))                
    print ('Nome cliente: ' + str(od['DESCCLI']))
    print ('Codice cliente: ' + str(od['CODCLI']))
    print ('Modello: ' + str(od['MODELLO']))
    print ('Matricola: ' + str(od['MATRICOLA']))
    print ('Seriale: ' + str(od['SERIALE']))
    print ('Accessori: ' + str(od['ACCESSORI']))
    print ('Difetto: ' + str(od['NOTE']))
    if str(od['UT_STATO']) == 'CON':
        print ('Consegnato: SI')
    elif str(od['UT_STATO']) == 'NN':
        print ('Consegnato: NO')
    print ('----------------------------------------------------------------------------------------------------------------------------------')
    i = i + 1



doc = ET.parse("schedeinput.xml")
root_node = doc.getroot()

xx = lung - int(xi)
while xx < lung:
    child = ET.SubElement(root_node, "scheda")
    # child.set("attributo1","valore")                      # PER SETTARE UN ATTRIBUTO DEL TAG
    od = OrderedDict(table.records[xx])
    
    group  = ET.SubElement(child,"numscheda")
    group.text = str(od['SCHEDA'])
    
    group  = ET.SubElement(child,"cod")
    group.text = str(od['CODCLI'])
    
    group  = ET.SubElement(child,"nome")
    group.text = str(od['DESCCLI'])
    
    group  = ET.SubElement(child,"mod")
    group.text = str(od['MODELLO'])
    
    group  = ET.SubElement(child,"matr")
    group.text = str(od['MATRICOLA'])
    
    group  = ET.SubElement(child,"serial")
    group.text = str(od['SERIALE'])
    
    group  = ET.SubElement(child,"accessori")
    group.text = str(od['ACCESSORI'])
    
    group  = ET.SubElement(child,"difetto")
    group.text = str(od['NOTE'])
    
    group  = ET.SubElement(child,"stato")
    group.text = str(od['UT_STATO'])
    
    tree = ET.ElementTree(root_node)
    
    
    #print(od['SCHEDA'])
    #print (xx)
    xx = xx + 1
    
tree.write('output.xml')