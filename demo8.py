#DSA

#stack-LIPO or FILO
#operations
#1)PUSH--->insert
#2)POP--->delete
#3)PEEK--->view top item

#isEMPTY-check stack empty
#SIZE-number of items

#PUSH-add an item at top
#1)create empty stack
#2)input value
#3)add value to stack
#4)print stack



#pseudocode
# push(data)
# if(stack is full):
#  print stack Overflow
# else:
#   top++
#   stack[top or index]=Data


#stack program
#code
stack=[]

while True:
    print("\n1.push 2.pop 3.peek 4.display 5.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        val=int(input("enter value"))
        stack.append(val)
        print("pushed",val)
    elif choice==2:
        if not stack:
            print("stack empty")
        else:
            print("popped",stack.pop())
    elif choice==3:
        if not stack:
            print("stack empty")
        else:
            print("top")
    elif choice==4:
        print("STack",stack)
    else:
        print("invalid choice")


#queue operation
#enqueue
#dequeue
#front/peek
#isEmpty
#size

queue=[]

while True:
    print("\n1.push 2.pop 3.peek 4.display 5.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        val=int(input("enter value"))
        queue.append(val)
        print("added",val)
    elif choice==2:
        if not queue:
            print("queue empty")
        else:
            print("removed",queue.pop())
    elif choice==3:
        if not queue:
            print("queue empty")
        else:
            print("top")
    elif choice==4:
        print("QUeue",queue)
    else:
        print("invalid choice") 
        
 
#circuler queue
#1)reuses empty spaces
#save money



#if front is free,rear can resue it


n=3
queue=[none]*3
front=0
rear=0

#insert
queue[rear]=10
rear=(rear+1)%size

    [10----]
[10,10----]
[10,20,.30---]
delete->10

[-20 30---]

important conditions
queue is full when (rear+1)%size==frozenset

queue is empty when frontsize

#deques
. if queue empty->print message
. start from front











