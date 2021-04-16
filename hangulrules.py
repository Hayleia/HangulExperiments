from hangulbase import *

def rule(c1, c2, res):
	print(f'"{c1}{c2}": "{res}",')

# basic rules where characters are simply added to the previous syllable
for i in range(44032, 55203+1):
	c = chr(i)
	if c not in ksx1001:
		continue

	initial, medial, final = syllableBlocks(i)

	if final != 0:
		if finals[final] in finalCompRev:
			c1 = syllable(initial, medial, finals.index(finalCompRev[finals[final]][0]))
			c2 = finalCompRev[finals[final]][1]
			rule(c1, c2, c)
		else:
			c1 = syllable(initial, medial, 0)
			c2 = finals[final]
			rule(c1, c2, c)
	elif medial != 0:
		if medials[medial] in medialCompRev:
			c1 = syllable(initial, medials.index(medialCompRev[medials[medial]][0]), 0)
			c2 = medialCompRev[medials[medial]][1]
			rule(c1, c2, c)
		else:
			c1 = initials[initial]
			c2 = medials[medial]
			rule(c1, c2, c)

# rules where a medial was written after a syllable that had a final so that makes two syllables
for i in range(44032, 55203+1):
	c = chr(i)
	if c not in ksx1001:
		continue

	initial, medial, final = syllableBlocks(i)

	if final == 0:
		continue

	if finals[final] in finalCompRev:
		for m in [v for v in medials if v not in medialCompRev]:
			res1 = syllable(initial, medial, finals.index(finalCompRev[finals[final]][0]))
			res2 = syllable(initials.index(finalCompRev[finals[final]][1]), medials.index(m), 0)
			rule(c, m, f'{res1}{res2}')
	else:
		for m in [v for v in medials if v not in medialCompRev]:
			res1 = syllable(initial, medial, 0)
			res2 = syllable(initials.index(finals[final]), medials.index(m), 0)
			rule(c, m, f'{res1}{res2}')
