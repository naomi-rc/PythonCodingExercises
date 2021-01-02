def convert(number):
    factors = {3:"Pling", 5:"Plang", 7:"Plong"}
    result = ""
    for factor, sound in factors.items():
        result += sound if number % factor == 0 else ""
    
    return result if result else str(number)
