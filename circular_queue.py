size = 5
queue = [None] * size
front = -1
rear = -1

def isEmpty():
    return front == -1

def isFull():
    return (rear + 1) % size == front

def getFront():
    if isEmpty():
        print('Queue is Empty')
        return -1
        
    print(f'Front Element: {queue[front]}')
    return queue[front]

def getRear():
    if isEmpty():
        print('Queue is Empty')
        return -1
        
    print(f'Rear Element: {queue[rear]}')
    return queue[rear]
    
def enqueue():
    global front, rear

    value = int(input('Enter value to enqueue: '))

    if isFull():
        print('Queue is Full, You cannot Enqueue...!')
        return

    if isEmpty():
        front=0
        rear=0
    else:
        rear = (rear+1) % size

    queue[rear] = value
    print(f'{value} Inserted to Queue.')

def dequeue():
    global front, rear

    if isEmpty():
        print('Queue is empty!')
        return

    removed_ele = queue[front]
    queue[front] = None

    if front==rear:
        front=-1
        rear=-1

    else:
        front = (front+1)%size

    print(f'{removed_ele} is removed from the Queue')
    return removed_ele

def display():
    if isEmpty():
        print('Queue is Empty')
        return

    print('Queue Elements: ',end='')
    
    i = front
    
    while True:
        print(queue[i],end=' ')
        if i == rear:
            break
        i=(i+1)%size
    print()

while True:

    print('====Menu====')
    print('1.Get Front\n2.Get Rear\n3.Enqueue\n4.Dequeue\n5.Display\n6.Exit')

    choice = int(input('Enter Chioce:'))

    if choice==1:
        getFront()

    elif choice==2:
        getRear()

    elif choice==3:
        enqueue()

    elif choice==4:
        dequeue()

    elif choice==5:
        display()

    elif choice==6:
        print('Exited...!')
        break

    else:
        print('Invalid Choice')