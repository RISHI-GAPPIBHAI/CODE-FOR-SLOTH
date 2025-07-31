#This is the solution for the latest morphing challenge that sloth has given to his subscribers

#SOOO,let's start!!!!!
#OH,btw for the introductions,I'm Rishi :)

word1=input("Enter the first word: ").lower().strip()
word2=input("Enter the second word: ").lower().strip()
print("Just so you know,the 2nd word will be combined with the 1st one")
Morphine=""       #for the Morphed word.....I've named it morphine cause.......yeah
i=0
can_morph_till_here=0
Morphine_Supplier=""
for char in reversed(word1):
    Morphine_Supplier=char+Morphine_Supplier
    if Morphine_Supplier==word2[0:i+1]:
        can_morph_till_here=i
    i+=1
print(Morphine_Supplier)
print(can_morph_till_here)
if can_morph_till_here==0:
    Morphine=word1+word2
elif not can_morph_till_here==len(word2)-1:
    Morphine=word1+word2[can_morph_till_here+1:]
else:
    Morphine=word1
print(Morphine)
#DONE!!
#Keep up the good work sloth!!!