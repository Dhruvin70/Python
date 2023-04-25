import string

readingFile = open("18887916.txt","r")
# print(readingFile.read())
text = readingFile.read()

for i in text:
    if i in string.punctuation:
        text = text.replace(i,"")
# print(text)

raw_words = text.split()
for i in raw_words:
   eaw_list = raw_words

# print(eaw_list)
my_dict = {}

"""
Create a key-value dictionary
Create a list of words by using seperate "blank space"
Iterate through the list and dictionary
Check if keyword is present in dictionary or not
If present, increase value counter
If not, add a new key with keyword as value, and counter as 1

"""
for word in eaw_list:
    if word in my_dict:
        my_dict[word] +=1
    else:
        my_dict[word] = 1
print(my_dict)

for key,value in my_dict.items():
    print(key,":", value)