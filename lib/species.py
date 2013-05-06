class Species: 

	def __init__(self, code):
		self.code = code
		self.dic_character_states = {}

	def choose_state(self, character, state_label):
		self.dic_character_states[character.code] = [character, character.get_state(state_label)] 


	def character_state(self, character_code):
		return self.dic_character_states[character_code][1]

	def characters(self):
		return [charac_state for charac_state in self.dic_character_states.itervalues()]
