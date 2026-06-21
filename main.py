import argparse
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

def complexite_verbose(password):
    return f'Complexity --> {complexite(password)} possibilities'



def entropie(password):
    return f'Entropy --> {round(log2(complexite(password)),3)} bits'



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
    
    return f'Time to crack --> {" ".join(result_parts)}'


#Dash args
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password", type=str, help="Password to analyze")
parser.add_argument("-s", "--speed", type=int, help="Speed of bruteforce")

args = parser.parse_args()

if args.password is None:
    print("You must define a password using -p <password>")
else:
    print(f"Password : {args.password}")
    print("")
    # Automatically run both calculations since the password was provided
    print(complexite_verbose(args.password))
    print(entropie(args.password))
    if args.speed is not None:
        print(time_to_crack(args.password, args.speed))
