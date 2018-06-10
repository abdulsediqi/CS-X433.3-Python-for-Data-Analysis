import numpy as np

#1.icnlude a section with your name 
Name = 'Abdul Sediqi'

#2 create matrix A with size (3,5) containing randow numbers 
A = np.random.randint(5,10,15).reshape(3,5)
print("A computes to:")
print (A)

#3 find the length and size of matrix A
print("The size of A is " +  str(A.size) +  "and the length of A computes to " + str (A.itemsize))

#4. Resize (crop) matrix A to size (3,4)
A = A[:, 0:4]
print("\nI get a cropped matrix A here:")
print (A)

#5. Find the transpose of matrix A and assign it to B
B = A.T
print("\nHere is the version for B:")
print(B)

#6. Find the minimum value in column 1 of matrix B
print("\nMatrix B minimum value in 1st column: " + str(B[:,1].min()))

#7. Find the minimum and maximum values for the entire matrix A
print("Minimum in Matrix A value is: " + str(A.min()))
print("Maximum value for matrix B: " + str(A.max()))

#8. Create a Vector X (an array) with 4 random numbers
X = np.random.randint(0,20,4)
print("\nVector X with an array of four random numbers:")
print(X)

#9. Create a function and pass Vector X and matrix A in it.
#10. In the new function multiply Vector X with matrix A and assign the result to D
def foo(g1,g2):
    return g1*g2
D = foo(X,A)
print("\nResult D from X and A:")
print(D)

#11. Create a complex number Z with absolute and real parts != 0
Z = 5 + 7j
print("\nHere is the result for Z: " + str(Z))

#12. Show its real and imaginary parts as well as its absolute value
print("The real value for Z computes to: " + str(Z.real))
print("The imaginary value for Z computes to: " + str(Z.imag))
print("Here is the absolute value for Z: " + str(abs(Z)))

#13. Multiple result D with the absolute value of Z and record it to C
C = D * abs(Z)
print("\nThe value of C computes to:")
print(C)

#14. Convert matrix B from a matrix to a string and overwrite B
B = B.tostring()
print("\nNow, here is the matrix B computing to a sting:")
print(B)

#15. Display a text on the screen: 'Name is done with HW2' but pass your 'Name' as a string variable
print("\n" + Name + " is done with HW2")

#16. Organize your code: use each line from this assignment as a comment line before each step.
#17. Save all steps as a script in .py file.
#18. Email me your .py file and screenshots of your running code before next class. I will run it

