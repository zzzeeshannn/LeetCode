class Trie:

	def __init__(self):
		self.root = dict()

	def insert(self, words):
		for word in words:
			current = self.root
			for char in word:
				if char not in current:
					current[char] = dict()
				current = current[char]
			current['*'] = '*'

	@lru_cache()
	def search(self, target):
		if target == '':
			return True

		result = False
		node = self.root

		for index, char in enumerate(target):
			if char not in node:
				break
			node = node[char]
			if '*' in node:
				result = result or self.search(target[index+1:])
				if result:
					break
		return result

class Solution:
	def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
		obj = Trie()
		obj.insert(words)
		final = []
		for word in words:
			node = obj.root
			for index , char in enumerate(word):
				node=node[char]
				if "*" in node:
					if index!=len(word)-1 and obj.search(word[index+1:]):
						final.append(word)
						break
		return final