from hangulbase import *

def typeChar(s, c):
	# s is current string, c is typed character
	if s == None or len(s) == 0:
		return c
	lastChar = s[-1]
	lastOrd = ord(lastChar)

	if lastChar in initials and c in medials:
		return f'{s[:-1]}{syllable(initials.index(lastChar), medials.index(c), 0)}'
	elif 44032 <= lastOrd <= 55203: # syllable
		initial, medial, final = syllableBlocks(lastOrd)

		# if there is no final and the new char is a final, merge
		if final == 0 and c in finals:
			return f'{s[:-1]}{syllable(initial, medial, finals.index(c))}'

		# if there is already a final but it is mergeable with the new char into a composed final, merge
		if finals[final] in finalComp and c in finalComp[finals[final]][0]:
			tple = finalComp[finals[final]]
			return f'{s[:-1]}{syllable(initial, medial, finals.index(tple[1][tple[0].index(c)]))}'

		# if there is a simple final and the new char is a medial, split the old syllable
		if final != 0 and finals[final] not in finalCompRev and c in medials:
			return f'{s[:-1]}{syllable(initial, medial, 0)}{syllable(initials.index(finals[final]), medials.index(c), 0)}'

		# if there is a composed final and the new char is a medial, split the old final
		if finals[final] in finalCompRev and c in medials:
			return f'{s[:-1]}{syllable(initial, medial, finals.index(finalCompRev[finals[final]][0]))}{syllable(initials.index(finalCompRev[finals[final]][1]), medials.index(c), 0)}'

		# if no final yet, and current medial can be composed with new char, merge
		if medials[medial] in medialComp and c in medialComp[medials[medial]][0] and final == 0:
			tple = medialComp[medials[medial]]
			return f'{s[:-1]}{syllable(initial, medials.index(tple[1][tple[0].index(c)]), 0)}'

	return f'{s}{c}'

def typeSeq(s):
	ret = None
	for c in s:
		ret = typeChar(ret, c)
	return ret
