new_words = ["muon", "jet", "tau", "electron", "photon"]

#extract first letters of words longer than 3 chars

long_words = [w[0] for w in new_words if len(w) > 3]
print(long_words) 


lengths = {w:len(w) for w in new_words if len(w) > 3} 

print(lengths)

text = "mississippi"

#unique chars in a string
unique_chars = [x for i,x in enumerate(text) if x not in text[:i]]
"""
for x in text:
    if x not in unique_chars:
        unique_chars.append(x)
"""
print(unique_chars)

"""

numbers = [1,2,3,4,5,6,7]

#filter even nums

evens = [(n%2==0) for n in numbers]
print(evens)

words = ["Muon", "Electron", "Tau"]

lower = [w.lower() for w in words]

print(lower)

squares = {n: n**2 for n in numbers}
print(squares)

events = {
    "e1": 12,
    "e2": 45,
    "e3": 8,
    "e4": 60
}

high_pt = {k:v for k, v in events.items() if v>20}
print(high_pt)

#nested loops compre

pairs = [(x,y) for x in range(2) for y in range(3)]
print(pairs)


pt = [10, 35, 50, 5, 80]

selected = [x for x in pt if x > 25]
print(selected)

"""
