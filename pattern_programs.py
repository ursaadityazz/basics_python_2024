# i = 0
# for i in range(5):
#     for j in range(5):
#         print('*', end= '')

#     print()

# *****
# *****
# *****
# *****
# *****

# i = 0
# for i in range(5):
#     for j in range(i+1):
#         print('*', end= '')

#     print()

# *
# **
# ***
# ****
# *****

# i = 0
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print('*', end= '')

#     print()

# *****
# ****
# ***
# **
# *

i = 0
n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end= '')
    for j in range(i,n):
        print('*', end= '')

    print()

#  *****
#   ****
#    ***
#     **
#      *


# i = 0
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ', end= '')
#     for j in range(i,n):
#         print('*', end= '')
#     for j in range(i+1):
#         print('*', end= '')    

#     print()

#  ******
#   ******
#    ******
#     ******
#      ******

i = 0
n=5
for i in range(n):
    for j in range(i+1):
        print(' ', end= '')
    for j in range(i,n):
        print('*', end= '')
    for j in range(i+1):
        print('*', end= '')
    for j in range(i,n):
        print(' ', end= '')
    for j in range(i,n):
        print(' ', end= '')
    for j in range(i+1):
        print('*', end= '')
    for j in range(i,n):
        print('*', end= '')
  

    print()

#  ******          ******
#   ******        ******
#    ******      ******
#     ******    ******
#      ******  ******


