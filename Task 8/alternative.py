#This program has two parts.
#First part: 
#It takes a String (sentence) and iterates through
#its characters by converting the characters to
#upper and lower cases alternately.
#Second part:
#It takes a String (sentence) and iterates through
#the words in the String and converts the words
#into upper and lower cases alternately.

#First part
text = "Python is a wonderful programming language"
print(f"Original text: {text} ")

#To hold edited upper/lower case characters of text
text_edited = ''

for x in range(0,len(text)):
  if x % 2 == 0:
    #converts charcater to upper case if its index in the String is even number
    text_edited = text_edited + text[x].upper() 
  else:
    text_edited = text_edited + text[x].lower()

#copies words separated by white space into a list (text1_splitted_list)
text_splitted_list = text_edited.split(" ")
print(" ".join(text_splitted_list)) #joins all values in the list by inserting white spaces inbetween

#second code

print("\nOriginal text: {} ".format(text))

#declaring empty list
text_edited_list = []

#populating list with words from text separated by white space
text_list = text.split(" ")

for y in range(0,len(text_list)):
   if y % 2 == 0:
     text_edited_list.append(text_list[y].upper())#add words into list - index even
   else:
     text_edited_list.append(text_list[y].lower())#add words into list - index odd

print(" ".join(text_edited_list))
   
