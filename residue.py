from primes import primes
number = input("Choose an upper bound: ")
p = primes(int(number))
for prime in p:
    residues = set() 
    nonresidues = set(range(1,prime))
    for i in range(1,prime):
        q = i**2
        i = q
        while i - prime >= 0:
            i = i - prime
        residues.add(i)
        nonresidues.discard(i)
    print(prime, residues, nonresidues)
