# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

# def isLatinSquare(lst):
#     # Your code goes here...
#     pass

def isLatinSquare(lst):
    N = len(lst)
    rows = []
    for i in range(N):
        rows.append(set([]))
    cols = []
    for i in range(N):
        cols.append(set([]))
    invalid = 0
    for i in range(N):
        for j in range(N):
            rows[i].add(lst[i][j])
            cols[j].add(lst[i][j])
  
            if (lst[i][j] > N or lst[i][j] <= 0) :
                invalid += 1
    numrows = 0
    numcols = 0
    for i in range(N):
        if (len(rows[i]) != N) :
            numrows+=1
        if (len(cols[i]) != N) :
            numcols+=1
    if (numcols == 0 or numrows == 0 and invalid == 0) :
        return True
    else:
        return False
 
a = isLatinSquare([  [ 5, 6, 7, 8 ],
             [ 6, 5, 7, 8 ],
             [ 7, 8, 5, 6 ],
             [ 8, 6, 7, 5 ] ])
print(a)