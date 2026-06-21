from math import log2

numbers = [chr(i) for i in range(48,58)]
caps = [chr(i) for i in range(65,91)]
lower = [chr(i) for i in range(97,123)]
specials = [chr(i) for i in range(33,48)] + [chr(i) for i in range(58,65)]\
    + [chr(i) for i in range(91,97)] + ["{","|","}"]
    

def complexite(password):
    num = False
    cap = False
    low = False
    spec = False
    possibilities = 0
    for c in password:
        if c in numbers and num == False:
            num = True
            possibilities += len(numbers)
        elif c in caps and cap == False:
            cap = True
            possibilities += len(caps)
        elif c in lower and low == False:
            low = True
            possibilities += len(lower)
        elif c in specials and spec == False:
            spec = True
            possibilities += len(specials)
    return possibilities**len(password)



def entropie(password):
    return f'{password} --> {round(log2(complexite(password)),3)} bits'



def time_to_crack(password,speed):
    years = 0
    weeks = 0
    days = 0
    hours = 0
    minutes = 0
    seconds = complexite(password)/speed
   
    if seconds > 31449600:
        years = seconds//31449600
        seconds -= 31449600*years
        
    if seconds > 604800 :
        weeks = seconds//604800
        seconds = 604800*weeks  
        
    if seconds > 86400:
        days = seconds//86400 
        seconds -= 86400*days
        
    if seconds > 3600 :
        hours = seconds//3600
        seconds -= 3600*hours
        
    if seconds > 60 :
        minutes = seconds//60 
        seconds -= 60*minutes
    
    time_units = {
        'years': years,
        'weeks': weeks,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': round(seconds, 2)
    }
    
    # Filter and format non-zero values
    result_parts = [f'{value} {unit}' for unit, value in time_units.items() if value > 0]
    
    return f'{password} --> {" ".join(result_parts)}'


#Tests

passwordA = "hello123"
passwordB = "I1mK.ng2"
passwordC = "12345678"
passwordD = "2qT$S~bIP6_2"
passwordE = "MAmaD0uSakirig@na"
attemps_per_sec = 10**9

print("Number of possibilities :")
print("-------------------------")
print(passwordA,"-->",complexite(passwordA),"possibilities")
print(passwordB,"-->",complexite(passwordB),"possibilities")
print(passwordC,"-->",complexite(passwordC),"possibilities")
print(passwordD,"-->",complexite(passwordD),"possibilities")
print(passwordE,"-->",complexite(passwordE),"possibilities")

print("")
print("Entropy (H = log2(N^L)) :")
print("--------------------------")
print(entropie(passwordA))
print(entropie(passwordB))
print(entropie(passwordC))
print(entropie(passwordD))
print(entropie(passwordE))

print("")
print("Time to crack password :")
print(time_to_crack(passwordA, attemps_per_sec))
print(time_to_crack(passwordB, attemps_per_sec))
print(time_to_crack(passwordC, attemps_per_sec))
print(time_to_crack(passwordD, attemps_per_sec))
print(time_to_crack(passwordE, attemps_per_sec))
