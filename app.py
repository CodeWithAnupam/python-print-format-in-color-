fruits = ['mango', 'apple', 'grapes', ]

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple


print(P+"Sl. No. \tItem")

for i, e in enumerate(fruits):

    print(O,i+1,"\t\t", e.title())


