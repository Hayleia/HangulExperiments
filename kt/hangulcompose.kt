package hangul.compose

import kotlin.math.max
import hangul.base.*

fun remove(s: String, i: Int): String {
	return s.substring(0, max(0, s.length-i-1))
}

fun getActions(s: String, c: Char): Pair<Int, String> {
	// s is "at least the last 1 character of what's currently here"
	if (s.length == 0) {
		return Pair(0, ""+c)
	}
	val lastChar = s.last()
	val lastOrd = lastChar.toInt()

	if (lastChar in initials && c in medials) {
		return Pair(1, "${syllable(initials.indexOf(lastChar), medials.indexOf(c), 0)}")
	} else if (44032 <= lastOrd && lastOrd <= 55203) { // syllable
		val (ini, med, fin) = syllableBlocks(lastOrd)

		// underscore is a sentinel in the "finals" string
		if (c == '_')
			return Pair(0, ""+c)

		//  if there is no final and the new char is a final, merge
		if (fin == 0 && c in finals)
			return Pair(1, "${syllable(ini, med, finals.indexOf(c))}")

		// if there is already a final but it is mergeable with the new char into a composed final, merge
		if ((finals[fin] in finalComp) && c in finalComp[finals[fin]]!!.get(0)) {
			val tple = finalComp[finals[fin]]
			return Pair(1, "${syllable(ini, med, finals.indexOf(tple!!.get(1)[tple[0].indexOf(c)]))}")
		}

		// if there is a simple final and the new char is a medial, split the old syllable
		if (fin != 0 && finals[fin] !in finalCompRev && c in medials)
			return Pair(1, "${syllable(ini, med, 0)}${syllable(initials.indexOf(finals[fin]), medials.indexOf(c), 0)}")

		// if there is a composed final and the new char is a medial, split the old final
		if (finals[fin] in finalCompRev && c in medials)
			return Pair(1, "${syllable(ini, med, finals.indexOf(finalCompRev.getValue(finals[fin])[0]))}${syllable(initials.indexOf(finalCompRev.getValue(finals[fin])[1]), medials.indexOf(c), 0)}")

		// if no final yet, and current medial can be composed with new char, merge
		if (medials[med] in medialComp && c in medialComp.getValue(medials[med])[0] && fin == 0) {
			val tple = medialComp[medials[med]]
			return Pair(1, "${syllable(ini, medials.indexOf(tple!!.get(1)[tple[0].indexOf(c)]), 0)}")
		}
	}

	return Pair(0, ""+c)
}

fun typeChar(s: String, c: Char): String {
	val (rm, text) = getActions(s, c)
	return remove(s, rm) + text
}

fun typeSeq(s: String): String {
	var ret: String = ""
	for (i in 0..s.length-1) {
		ret = typeChar(ret, s[i])
	}
	return ret
}
