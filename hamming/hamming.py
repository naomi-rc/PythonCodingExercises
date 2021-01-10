from operator import ne

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b): 
        raise ValueError("Strands are of unequal length")
    return sum(map(ne, strand_a, strand_b))