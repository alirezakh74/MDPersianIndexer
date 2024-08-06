import codecs

input_file = codecs.open("input.txt", "r", encoding="utf-8")
text = input_file.read()
#print(text.encode('utf-8'))

index_file = open("index.txt", "w+")

counter = 0
first_peice = ""
second_peice = ""
for i, c in enumerate(text.encode("utf-8")):
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
        # if it is not last char
        if(len(list(enumerate(text.encode("utf-8")))) - 1 != i):
            index_file.write(str(temp) + ",")
        else:
            index_file.write(str(temp))
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
    for counter, j in enumerate(current_line_array):
        if(j == ""):
            continue
        if(j == "\n"):
            output_file.write(str(73) + ",")
            continue
        if(counter != len(current_line_array) - 1):
            output_file.write(str(j) + ",")
        else:
            # don't use comma after last character
            output_file.write(str(j))

# algorithm for set correct char(first, last, middle)

# remove last comma

# remove \n at end of index_array
# temp_array = []
# for i in index_array:
#     temp_array.append(i.replace('\n', ''))
#     print(i)

# index_array = temp_array

#output_file.write(chars_array)

#flush stuff on buffer to output.txt file
#output_file.flush()
output_file.close()
output_file = open("output.txt", "r")

# final output for set first, middle or last charactercurrent_line_array
final_output_file = open("final_output.txt", "w+")
lines = output_file.readlines()
for i, line in enumerate(lines):
    #print(str(i) + " and " + str(line))
    if(line == "\n"):
        continue
    current_line_array = line.split(",")
    for counter, j in enumerate(current_line_array):

        # set andstring variable base on is it last or not char
        if counter == len(current_line_array) - 1:
            and_string = ""
        else:
            and_string = ", "

        # if counter == len(current_line_array) - 1:
        #     break
        # algorithm for select persian chars
        # if char is not ain, ghain and aa(first or second aa)
        number = int(j)
        if(number == 20 or number == 21 or number == 22 or number == 23 or number == 24 or number == 57):
            final_output_file.write(str(number) + and_string)
        elif((number != 1) and (number != 2) and (number != 35) and (number != 39)):
            # if char is last char in word or sentence
            if((counter == len(current_line_array) - 1) or (current_line_array[counter + 1] == str(72)) or (current_line_array[counter + 1] == str(73))):
                final_output_file.write(str(number + 1) + and_string)
            else:
                final_output_file.write(str(number) + and_string)
        # if char is first aa
        elif(number == 1):
             # if char is first char in word and sentence
            #if(counter == 0 or current_line_array[counter - 1] == 72):
            #    final_output_file.write(str(number) + and_string)
            final_output_file.write(str(number) + and_string)
        # if char is second aa(2 that actually can be sticky or not (can be 2 or 3))
        elif(number == 2):
            # if not first char and prevous char Dall Zaal Re Ze jhe Vaav AA
            if((counter != 0 and current_line_array[counter - 1] != str(72)) and (current_line_array[counter - 1] != str(1) and current_line_array[counter - 1] != str(20) and current_line_array[counter - 1] != str(21) and current_line_array[counter - 1] != str(22) and current_line_array[counter - 1] != str(23) and current_line_array[counter - 1] != str(24) and current_line_array[counter - 1]  != str(57))):
                final_output_file.write(str(number+1) + and_string)
            else:
                final_output_file.write(str(number) + and_string)
        # if char is aain or ghain
        elif(number == 35 or number == 39):
            # if it is first char (index is zero or prevous char is space or it is not last char)
            if(counter == 0 or current_line_array[counter - 1] == str(72) or current_line_array[counter - 1] == str(72)):
                final_output_file.write(str(number) + and_string)
            elif(counter == len(current_line_array) - 1 or current_line_array[counter + 1] == str(72) or current_line_array[counter + 1] == 73):
                if(current_line_array[counter - 1] == str(1) or current_line_array[counter - 1] == str(2) or current_line_array[counter - 1] == str(20) or current_line_array[counter - 1] == str(21) or current_line_array[counter - 1] == str(22) or current_line_array[counter - 1] == str(23) or current_line_array[counter - 1] == str(24) or current_line_array[counter - 1] == str(57)):
                    final_output_file.write(str(number + 3) + and_string)
                else:
                    final_output_file.write(str(number + 2) + and_string)
            else:
                final_output_file.write(str(number + 1) + and_string)

input_file.close()
index_file.close()
output_file.close()
final_output_file.close()




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