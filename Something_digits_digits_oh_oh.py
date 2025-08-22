def verifier(index):
    print("Make sure you only enter a number")
    while True:
        try:
            number = int(input(f"Enter the {index}{"st" if index==1 else "nd"} number:"))
            break
        except ValueError:
            print("You feed something other than numbers didn't you? 😡😡😡🥀🥀🥀🥀")
            print("Try again!!!")
    return number



def heavy_worker(first_number, second_number):
    smaller_number=first_number if first_number<=second_number else second_number
    larger_number=first_number if first_number>=second_number else second_number
    the_number_line=""
    for i in range(smaller_number+1,larger_number):
        the_number_line+=str(i)
    print(len(the_number_line))



def main():
    print("in this program you'll feed the program (that is me😩🥵), to numbers and I'll tell you the number of digits between the two numbers if we make a word out of all the numbers")
    print("Example:\nfrom 1-20:\n2345678910111213141516171819\nSo the number of digits in between is 28")

    first_number=verifier(1)
    second_number=verifier(2)
    heavy_worker(first_number, second_number)
if __name__ == "__main__":
    main()

draft_matrix=[[1,2,3,12,57,76],    #11,12,13,14,15,16,26,36,46,45,44,43,42,41,31,21,22,23,24,25,35,34,33,32
              [4,5,6,45,98,30],    #11,12,13,14,15,16,26,36,35,34,33,32,31,21,22,23,24,25
              [7,8,9,67,10,11],    #3x6----2x5
              [0,9,6,45,34,23]]    #4x6----3x2

def invigilation(index):   #This function has No business being here, I'm writing it here just to practice importing function from one program to another
    print("Make sure you only enter a number")
    while True:
        try:
            number = int(input(f"Number of {"Rows: " if index==1 else "Columns:"}"))
            break
        except ValueError:
            print("You feed something other than numbers didn't you? 😡😡😡🥀🥀🥀🥀")
            print("Try again!!!")
    return number



def verifier_for_matrix(i,j): #This function has No business being here, I'm writing it here just to practice importing function from one program to another
    print("Make sure you only enter a number")
    while True:
        try:
            number = float(input(f"enter element number ({i}x{j}): "))
            break
        except ValueError:
            print("You feed something other than numbers didn't you? 😡😡😡🥀🥀🥀🥀")
            print("Try again!!!")
    return number

def matrix(rows,columns):#This function has No business being here, I'm writing it here just to practice importing function from one program to another
    matrixx=[]
    print("I want you to type in the elements now")
    for i in range(1,rows+1):
        row=[]
        for j in range(1,columns+1):
            row.append(verifier_for_matrix(i,j))
        matrixx.append(row)
    return matrixx

