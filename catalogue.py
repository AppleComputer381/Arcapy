import os

class files:
	"""
	s'occupe des fichiers pour faire un catalogue
	"""
	def listing(path):
		"""
		s'occuppe de toute la partie recherche, dans un fichier donner
		path --> la ou la fonction doit rechercher
		"""
		files= os.listdir(path)
		directory = {}
		for name in files:

			if len(os.listdir(f"{path}/{name}")) != 0:
				files2 = os.listdir(f"{path}/{name}")
				underfiles = []

				for name2 in files2:
					underfiles.append(name2)
				directory[name]=underfiles
				continue

			directory[""]= name
		return directory

	def sorting(files, lng: str):
		"""
		tri premierement par lettre si pas deja fait et ensuite tri par langue
		files --> fichiers que la fonction doit trier
		"""
		other = []
		sort = {}
		assert type(files) == dict, "files is not dict, it's impossible to sort"
		for name in files.keys():
			temp = []
			if name == "":
				other.append(files[name])
				continue

			for file in files[name]:
				if lng in file:
					temp.append(file)

			sort[name]= temp
			for otherfile in other:
				sort[otherfile[0]].append(otherfile)
		return sort



