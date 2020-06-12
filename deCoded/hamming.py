def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) == len(strand_b):
        for i in range(0,len(strand_a)):
            print(f"ARE {strand_a[i]} AND {strand_b[i]} EQUAL?")
            if strand_a[i] == strand_b[i]:
                print("YES THEY ARE!!")
            else: 
                print("NO THEY ARE NOT")    
                hamming_distance+=1

    else:
        print(f"{strand_a} AND {strand_b} ARE NOT EQUAL IN LENGTH. PLEASE ENTER SEQUENCES OF EQUAL LENGTH.")   

    return hamming_distance

print(distance("GAGCCTACTAACGGATCT","CATCGTAATGACGGCCT"))