# time complexity : 2**n -1
# https://mathworld.wolfram.com/TowerofHanoi.html

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(n, from_pos, "->", to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)


/*
A, B, C :: n disks
        
1) move n-1 From A to B through C 
2) move nth disk from A to C
3) move n-1 disks to C through A

*/
