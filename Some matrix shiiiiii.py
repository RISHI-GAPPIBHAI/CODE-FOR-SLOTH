from Something_digits_digits_oh_oh import invigilation,matrix

print("This is the solution to some matrix program kinda challenge sloth gave")


def inputs():
    print("For the starters,you gotta tell me the number of rows and columns that your matrix will have")
    rows = invigilation(1)
    columns = invigilation(2)
    print("So your matrix is of the form",rows,"x",columns)
    our_matrix=matrix(rows=rows,columns=columns)
    function_that_does_the_heavy_lifting(our_matrix,rows,columns)


def function_that_does_the_heavy_lifting(our_matrix,rows,columns):
    list_to_print= [our_matrix[0]]
    if rows%2==0:
        for i in range(1,rows):
            list_to_print.append(our_matrix[i][columns-1])
        for i in range(columns-2,-1,-1):
            list_to_print.append(our_matrix[rows-1][i])
        print("There's a flaw in my thinking..........")
        print(list_to_print)
    else:
        pass


inputs()
def main():
    pass
