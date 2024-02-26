sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#replace exclamatory marks by space
sentence_replace = sentence.replace("!"," ")
print(sentence_replace)

#sentence assigned sentence_replace
sentence = sentence_replace

#change whole sentence to uppercase
sentence_uppercase = sentence.upper()
print(sentence_uppercase)

#reverse sentence
sentence_reverse = sentence[::-1]
print(sentence_reverse)
