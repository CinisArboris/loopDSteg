import os
import subprocess
import time

#Archivos de prueba.
test_fileTXT = "./test/secret.txt"
test_fileJPG = "./test/f_f_a.jpg"
test_keys = "./test/wordlist.txt"

keys = "C:\\Users\\eyver-dev\\Documents\\python\\loopSteg\\rockyou.txt"
response = -1
resA = 'wrote extracted data to "secret.txt".'
resB = 'the file "secret.txt" does already exist. overwrite ?'

# ============================
def ocultar(origen, destino, key):
	comando = 'steghide embed -cf '+origen+' -ef '+destino+' -p '+key
	response = subprocess.Popen(comando,shell=True)
	status(response, key)
# ============================
def des_ocultar(destino, wordlist):
	response = 'default'
	wordlist = wordlist.replace("\\", "/")
	wordlist = wordlist.replace('"', "")
	word = open(wordlist, "r")
	contenido = word
	for w in contenido:
		print ('try', w)
		comando = 'steghide extract -sf '+destino+' -p '+w
		response = subprocess.getoutput(comando)
		if (response == resA):
			print ('key found !!!', w)
			word.close()
			return 0
		if (response == resB):
			return 0
# ============================
def status(response, k):
	#response = 0 // true:succes:200
	#response = 1 // false:error:404
	if (response == 0): print ('200', k)
	if (response == 1): print ('404')
	print ('*'*10)
# ============================
def test(codOP):
	if (codOP == 1):
		ocultar(
			test_fileJPG,
			test_fileTXT,
			key
		)#ENCRYPT
		print ('encryptado ::', key)
	if (codOP == 2):
		des_ocultar(
			test_fileJPG, test_keys
		)#DECRYPT
# ============================
def operacion(codOP):
	if (codOP == 1):
		fileJPG_container = input('Contenedor  ')
		fileTXT_flag = input('flag  ')
		password = input('clave  ')
		ocultar(
			fileJPG_container,
			fileTXT_flag,
			password
		)#ENCRYPT
	if (codOP == 2):
		fileJPG_container = input('param[container]  ')
		wordlist = input('param[wordlist]  ')
		if (wordlist == ""):
			wordlist = os.environ['rockyou']
			print ('param[wordlist]', wordlist)
		res = des_ocultar(
			fileJPG_container,
			wordlist
		)#DECRYPT
		if (res == 0): return 0



# ************************************************
# FUNCIONES DISPONIBLES
print ('Requisitos :: [steghide] en las variables de entorno.')
print ('Requisitos :: [wordlist.txt] en una variable, con la ruta absoluta.')
print ('Requisitos :: [archivo txt a esconder] en una variable, con la ruta absoluta.')
print ('Requisitos :: [archivo jpg a ser el contenedor] en una variable, con la ruta absoluta.')
print ('1 :: ENCRYPT')
print ('2 :: DECRYPT LOOP')
codOP = int(input('\nElige tu opcion :: '))
test(codOP)
#operacion(codOP)






		
