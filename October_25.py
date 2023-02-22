# This program displays a stair-step pattern.


# num_steps = 6
# for r in range(num_steps):
#    for c in range(r):
#       print(' ', end='')
#    print('#')
   
   
# Excersize B 
base_size=10
for r in range(base_size,0):
    for c in range(r-1):
        print('*', end='')
    print()

# Excersize C
base_size=10
for r in range(base_size,0-1):
    for c in range(r):
        print('*', end='')
    print()
