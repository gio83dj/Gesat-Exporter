# QUESTO PROGRAMMA CARICA IL FILE DBF IN MEMORIA E POI LO TRASCRIVE IN XML


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
# --- carica dbf ---
table = DBF('SCHEDA.dbf', encoding='iso-8859-1', load=True)

print()
print()
#print('Caricati numero di schede su ATTUALE: ' + str(len(table)))
print()
print()


#i = input('Stampare le ultime schede, inserire numero di inserimenti dall ultima: ')
i = 2000
schedetot = i
lungtot = len(table)
i = lungtot - int(i)                   # PARTE A CONTARE TOT CHEDE PRIMA DELLA FINE 


while i < lungtot:
    od = OrderedDict(table.records[i])
    
    #print (i)
    if str(od['ANNO']) == "2019":
        if str(od['UT_STATO']) != "CON":
            print ('Numero scheda: ' + str(od['SCHEDA']))                
            print ('Anno: ' + str(od['ANNO']))
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
            if str(od['FL_REV']) == 'R':
                print ('COMPLETATO: SI')
            elif str(od['FL_REV']) == '':
                print ('COMPLETATO: NO')
            print ('----------------------------------------------------------------------------------------------------------------------------------')
    i = i + 1



#doc = ET.parse("schedeinput.xml")
#root_node = doc.getroot()                                  # NON FACCIO PIU IL PARSING DA FILE XML MA DA DATA COSI' ELIMINO IL FILE DI INPUT
xmldata = "<schedeTot></schedeTot>"
root_node = ET.fromstring(xmldata)
num_schede_anno = 0

indice = lungtot - int(schedetot)
while indice < lungtot:
    
    # child.set("attributo1","valore")                      # PER SETTARE UN ATTRIBUTO DEL TAG (NON MI SERVE AL MOMENTO
    od = OrderedDict(table.records[indice])
    
    if str(od['ANNO']) == "2019":
        if str(od['UT_STATO']) != "CON":
            child = ET.SubElement(root_node, "scheda")
            
            subelemento  = ET.SubElement(child,"numscheda")
            subelemento.text = str(od['SCHEDA'])
            
            subelemento  = ET.SubElement(child,"riferimento")
            subelemento.text = str(od['RIF_MITT'])
            
            subelemento  = ET.SubElement(child,"anno")
            subelemento.text = str(od['ANNO'])
            
            subelemento  = ET.SubElement(child,"cod")
            subelemento.text = str(od['CODCLI'])
            
            subelemento  = ET.SubElement(child,"nome")
            subelemento.text = str(od['DESCCLI'])
            
            subelemento  = ET.SubElement(child,"mod")
            subelemento.text = str(od['MODELLO'])
            
            subelemento  = ET.SubElement(child,"matr")
            subelemento.text = str(od['MATRICOLA'])
            
            subelemento  = ET.SubElement(child,"serial")
            subelemento.text = str(od['SERIALE'])
            
            subelemento  = ET.SubElement(child,"accessori")
            subelemento.text = str(od['ACCESSORI'])
            
            subelemento  = ET.SubElement(child,"difetto")
            subelemento.text = str(od['NOTE'])
            
            subelemento  = ET.SubElement(child,"stato")
            subelemento.text = str(od['UT_STATO'])
            
            subelemento  = ET.SubElement(child,"chiusa")
            subelemento.text = str(od['FL_REV'])
            
                                                            
            if str(od['UT_STATO']) == "NN":
                if str(od['FL_REV']) != "R":
                    file = open('Non ancora visti.txt','a')
                    file.write(str(od['SCHEDA']) + " " + str(od['DATA']) + " " + str(od['DESCCLI']) + " " + str(od['RIF_MITT']) + " - " + str(od['MODELLO']) + '\n')
                    file.close()
            
            
            tree = ET.ElementTree(root_node)
            
            
            #print(od['SCHEDA'])
            #print (indice)

    indice = indice + 1
    
#tree.write('output.xml')

esci = input ("File 'Non ancora visti.txt' Salvato. Premi un tasto per chiudere la finestra.")