STOP = "STOP"
CORRESPONDANCES = {"Methionine" : "AUG", "Phenylalanine" : "UUU, UUC", 
"Leucine" : "UUA, UUG", "Serine" : "UCU, UCC, UCA, UCG", 
"Tyrosine" : "UAU, UAC", "Cysteine" : "UGU, UGC", "Tryptophan" : "UGG", 
STOP : "UAA, UAG, UGA"}

def proteins(strand):
    proteins = []
    result = []
    strand_codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for codon in strand_codons:
        proteins += (protein for protein, codons in CORRESPONDANCES.items() if codon in codons)
        
    for protein in proteins:
        if protein == STOP:
            break
        result.append(protein)   
    return result   