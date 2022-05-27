import re
import string
'''
name = 'Sathe7sh'

#regex = re.compile('[A-Z]/\[0-9]')
full_name1 = 'Dhana'
#full_name2 = 'Dhana'
#char_avoid = set('/','[A-Z]','[0-9]')
for char in name:
    print(char)
    #if regex.search(char) == None:
    #if any(char in char_avoid):
    if re.match('^[A-Z0-9]', char):
        print("has special")
        continue
    else:
        print("No special")
            #full_name.join(char)
        full_name1 += char
    #full_name2 = full_name2 + full_name2.join(char)

print(full_name1)
#print(full_name2)

#for i in range(0,l):
#    if file_content[i] != '[A-Z]':
#        clean_text = file_content[i]
#regex = re.compile('[A-Z]/\[0-9]')
'''
seq_full = """ORIGIN
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
        61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""
seq_clean = ''.join(filter(str.isalpha, seq_full))
seq_clean = ''.join(filter(str.islower, seq_clean))
print(seq_clean)

str1 = "D343ssdf99gg"
str2 = str1.isalpha()
print(str2)