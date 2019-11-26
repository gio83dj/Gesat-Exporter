copy "Z:\gesat\DBF\SCHEDA.DBF" "C:\Users\Giorgio\Desktop\Program\SCHEDA.DBF"
cd Program
python vcard.py
move "C:\Users\Giorgio\Desktop\Program\*.vcf" "C:\Users\Giorgio\Desktop\Program\vcf"
pause
python dbf_anno.py
ftp -s:script.txt
quit
