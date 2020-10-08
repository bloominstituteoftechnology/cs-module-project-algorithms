def eating_cookies(n):
	s = [1, 2, 4]
	for i in range(0, n):
		s = [s[1], s[2], sum(s)]
	return s[2] - sum(s[:2])
