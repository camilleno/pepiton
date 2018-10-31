import os
import sys

cheminSite = "C:\\xampp\\htdocs\\" # chemin du site
dossierSite = 'camno' # Dossier du site web
cheminBackup = 'C:\\Users\\Administrateur.WIN-2LSSMGFLPDD\\Desktop\\save' # Dossier des sauvegardes

cheminMysql = 'C:\\xampp\\mysql\\bin\\'

optionsMenu = [ ["1-", "Sauvegarder le site",
					  "Xcopy /E /Y %s%s %s" % (cheminSite, dossierSite, cheminBackup)],
                ["2-", "Sauvegarder la base de donnees",
                       "%smysqldump -u root  --opt mrbs -h localhost --databases>%s/%s.sql" % (cheminMysql, cheminBackup, dossierSite)],
			["3-", "Restaurer le site",
				      "Xcopy /E /Y %s %s%s " % (cheminBackup, cheminSite, dossierSite )],
				 ["4-", "Restaurer la base de donnees",
					   "%smysql -u root  <%s/%s.sql" % (cheminMysql,
cheminBackup, dossierSite)],
				["5-", "Quitter\n",""]]
debug_print = False
if len(sys.argv) == 2:
	  debug_print = sys.argv[1] == 'debug'

while True:
	print ("========== M E N U ===========\n")
	for optionNum, optionTxt, optionCmde in optionsMenu:
		print (optionNum, optionTxt)

	try:
		choix = int(input('Entrez votre choix : '))
	except ValueError:
		choix = 0
	if choix == len(optionsMenu):break
	choix-= 1
	if choix in range(len(optionsMenu)):
		if debug_print:
			print ('[%s]\n>>> %s\n' % (optionsMenu[choix][1], optionsMenu[choix][2]))
		else:
		     os.system(optionsMenu[choix][2])
