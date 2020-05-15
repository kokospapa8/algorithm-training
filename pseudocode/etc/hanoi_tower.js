def hanoi(n, a, b, c) {
    if(n <1) { return;}
    hanoi(n-1,a,c,b)
    console.log(n + " disk : " + a + "-> + c);
    hanoi(n-1,b,a,c)
    
/*
A, B, C :: n disks
        
1) move n-1 From A to B through C 
2) move nth disk from A to C
3) move n-1 disks to C through A

*/
