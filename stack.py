stack = []

def pushElement():
    ele=int(input('Enter Element to Append:'))
    stack.append(ele)
    print('Element Pushed')

def popElement():
    if len(stack) == 0:
        print('Stack is Empty')
    else:
        stack.pop()
        print('Element Popped')

def peep():
    if len(stack) == 0:
        print('Stack is Empty')
    else:
        print('Stack Elements')
        for i in range(len(stack)-1,-1,-1):
            print(stack[i],end='\n')

while True:

    print('1.Push\n2.Pop\n3.Peep\n4.Exit')

    choice = int(input('Enter Chioce:'))

    if choice==1:
        pushElement()

    elif choice==2:
        popElement()

    elif choice==3:
        peep()

    elif choice==4:
        print('Exited...!')
        break

    else:
        print('Invalid Choice')