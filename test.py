from translate import Translator

translator= Translator(from_lang="uz",to_lang="en")
translation = translator.translate("bir yuz o`n bir")
print(translation)