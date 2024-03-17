# https://github.com/linuxscout/pyarabic المصدر

# Diacritics
FATHATAN = u'\u064b'
DAMMATAN = u'\u064c'
KASRATAN = u'\u064d'
FATHA = u'\u064e'
DAMMA = u'\u064f'
KASRA = u'\u0650'
SHADDA = u'\u0651'
SUKUN = u'\u0652'

TASHKEEL = (FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA, SUKUN, SHADDA)

TATWEEL = u'\u0640'

bad_words = ['ختفوووو', 'كىىى', 'اشخطك', 'ياديوث', 'كسمك', 'المتىْاكه', 'الزنا', 'شرموطه', 'اهنيك', 'الديوتْ', 'القحىِه', 'الشرموطه', 'ياقحبه', 'العاهره', 'مص', 'عيري', 'واتفل', 'قحبه', 'قحبة', 'ياقواده', 'وشتمتك', 'السٌرموطه', 'يكسمك', 'خرق', 'انيك', 'الجراره', 'جرار', 'وكىىىمها', 'اللعن', 'القواد', 'بكىىىها', 'كىىىىمك', 'ترضع', 'الخضوع', 'اىْيك', 'ياقحىِه', 'رْبي', 'الدىِوث', 'العن', 'فحول', 'ونيكه', 'بلعن', 'تنبح', 'ياخنيث', 'الزنوه', 'مصي', 'الـةـواد', 'امك', 'المنيوكه', 'الديوث', 'وانىِكك', 'الشرموطة', 'زنوه', 'انىِك', 'الجرار', 'كس', 'سٌرموطه', 'شرموط', 'الرْنا', 'كىىىمك', 'قحىِه', 'ياجرار', 'بخرقه', 'زبي', 'القحبه', 'المحنه', 'ىْيكة', 'قحيب', 'بنيك', 'بكسمك', 'خصيانه', 'كسم']

class Word():
	def is_tashkeel(archar):
		"""Checks if the given ``archar`` Arabic Tashkeel Marks (
			- FATHA, DAMMA, KASRA, SUKUN,
			- SHADDA,
			- FATHATAN, DAMMATAN, KASRATAn)."""
		return archar in TASHKEEL

	def is_vocalized(word):
		"""Checks if the arabic word is vocalized.
		the word musn't  have any spaces and pounctuations.
		@param word: arabic unicode char
		@type word: unicode
		@return: if the word is vocalized
		@rtype:Boolean
		"""
		if word.isalpha():
			return False
		for char in word:
			if Word.is_tashkeel(char):
				break
		else:
			return False
		return True

	def strip_tatweel(text): # هذي تشيل التطويل من الحروفــــــــــــ
		"""
		Strip tatweel from a text and return a result text.

		Example:
			>>> text = u"العـــــربية"
			>>> strip_tatweel(text)
			العربية

		@param text: arabic text.
		@type text: unicode.
		@return: return a striped text.
		@rtype: unicode.

		"""
		text = text.replace(TATWEEL, '')

		if not text:
			return text
		elif Word.is_vocalized(text):
			for char in TASHKEEL:
				text = text.replace(char, '')
		return text

	def BadWord(text): # هنا فلتر الكلام الوصخ اذ كانت صح معناه فيه كلام مو زين والعكس # from MrXD
		"""
		هاذي دالة فلتر الكلام اذ كلام وصخ يعطيك True
		واذ كان مافيه يعطيك False
		"""
		msg = Word.strip_tatweel(text)
		msgcat = msg.split()
		for i in msgcat:
			if i in bad_words:
				return True
			else:
				return False