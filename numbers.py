"""
This program takes a target number, and a list of smaller numbers (cards), and attempts to find a way to combine those cards into the target, using only +-*/

It does this by combining each pair of cards (once for each operator), and then all of those results, and then again, until all cards have been combined

Example usages:
	$ python3 numbers.py 75 50 2 3 8 7 819      
	> Found: (((50 * 7) - (75 + 2)) * 3) = 819
	> Completed in 0.03 seconds

	$ python3 numbers.py 3 7 6 2 1 7 824
	> Closest result was 2 away. ((((7 + 3) * 6) - 1) * (7 * 2)) = 826
	> Completed in 8.50 seconds

"""


import sys, math, itertools, time

class Operation():
	def __init__(self, func, sign):
		self.func = func
		self.sign = sign

operations = [
	Operation(lambda x,y: x+y, "+"),
	Operation(lambda x,y: x-y, "-"),
	Operation(lambda x,y: x*y, "*"),
	Operation(lambda x,y: int(x/y) if x%y == 0 else 0, "/")
]

# A bunch is a group of cards, combined with operations to give a value
class Bunch():
	def __init__(self, value, used, prettyParts):
		self.value = value
		if value == 0: # not useful
			self.hash = 0
			return
		self.used = used 
		self.pretty = prettyParts
		self.hash = (value << len(cards)) + used # Duplicate bunches with the same value, using the same cards are irrelevant

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

	# Human readable method fo reaching found value
	def prettier(self, x):
		if x[1] == "":
			return str(x[0])
		#TODO: remove surplus brackets
		return "(%s %s %s)"%(self.prettier(x[0]), x[1], self.prettier(x[2]))

	# Check that two bunched do not use the same card
	def isCollision(self, b1, b2):
		if b1.value == 0 or b2.value == 0:
			return True
		return b1.used & b2.used != 0

	# Find all the different values that can be reached by combining two these two bunches with the operators
	def combine(self, b1, b2): #returns newBunches, Matched bunch
		newBunches = {}
		if self.isCollision(b1, b2):
			return newBunches, None

		bigBunch, smallBunch = (b1, b2) if b1.value > b2.value else (b2, b1)
		for op in operations:
			bunch = Bunch(op.func(bigBunch.value, smallBunch.value), bigBunch.used | smallBunch.used, (bigBunch.pretty, op.sign, smallBunch.pretty))
			if bunch.value == self.target: # Found the answer!
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
	target = int(sys.argv[-1])
	cards = [int(c) for c in sys.argv[1:-1]]
	Solution(cards, target)
	print("Completed in %.2f seconds" % (time.time() - start_time))