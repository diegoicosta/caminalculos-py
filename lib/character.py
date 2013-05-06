class Character:

	def __init__(self, code, name, states):
		self.code = code
		self.name = name
		self.states = []
		for key, value in states.iteritems():			
			self.states.append(CharacterState(key,value))

	def state_names(self):
		return [s.label for s in self.states]

	def has_state(self, label):
		return label in self.state_names()

	def get_state(self, label):
		found = filter(lambda s: s.label == label, self.states )
		if len(found) > 0: return found[0] 



class CharacterState:

	def __init__(self,label, symbol):
		self.label = label
		self.symbol = symbol



