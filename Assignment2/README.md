***For amicable pairs, the logic is that we run the loop for only one of the two numbers in the pair. The second number is dependent on whether first number is able 
to form a number by summing it's divisors, which also satisfies the same condition. to ensure this I have put SUM of number as input to sum of divisors function defined
and this should be equal to the number itself. the greater than condition in if statement is to ensure repition does not occur.

***Modified cloud server is made using sage math function factor(). The factor() function gives factors in multiplied format which are needed to be converted into 
list as given in the question, so I used a list comprehension in Python.

***In carmichael number, is an odd composite number n which satisfies Fermat's little theorem
 a^(n-1)-1=0 (mod n) 	
for every choice of a satisfying (a,n)=1 (i.e., a and n are relatively prime) with 1<a<n. Hence I used the sage math function 'all' to check whether 
the iterator condition is true or false. Rest is just mathematical equation mentioned above is used in if statement.
