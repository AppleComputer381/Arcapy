import configparser
from files import files
import os


class conf:
	"""
	s'occupe de tout les fichiers de configurations
	"""
	

	def console(*, nom, locj, nbrj = 0, nemu1, nemu2 = 0, cmd1, cmd2 = 0, dsc, img = 0):
		"""
		creer un fichier de configuration pour les consoles
		"""
		config = configparser.ConfigParser()
		files= os.listdir("Data/conf/")
		config.read("Data/conf/console.conf")
		config[nom.upper()] = {"dir-jeu": locj, "nbr-jeu": nbrj, "emulateur-1": nemu1, 
									"cmd-emu": cmd1, "emulateur-2": nemu2, "cmd-emu-2": cmd2,
									"description": dsc, "image": img}

		with open(f"Data/conf/console.conf", 'w') as configfile:
			config.write(configfile)
			print("finish")


	def jeu(*, dir, nom, lang = 0, an = 0, dsc = 0, img = 0, dirj):
		"""
		ajoute un jeu a la liste
		dir --> la ou est situer le fichier qui liste tout les jeux present exemple: 
			D:/console/ (ne pas mettre liste.conf si il y est deja present)

		"""
		config = configparser.ConfigParser()
		config.read(f"{dir}liste.conf")

		config[nom] = {"langue": lang, "annee-de-sortie": an, "description du jeu": dsc, "dir-image": img, "dir-jeu": dirj }

		with open(f"{dir}liste.conf", 'w') as configfile:
			config.write(configfile)

			print("finish")
class csf: 

	def resarch(*, console = "", jeu):
		"""
		fonction de recherche, il faut 
		"""
		console = console.upper()
		config = configparser.ConfigParser()

		config.read(f"console.conf")
		dirj = config.get(console, "dir-jeu")
		config.read(f"{dirj}liste.conf")
		if jeu.upper() in config:
			print("OK")
		else:
			print("nope")
		

		

	def autoconf():
		pass


conf.console(nom="NES", locj="D:/Arcade/nintendo/NES", nemu1= "ABS", cmd1="ABS", dsc="Console de 83 de nintendo, probablement l'une des meilleur console")
conf.jeu(dir = "D:/Arcade/nintendo/NES/", nom = "ARessha", dirj = "D:/Arcade/nintendo/NES/A/A Ressha de Ikou (Japan).zip")
csf.resarch(console = "nes", jeu = "A Ressha")