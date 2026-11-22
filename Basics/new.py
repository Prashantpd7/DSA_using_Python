MAX = 5

stack = [None] * MAX
top = -1

def push(item):
    global top
    if top == MAX - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print(f"Deleted: {stack[top]}")
        top -= 1

def display():
    if top == -1:
        print("Stack is Empty")
    else:
        for i in range(top, -1, -1):
            print(stack[i])

def main():
    push(10)
    push(20)
    push(30)

    display()
    pop()
    display()

if __name__ == "__main__":
    main()
