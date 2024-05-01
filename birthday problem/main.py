import canonical
import strong
import matching
import triplet
import math


#returns the empirical probability of the function returning true over the sample "sample"
def probability(n,sample,function):
    count = 0
    for i in range(sample):
        if function(n):
            count += 1
    return (count/sample)

nb = 10000
print("Simulations : \n\nCanonical birthday,",nb,"simulations")
for n in [2,3,4,5,10,20,23,30,50]:
    p = probability(n,nb,canonical.duplicate)
    display = "n = " + str(n) + " p = " + str(p)
    if p != 0:
        display = display + " intervalle 95: " + str([p-1/(2*math.sqrt(math.sqrt(p*(1-p))*nb)),p+1/(2*math.sqrt(math.sqrt(p*(1-p))*nb))])

    print(display)
    #print("n =",n,"p =", p, "intervalle 95:",[p-1/(2*math.sqrt(math.sqrt(p*(1-p))*nb)),p+1/(2*math.sqrt(math.sqrt(p*(1-p))*nb))])

nb = 100
print("\n \nStrong birthday,",nb,"simulations")

for n in [2000,2500,2700,2800,3000,3063,3064,3500,4000,4400]:
    p = probability(n,nb,strong.allshared)
    display = "n = " + str(n) + " p = " + str(p)
    if p != 0:
        display = display + " intervalle 95: " + str([p-1/(2*math.sqrt(math.sqrt(p*(1-p))*nb)),p+1/(2*math.sqrt(math.sqrt(p*(1-p))*nb))])

    print(display)

nb = 20000
print("\n\nUnrestricted matching problem,",nb,"simulations")

for k in [0,1,2,3,4,5,6]:
    p = probability(k,nb,matching.match)
    display = "k = " + str(k) + " p = " + str(p)
    if p != 0:
        display = display + " intervalle 95: " + str([p-1/(2*math.sqrt(math.sqrt(p*(1-p))*nb)),p+1/(2*math.sqrt(math.sqrt(p*(1-p))*nb))])

    print(display)
   
#triplet values a little lower than article, there must be a problem

nb = 5000
print("\n\nTriplet birthday,",nb,"simulations")
for n in [23,40,60,75,87,88,145]:
    p = probability(n,nb,triplet.triplet)
    display = "n = " + str(n) + " p = " + str(p)
    if p != 0:
        display = display + " intervalle 95: " + str([p-1/(2*math.sqrt(math.sqrt(p*(1-p))*nb)),p+1/(2*math.sqrt(math.sqrt(p*(1-p))*nb))])

    print(display)


