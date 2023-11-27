from primes import primes
p = primes(10)
for prime in p:
    residues = set() 
    for i in range(1,prime):
        q = i**2
        i = q
        while i - prime >= 0:
            i = i - prime
        residues.add(i)
