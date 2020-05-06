def is_unique(string = None):
	x = 0

	for char in string:
		i = ord(char) - 97
		if (x >> i) & 1 == 1:
			return False
		x ^= 1 << i

	return True


if __name__ == "__main__":
    print(is_unique('aba'))
    