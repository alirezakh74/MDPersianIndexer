import codecs

input_file = codecs.open("input.txt", "r", encoding="utf-8")
text = input_file.read()
#print(text.encode('utf-8'))

index_file = open("index.txt", "w+")

counter = 0
first_peice = ""
second_peice = ""
for c in text.encode("utf-8"):
    #print(c)
    temp = 0

    # if it is a space
    if c == 32: # 32 is ascii number of space
        temp = 72 # index of space in persian font image tileset
        index_file.write(str(temp) + ",")
        continue

    # if it is english numbers
    if c == 48: # 48 is ascii number of zero
        temp = 62 # index of sefr
        index_file.write(str(temp) + ",")
        continue
    elif c == 49: # 49 is ascii number of one
        temp = 63 # index of yek
        index_file.write(str(temp) + ",")
        continue
    elif c == 50:
        temp = 64 # index of do
        index_file.write(str(temp) + ",")
        continue
    elif c == 51:
        temp = 65 # index of se
        index_file.write(str(temp) + ",")
        continue
    elif c == 52:
        temp = 66 # index of chahar
        index_file.write(str(temp) + ",")
        continue
    elif c == 53:
        temp = 67 # index of paang
        index_file.write(str(temp) + ",")
        continue
    elif c == 54:
        temp = 68 # index of shesh
        index_file.write(str(temp) + ",")
        continue
    elif c == 55:
        temp = 69 # index of haaft
        index_file.write(str(temp) + ",")
        continue
    elif c == 56:
        temp = 70 # index of haasht
        index_file.write(str(temp) + ",")
        continue
    elif c == 57:
        temp = 71 # index of noh
        index_file.write(str(temp) + ",")
        continue


    if counter % 2 == 0:
        counter += 1
        first_peice = c
        continue
    else:
        counter += 1
        second_peice = c
    
    # if it is a new line (\n)
    if first_peice == 13 and second_peice == 10: # 10 is ascii number of new line
        index_file.write(str("\n"))
        continue

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
    
    #print(str(first_peice) + " and " + str(second_peice))
    if temp != 0:
        index_file.write(str(temp) + ",")
    # index_file.write("\n")
    # c = c + 2

# # while (c := text.encode('utf-8')):
# #     print(c)


# algorithm for select between persian characters()
output_file = open("output.txt", "w+")
index_file.seek(0)
lines = index_file.readlines()
for i, line in enumerate(lines):
    if(line == "\n"):
        continue
    current_line_array = line.split(",")
    for j in current_line_array:
        if(j == ""):
            continue
        if(j == "\n"):
            output_file.write(str(73) + ",")
            continue
        if(i != len(lines)):
            output_file.write(str(j) + ",")
        else:
            # don't use comma after last character
            output_file.write(str(j))

# remove last comma

# remove \n at end of index_array
# temp_array = []
# for i in index_array:
#     temp_array.append(i.replace('\n', ''))
#     print(i)

# index_array = temp_array

#output_file.write(chars_array)


input_file.close()
index_file.close()
output_file.close()



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