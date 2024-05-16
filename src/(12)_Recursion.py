# (12)_Recursion


def hanoi(n,s,d,l):
    if n == 1:
        print('Move the disk from peg ' + s + ' to peg ' + d + '.')

    else: 
        hanoi(n-1,s,l,d) # move n-1 disks from s to l
        hanoi(1,s,d,l) # move 1 disk from s to d
        hanoi(n-1,l,d,s) # move n-1 disks from l to d

hanoi(3,'A','C','B')