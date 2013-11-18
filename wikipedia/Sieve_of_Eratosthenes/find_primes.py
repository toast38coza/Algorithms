"""
Sieve of Eratosthenes
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Hat-tip: http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python

"""

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*i, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

    
if __name__ == "__main__":
    print primes_sieve(100)