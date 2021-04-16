# Initial consonants, ordered for syllable creation
initials = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
# Medial vowels, ordered for syllable creation
medials = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
# Final consonants (including none), ordered for syllable creation
finals = '_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'

medialComp = {
	'ㅗ': ('ㅏㅐㅣ', 'ㅘㅙㅚ'),
	'ㅜ': ('ㅓㅔㅣ', 'ㅝㅞㅟ'),
	'ㅡ': ('ㅣ', 'ㅢ'),
}
finalComp = {
	'ㄱ': ('ㅅ', 'ㄳ'),
	'ㄴ': ('ㅈㅎ', 'ㄵㄶ'),
	'ㄹ': ('ㄱㅁㅂㅅㅌㅍㅎ', 'ㄺㄻㄼㄽㄾㄿㅀ'),
	'ㅂ': ('ㅅ', 'ㅄ'),
}
finalCompRev = {}
for first, (seconds, comps) in finalComp.items():
	for i in range(len(seconds)):
		finalCompRev[comps[i]] = (first, seconds[i])
medialCompRev = {}
for first, (seconds, comps) in medialComp.items():
	for i in range(len(seconds)):
		medialCompRev[comps[i]] = (first, seconds[i])

def syllable(ini, med, fin):
	return chr(ini*588 + med*28 + fin + 44032)

def syllableBlocks(syllOrd):
	initial = int((syllOrd-44032)/588)
	medial = int((syllOrd-44032-initial*588)/28)
	final = int((syllOrd-44032)%28)
	return (initial, medial, final)
