class Similarity:

	@staticmethod
	def tanimoto(e1, e2):
		for cs in e1.characters():
			count = Similarity.intersection(e1,e2)

		return float(count) / (22 - count)

	@staticmethod
	def intersection(e1, e2):
		count = 0
		for cs in e1.characters():
			if e2.character_state(cs[0].code).symbol == e1.character_state(cs[0].code).symbol:
				count += 1 
		return count
