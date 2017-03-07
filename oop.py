class Person(object):
	def __init__(self, name):
		self.name = name

	def identity(self):
		print('My name is {}'.format(self.name))


class SuperHero(Person):
	def  __init__(self, name, hero_name):
		super(SuperHero, self).__init__(name)
		self.hero_name = hero_name

	def identity(self):
		super(SuperHero, self).identity()
		print('... and I am {}'.format(self.hero_name))


corey = Person('Corey')
corey.identity()

wade = SuperHero('Wade', 'Deadpool')
wade.identity()
