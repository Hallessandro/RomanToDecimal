def RomanToDecimal(number):
    final_number = 0
    for x in range(len(number)):
        try:
            result = next_numb(number[x], number[x+1])
            if(result != 0):
                if(x-1 < 0):
                    final_number += result
                else:
                    final_number += previous_numb(number[x], number[x - 1])
            else:
                final_number += 0
        except IndexError:
            try:
                final_number += previous_numb(number[x], number[x - 1])
            except IndexError:
                final_number += convert(number[x])

    return final_number

def next_numb(number, next):
    if convert(next) > convert(number):
        return 0
    else:
        return convert(number)

def previous_numb(number, previous):
    if(convert(previous) < convert(number)):
        return convert(number) - convert(previous)
    else:
        return convert(number)

def convert(value):
    if (value == "I"):
        return 1
    elif (value == "V"):
        return 5
    elif (value == "X"):
        return 10
    elif (value == "L"):
        return 50
    elif (value == "C"):
        return 100
    elif (value == "D"):
        return 500
    elif (value == "M"):
        return 1000
