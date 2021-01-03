FACTORS = {3: "Pling", 5: "Plang", 7: "Plong"}

def convert(number):    
    result = ''.join(
        sound for factor, sound in FACTORS.items() 
        if number % factor == 0
    )
    return result if result else str(number)