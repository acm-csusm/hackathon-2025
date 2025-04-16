def romanToNumeral(roman):
    index = 0
    total = 0

    while index < len(roman):
        current = charConversion(roman[index])
        if index + 1 < len(roman):
            if roman[index] == 'I' and roman[index + 1] != 'I':
                current = charConversion(roman[index + 1]) - 1
                index += 1
            elif roman[index] == 'X' and roman[index + 1] != 'X':
                current = charConversion(roman[index + 1]) - 10
                index += 1
            elif roman[index] == 'C' and roman[index + 1] != 'C':
                current = charConversion(roman[index + 1]) - 100
                index += 1

        total += current
        index += 1

    print(total)

def charConversion(char):
    if char == 'M':
        return  1000
    if char == 'D':
        return  500
    if char == 'C':
        return  100
    if char == 'L':
        return  50
    if char == 'X':
        return  10
    if char == 'V':
        return  5
    if char == 'I':
        return  1

romanToNumeral("XCIX")