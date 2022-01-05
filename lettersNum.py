def to_letters (num):
    result = ""
    gn1 = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    gn2 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    gn3 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    if num < 10:
        result = gn1[num]
    elif num > 9 and num < 20 :
        result = gn3[num - 10]
    elif num > 19 and num <100:
        if num % 10 == 0:
            result = gn2[(num // 10) - 2]
        else:
            result = gn2[(num // 10) - 2] + " " + gn1[num % 10]
    else:
        result = "your number is not between 0 and 100"

    return result
        


print(to_letters(int(input("please enter a number between 0 and 100: "))))