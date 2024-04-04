import canonical
import strong
import matching
import triplet
import math

#function doesn't work, just trying to verify article maths values but float too big
def calcul(n):
    s = 0
    m = 365
    for i in range(math.floor(n/2) + 1):
        s += math.factorial(m)*math.factorial(n)/(math.factorial(i)*math.factorial(n-2*i)*math.factorial(m-n+i)*2^i*m^n)
    return 1 - s


#returns the empirical probability of the function returning true over the sample "sample"
def probability(n,sample,function):
    count = 0
    for i in range(sample):
        if function(n):
            count += 1
    return (count/sample)

print("Simulations : \n\nCanonical birthday")
for n in [2,3,4,5,10,20,23,30,50]:
    print("n =",n,"p =", probability(n,10000,canonical.duplicate))

print("\n \nStrong birthday")

for n in [2000,2500,2700,2800,3000,3063,3064,3500,4000,4400]:
    print("n =",n,"p =", probability(n,100,strong.allshared))

print("\n\nUnrestricted matching problem")

for k in [0,1,2,3,4,5,6]:
   print("k =",k,"p =", probability(k,20000,matching.match))
#triplet values a little lower than article, there must be a problem
print("\n\nTriplet birthday")
for n in [23,40,60,75,87,88,145]:
    print("n =",n,"p =", probability(n,5000,triplet.triplet))


