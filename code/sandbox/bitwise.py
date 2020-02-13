


def myproduct(num1,num2):
    num1_temp = num1
    num2_temp = num2
    result = 0
    
    while (num1_temp >= 1):
        if num1_temp & 1:
            result = result + num2_temp
        num1_temp = num1_temp >> 1
        num2_temp = num2_temp << 1
        
    return result

print(myproduct(1000,2))




