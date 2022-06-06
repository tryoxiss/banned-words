# first line CANNOT be anything BUT an import or comment I refuse to write code here

from turtle import clear


compiled = open("compiled.txt", "w")
rawlist = open("rawlist.txt", "r")

content = rawlist.readlines()
exclude = [',', ' ','.', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '&']

thisvariableistrue = True

for i in range(0, len(content)): # 500000
    if thisvariableistrue == True:
        if '-' in content[i]:
            i += 1
            continue
        elif '1' in content[i]:
            i += 1
            continue
        elif '2' in content[i]:
            i += 1
            continue
        elif '3' in content[i]:
            i += 1
            continue
        elif '4' in content[i]:
            i += 1
            continue
        elif '5' in content[i]:
            i += 1
            continue
        elif '6' in content[i]:
            i += 1
            continue
        elif '7' in content[i]:
            i += 1
            continue
        elif '8' in content[i]:
            i += 1
            continue
        elif '9' in content[i]:
            i += 1
            continue
        elif '0' in content[i]:
            i += 1
            continue
        elif '.' in content[i]:
            i += 1
            continue
        elif ',' in content[i]:
            i += 1
            continue
        elif '-' in content[i]:
            i += 1
            continue
        elif '&' in content[i]:
            i += 1
            continue
        elif '/' in content[i]:
            i += 1
            continue
        elif "'" in content[i]:
            i += 1
            continue
        elif 'A' in content[i]:
            i += 1
            continue
        elif 'B' in content[i]:
            i += 1
            continue
        elif 'C' in content[i]:
            i += 1
            continue
        elif 'D' in content[i]:
            i += 1
            continue
        elif 'E' in content[i]:
            i += 1
            continue
        elif 'F' in content[i]:
            i += 1
            continue
        elif 'G' in content[i]:
            i += 1
            continue
        elif 'H' in content[i]:
            i += 1
            continue
        elif 'I' in content[i]:
            i += 1
            continue
        elif 'J' in content[i]:
            i += 1
            continue
        elif 'K' in content[i]:
            i += 1
            continue
        elif 'L' in content[i]:
            i += 1
            continue
        elif 'M' in content[i]:
            i += 1
            continue
        elif 'N' in content[i]:
            i += 1
            continue
        elif 'O' in content[i]:
            i += 1
            continue
        elif 'P' in content[i]:
            i += 1
            continue
        elif 'Q' in content[i]:
            i += 1
            continue
        elif 'R' in content[i]:
            i += 1
            continue
        elif 'S' in content[i]:
            i += 1
            continue
        elif 'T' in content[i]:
            i += 1
            continue
        elif 'U' in content[i]:
            i += 1
            continue
        elif 'V' in content[i]:
            i += 1
            continue
        elif 'W' in content[i]:
            i += 1
            continue
        elif 'X' in content[i]:
            i += 1
            continue
        elif 'Y' in content[i]:
            i += 1
            continue
        elif 'Z' in content[i]:
            i += 1
            continue

    # if '-' in content[i]:
    #     i += 1
    #     continue

    compiled.write(content[i])

    # for j in range(0, 4):
    #     if exclude[j] in content[i]:
    #         pass
    #     else: 
    #         filtered.write(f"{content[i]}\n")