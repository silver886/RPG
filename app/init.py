class player(object):
	"""docstring for player"""
	def __init__(self, name, hp, mp, exp):
		super(player, self).__init__()
		self.name = name
		self.hp = hp
		self.mp = mp
		self.exp = exp