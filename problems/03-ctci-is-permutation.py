def is_permutation(a = None, b = None):
	if len(a) != len(b):
		return False

	counts = {}
	for char in a:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1

	for char in b:
		if char not in counts:
			return False

		count = counts[char] - 1
		if counts[char] == 0:
			del counts[char]
		else:
			counts[char] = count

	return True


if __name__ == "__main__":
    print(is_permutation('aba', 'baa'))
    