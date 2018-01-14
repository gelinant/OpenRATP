import urllib.request




def checkfileondisk(csv):
		
	try:
		open(csv+'.csv','r')
	except FileNotFoundError:
		return False

	return True






def checkfilesondisk():
	missing =[]
	for csv in ['valid1','valid2','gares']:
		isondisk = checkfileondisk(csv)
		if isondisk == False:
			missing += [csv]
	return missing




def downloadmissing():
	missing = checkfilesondisk()
	for elt in missing:
		downloadfile(elt)
	print('done')






def downloadfile(FILE):
	if FILE == "valid1":
		URL = "https://opendata.stif.info/explore/dataset/validations-sur-le-reseau-ferre-nombre-de-validations-par-jour-1er-sem/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"

	elif FILE == 'valid2':
		URL = "https://opendata.stif.info/explore/dataset/validations-sur-le-reseau-ferre-nombre-de-validations-par-jour-2e-sem/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"

	elif FILE == "gares":
		URL = "https://opendata.stif.info/explore/dataset/emplacement-des-gares-idf/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"

	else :
		print('error')
		return('error')
		
	urllib.request.urlretrieve(URL, FILE+'.csv')



