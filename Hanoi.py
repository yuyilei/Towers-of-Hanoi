def output(num,a,b) :
    print "Move disk" , num , "from peg " ,a , "to peg" ,b 

def move(num,frompeg,to,transition) :
    if num == 1 : 
        output(num,frompeg,to)
    else :
        move(num-1,frompeg,transition,to) 
        output(num,frompeg,to) 
        move(num-1,transition,to,frompeg)

if __name__ == '__main__' :
    n = input("Enter the number of discs: ") 
    d = { 'a':'A', 'b':'B' , 'c':'C'} 
    print "The sequence of moves involved in the Tower of Hanoi are :" 
    print 
    move(n,d['a'],d['b'],d['c']) 
    print 
    print "The steps of moving " , n , "dics from A to B are" , 2**n-1 
