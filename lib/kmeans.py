
class Kmeans:

	def __init__(self, k, data):
		r = ranger(len(data))
		random.shuffler(r)
		self.clusts = data.take(r[:k],0)



Kmeans(2,[ [0,1,2,3], [1,5,3,6] ])
