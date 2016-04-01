class player(object):
	"""docstring for player"""
	def __init__(self, name, hp, mp, exp):
		super(player, self).__init__()
		self.__name = name
		self.__hp = hp
		self.__mp = mp
		self.__exp = exp
		pass
	def info(self):
		
		print("Name:\t",  self.__name)

		pass


		
p1 = player("Silvester", 23, 45, 67)
p1.info()