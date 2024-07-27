import codecs

f1 = codecs.open("test.txt", "r", encoding="utf-8")
text = f1.read()
print(text.encode('utf-8'))

f2 = open("output.txt", "w+")

counter = 0
first_peice = ""
second_peice = ""
for c in text.encode("utf-8"):
    print(c)
    temp = 0

    # if it is a space
    if c == 32:
        temp = 72 # index of space in persian font image tileset
        f2.write(str(temp) + "\n")
        continue

    # if it is english numbers
    if c == 48:
        temp = 62 # index of sefr
        f2.write(str(temp) + "\n")
        continue
    elif c == 49:
        temp = 63 # index of yek
        f2.write(str(temp) + "\n")
        continue
    elif c == 50:
        temp = 64 # index of do
        f2.write(str(temp) + "\n")
        continue
    elif c == 51:
        temp = 65 # index of se
        f2.write(str(temp) + "\n")
        continue
    elif c == 52:
        temp = 66 # index of chahar
        f2.write(str(temp) + "\n")
        continue
    elif c == 53:
        temp = 67 # index of paang
        f2.write(str(temp) + "\n")
        continue
    elif c == 54:
        temp = 68 # index of shesh
        f2.write(str(temp) + "\n")
        continue
    elif c == 55:
        temp = 69 # index of haaft
        f2.write(str(temp) + "\n")
        continue
    elif c == 56:
        temp = 70 # index of haasht
        f2.write(str(temp) + "\n")
        continue
    elif c == 57:
        temp = 71 # index of noh
        f2.write(str(temp) + "\n")
        continue


    if counter % 2 == 0:
        counter += 1
        first_peice = c
        continue
    else:
        counter += 1
        second_peice = c

    if first_peice == 216 and second_peice == 162:
        temp = 1 # index of aa ba kolah
    elif first_peice == 216 and second_peice == 167:
        temp = 2 # index of aa(as well for a, e, o)
    elif first_peice == 216 and second_peice == 168:
        temp = 4 # index of be
    elif first_peice == 217 and second_peice == 190:
        temp = 6 # index of pe
    elif first_peice == 216 and second_peice == 170:
        temp = 8 # index of te
    elif first_peice == 216 and second_peice == 171:
        temp = 10 # index of se
    elif first_peice == 216 and second_peice == 172:
        temp = 12 # index of jim
    elif first_peice == 218 and second_peice == 134:
        temp = 14 # index of che
    elif first_peice == 216 and second_peice == 173:
        temp = 16 # index of he
    elif first_peice == 216 and second_peice == 174:
        temp = 18 # index of khe
    elif first_peice == 216 and second_peice == 175:
        temp = 20 # index of daal
    elif first_peice == 216 and second_peice == 176:
        temp = 21 # index of zaal
    elif first_peice == 216 and second_peice == 177:
        temp = 22 # index of re
    elif first_peice == 216 and second_peice == 178:
        temp = 23 # index of ze
    elif first_peice == 218 and second_peice == 152:
        temp = 24 # index of jhe
    elif first_peice == 216 and second_peice == 179:
        temp = 25 # index of sin
    elif first_peice == 216 and second_peice == 180:
        temp = 27 # index of shin
    elif first_peice == 216 and second_peice == 181:
        temp = 29 # index of saad
    elif first_peice == 216 and second_peice == 182:
        temp = 31 # index of zaad
    elif first_peice == 216 and second_peice == 183:
        temp = 33 # index of taa
    elif first_peice == 216 and second_peice == 184:
        temp = 34 # index of zaa
    elif first_peice == 216 and second_peice == 185:
        temp = 35 # index of a'ain
    elif first_peice == 216 and second_peice == 186:
        temp = 39 # index of gh'ain
    elif first_peice == 217 and second_peice == 129:
        temp = 43 # index of fe
    elif first_peice == 217 and second_peice == 130:
        temp = 45 # index of ghaaf
    elif first_peice == 218 and second_peice == 169:
        temp = 47 # index of kaaf
    elif first_peice == 218 and second_peice == 175:
        temp = 49 # index of ghaaf
    elif first_peice == 217 and second_peice == 132:
        temp = 51 # index of laam
    elif first_peice == 217 and second_peice == 133:
        temp = 53 # index of meem
    elif first_peice == 217 and second_peice == 134:
        temp = 55 # index of noon
    elif first_peice == 217 and second_peice == 136:
        temp = 57 # index of vaav
    elif first_peice == 217 and second_peice == 135:
        temp = 58 # index of he
    elif first_peice == 219 and second_peice == 140:
        temp = 60 # index of ye
    # start persina numbers comparision
    elif first_peice == 219 and second_peice == 176:
        temp = 62 # index of sefr
    elif first_peice == 219 and second_peice == 177:
        temp = 63 # index of yek
    elif first_peice == 219 and second_peice == 178:
        temp = 64 # index of do
    elif first_peice == 219 and second_peice == 179:
        temp = 65 # index of se
    elif first_peice == 219 and second_peice == 180:
        temp = 66 # index of chahaar
    elif first_peice == 219 and second_peice == 181:
        temp = 67 # index of paanj
    elif first_peice == 219 and second_peice == 182:
        temp = 68 # index of shesh
    elif first_peice == 219 and second_peice == 183:
        temp = 69 # index of haaft
    elif first_peice == 219 and second_peice == 184:
        temp = 70 # index of haasht
    elif first_peice == 219 and second_peice == 185:
        temp = 71 # index of noh
    
    
    
    print(str(first_peice) + " and " + str(second_peice))
    f2.write(str(temp) + "\n")
    # f2.write("\n")
    # c = c + 2

# # while (c := text.encode('utf-8')):
# #     print(c)



f1.close()
f2.close()



# file = open("test.txt", "r", encoding="utf-8")
# str = file.read()
# print(str)
# for c in str:
#     print(c)
# file.close()



# Original string
# original_string = "آب"

# Encoding to UTF-8
# encoded_string = original_string.encode('utf-8')
# encoded_string = "آب".encode('utf-8')

# for c in encoded_string:
#     print(c)

# Displaying the result
#print("Original String:", original_string)
# print("Encoded String:", encoded_string)