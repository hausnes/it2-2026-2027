'''
    https://projecteuler.net/problem=1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23. 

    Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())

'''
    Når me brukar betingelsen if i % 3 == 0 or i % 5 == 0, sjekkar me om eit 
    tal er eit multiplum av enten 3 eller 5. Dersom eit tal er eit multiplum 
    av begge (som 15, 30, 45, osv.), vil det fortsatt berre bli lagt til 
    summen éin gong.
'''