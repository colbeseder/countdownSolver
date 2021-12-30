import sys, math, itertools, time

class Op():
	def __init__(self, func, sign):
		self.func = func
		self.sign = sign

ops = [
	Op(lambda x,y: x+y, "+"),
	Op(lambda x,y: x-y, "-"),
	Op(lambda x,y: x*y, "*"),
	Op(lambda x,y: int(x/y) if x%y == 0 else 0, "/")
]

class Bunch():
	def __init__(self, value, used, prettyParts):
		self.value = value
		if value == 0:
			self.hash = 0
			return
		self.used = used
		self.pretty = prettyParts
		self.hash = (value << 8) + used

class Solution():
	bunches = {}
	cards = []
	target = None
	closest = None
	distance = math.inf

	def __init__(self, cards, target):
		self.cards = cards	
		self.target = target
		for i, card in enumerate(cards):
			bunch = Bunch(card, 2**i, (str(card),"",""))
			self.bunches[bunch.hash] = bunch
		result = self.solve()
		if result:
			print("Found: %s = %s"%(self.prettier(result.pretty), target))
		elif self.closest:
			print("Closest result was %s away. %s = %s"%(self.distance, self.prettier(self.closest.pretty), self.closest.value))
		else:
			print("No solution found")

	def prettier(self, x):
		if x[1] == "":
			return str(x[0])
		return "(%s %s %s)"%(self.prettier(x[0]), x[1], self.prettier(x[2]))

	def isCollision(self, b1, b2):
		if b1.value == 0 or b2.value == 0:
			return True
		return b1.used & b2.used != 0

	def combine(self, b1, b2): #returns newBunches, Matched bunch
		newBunches = {}
		if self.isCollision(b1, b2):
			return newBunches, None

		bigBunch, smallBunch = (b1, b2) if b1.value > b2.value else (b2, b1)
		for op in ops:
			bunch = Bunch(op.func(bigBunch.value, smallBunch.value), bigBunch.used | smallBunch.used, (bigBunch.pretty, op.sign, smallBunch.pretty))
			if bunch.value == self.target:
				return {}, bunch
			dist = abs(target - bunch.value)
			if dist < self.distance:
				self.closest = bunch
				self.distance = dist
			newBunches[bunch.hash] = bunch
		return newBunches, None

	def solve(self):
		for i in range(len(self.cards)-1):
			newBunches = {}
			for pair in itertools.combinations(self.bunches, 2):
				combined, found = self.combine(self.bunches[pair[0]], self.bunches[pair[1]])
				if found:
					return found
				newBunches.update(combined)
			self.bunches.update(newBunches)
		return None

if __name__ == "__main__" :
	start_time = time.time()
	target = int(sys.argv[1])
	cards = [int(c) for c in sys.argv[2:]]
	Solution(cards, target)
	print("Completed in %.2f seconds" % (time.time() - start_time))


