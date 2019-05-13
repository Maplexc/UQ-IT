def is_dna(string):
    # is a multiple of 3
    valid=[]
    if len(string)%3==0:
        for c in string:
            if c == 'A' or c == 'T' or c == 'G' or c == 'C':
                valid.append(True)
            else:
                valid.append(False)
        if all(valid):
            return True
        else:
            return False
    else:
        return False

    # A T C G




def is_dna_ans(string):
    if len(string)%3 != 0:
        return False
        # dont need to check anymore
    for c in string:
        if c not in ('A', 'T', 'C', 'G'):
            return False
        # if c == 'A' or "T" or "C" or "G" cannot write it like that, because bool('C') will return True, But bool('') will return False
    return True





def reverse_complement(dna):
    # A to T
    # T to A
    # C to G
    # G to C

    
    reverse_comp=''
    if is_dna_ans(dna) == False:
        return None
    #reverse string
    reverse_dna=dna[::-1]
    for c in reverse_dna:
        if c == 'T':
            reverse_comp+='A'
        elif c == 'A':
            reverse_comp+='T'
        elif c == 'C':
            reverse_comp+='G'
        elif c == 'G':
            reverse_comp+='C'
    return reverse_comp


def print_codons(dna):
    if is_dna(dna) == False:
        return None
    # loop
    # string splicing
    # print stuff
    num_codons=len(dna)/3
    start=0
    end=3+1
    while n<=num_codons:
        print(dna[start:end])
        start+=2

def print_codons_ans(dna):
    if is_dna(dna) == False:
        return None
    for i in range(0,len(dna),3):
        this_codon = dna [i:i+3]
        print (this_codon)

        
def get_number(string):
    first_number=''
    for c in string:
        if c.isdigit() or c == '-':
            first_number += c
            if first_number.isdigit() == False:
                break
    else:
        print
        return None
    return int(first_number)               
            
            


        
        
