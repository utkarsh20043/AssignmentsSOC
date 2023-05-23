# RSA system:
#step 1: Generate two distinct primes p and q.

#step 2: Create N thru product of p and q, N = p*q.

#step 3: Select and integer e(given e = 65537) such that gcd(e, (p-1)(q-1)) = 1. ===> PublicKey ===> (e, N).

#step 4: compute d. using, d = (e^(-1))mod((p-1)*(q-1)) ===> d = rem(e^(-1), (p-1)*(q-1))

#Note1 : In python rem(a^b, c) can be given by pow(a, b, c).

#Note2 : encrypted message(m') = pow(m, e, N) & decrypted message(m) = pow(m', d, N) ===> PrivateKey ===> (d, N).

In the code, I have mentioned the steps numbered with instances in the class carrying out different functions. So when reading the program refer this readme file 
to understand which object has the classes, initialised.
