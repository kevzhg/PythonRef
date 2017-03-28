#Hash Map

class HashMap:
		def __init__(self):
			self.size = 6
			self.map = [None]*self.size

		def _get_hash(self, key):
			hash = 0
			for char in str(key):
				hash += ord(char)
			return hash % self.size
		def add(self, key, value):
			key_hash = self._get_hash(key)
			key_value = [key,value]

			if self.map[key_hash] is None: #If cell is empty
				self.map[key_hash] = list([key_value])
				return True
			else:
				for pair in self.map[key_hash]:
					if pair[0] == key:
						pair[1] = value #If Key matches, update value corresponding to that key
						return True
				self.map[key_hash].append(key_value) #If new key, appending key-value pair
				return True
		def delete(self, key):
			key_hash = self._get_hash(key)

			if self.map[key_hash] is None:
				return False
			for i in range (0, len(self.map[key_hash])):
				if self.map[key_hash][i][0] == key:
					self.map[key_hash].pop(i)
					return True

		def pprint(self):
			print ('```````HM````````')
			for item in self.map:
				if item is not None:
					print(str(item))

h = HashMap()
h.add('Bob', '1')
h.add('Ming', '1')
h.add('Ming', '2')
h.pprint()
h.delete('Bob')
h.pprint()

