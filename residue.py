from primes import primes
number = input("Choose an upper bound: ")
p = primes(int(number))
for prime in p:
    residues = set() 
    nonresidues = set(range(1,prime))
    for i in range(1,prime):
        i = i**2
        while i - prime >= 0:
            i = i - prime
        residues.add(i)
        nonresidues.discard(i)
    if nonresidues == set():
        nonresidues = "There are no quadratic nonresidues for this prime."
    print(prime, residues, nonresidues)
