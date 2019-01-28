from collections import deque

# un deque es una lista iterable que puede introducirse valores tanto
# por delante o por detras. 


d = deque("amor")

for elem in d:
	print(elem.upper())

d.append('a')                    # add a new entry to the right side
d.appendleft('z')                # add a new entry to the left side

print(d)

print(d.pop())                        # return and remove the rightmost item
print(d.popleft())                    # return and remove the leftmost item

print(d)

print('z' in d)                         # search the deque

d.extend("xxx")                  # add multiple elements at once
print(d)
d.rotate(3)                      # right rotation
print("colocar a la derecha tres elementos ") 
print(d)
d.rotate(-3)                     # left rotation
print("colocar a la izquierda tres elementos ",) 
print(d)
d.pop()
d.pop()
d.pop()     # sacamos las x.
print("se borro? ",d)

reves = deque(reversed(d))               # make a new deque in reverse order
print("al reves ",reves)

lista = list(d)
print("pasando a lista ",lista)



