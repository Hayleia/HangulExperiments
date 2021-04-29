package hangul.base

// Initial consonants, ordered for syllable creation
val initials = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
// Medial vowels, ordered for syllable creation
val medials = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
// Final consonants (including none), ordered for syllable creation
val finals = "_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

val medialComp = mapOf(
	'ㅗ' to listOfNotNull("ㅏㅐㅣ", "ㅘㅙㅚ"),
	'ㅜ' to listOfNotNull("ㅓㅔㅣ", "ㅝㅞㅟ"),
	'ㅡ' to listOfNotNull("ㅣ", "ㅢ"),
)

val finalComp = mapOf(
	'ㄱ' to listOfNotNull("ㅅ", "ㄳ"),
	'ㄴ' to listOfNotNull("ㅈㅎ", "ㄵㄶ"),
	'ㄹ' to listOfNotNull("ㄱㅁㅂㅅㅌㅍㅎ", "ㄺㄻㄼㄽㄾㄿㅀ"),
	'ㅂ' to listOfNotNull("ㅅ", "ㅄ"),
)

private fun reverseComp(map: Map<Char, List<String>>): Map<Char, List<Char>> {
	val ret = mutableMapOf<Char, List<Char>>()
	for ((first, v) in map) {
		val (seconds, comps) = v
		for (i in 0..seconds.length-1) {
			ret[comps[i]] = listOf(first, seconds[i])
		}
	}
	return ret
}

val finalCompRev = reverseComp(finalComp)
val medialCompRev = reverseComp(medialComp)

fun syllable(ini: Int, med: Int, fin:Int): Char {
	return (ini*588 + med*28 + fin + 44032).toChar()
}

fun syllableBlocks(syllOrd: Int): List<Int> {
	val initial = (syllOrd-44032)/588
	val medial = (syllOrd-44032-initial*588)/28
	val fin = (syllOrd-44032)%28
	return listOf(initial, medial, fin)
}
