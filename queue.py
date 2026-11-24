from collections import deque 
queue = deque()

def enqueue():
    ele=int(input('Enter Element to Append:'))
    queue.append(ele)
    print('Element Apended')

def dequeue():
    if len(queue) == 0:
        print('Queue is Empty')
    else:
        queue.popleft()
        print('Element Popped')

def peep():
    if len(queue) == 0:
        print('Queue is Empty')
    else:
        print('Queue Elements')
        for ele in queue:
            print(ele,end='\n')
while True:

    print('1.Enqueue\n2.Dequeue\n3.Peep\n4.Exit')

    choice = int(input('Enter Chioce:'))

    if choice==1:
        enqueue()

    elif choice==2:
        dequeue()

    elif choice==3:
        peep()

    elif choice==4:
        print('Exited...!')
        break

    else:
        print('Invalid Choice')