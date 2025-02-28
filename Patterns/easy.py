def square_pattern(n):
    for i in range(n):
        print("*"*n)
        
square_pattern(5)
print("====================================================================================")
def right_angle_triangle(n):
    for i in range((n+1)):
        print(i*"*")

right_angle_triangle(5)
print("right_angle_triangle====================================================================================")
def right_angle_triangle_number(n):
    for i in range(1,(n+1)):
        for j in range(1,i+1):
            print(j,end="")
        print()

right_angle_triangle_number(5)
print("====================================================================================")
def right_angle_triangle_number_repeat(n):
    for i in range((n+1)):
        print(f"{i}"*i)

right_angle_triangle_number_repeat(5)
print("====================================================================================")

def inverse_right_angle_triangle(n):
    for i in range((n+1),0,-1):
        print(i*"*")

inverse_right_angle_triangle(5)
print("====================================================================================")

def inverse_right_angle_triangle_number(n):
    for i in range((n+1),0,-1):
        for j in range(1,i):
            print(j,end="")
        print()

inverse_right_angle_triangle_number(5)
print("====================================================================================")

def euqilateral_angle_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*int((2*i)-1))

euqilateral_angle_triangle(5)
print("euqilateral_angle_triangle====================================================================================")

def right_angle_triangle_reverse(n):
    for i in range((n),0,-1):
        print(" "*(n-i)+"*"*int((2*i)-1))

right_angle_triangle_reverse(5)
print("====================================================================================")

def combined_triangle(n):
    right_angle_triangle(n)
    right_angle_triangle_reverse(n)

combined_triangle(5)
print("====================================================================================")

def right_roated_pyramid(n):
    right_angle_triangle(n)
    inverse_right_angle_triangle(n)


right_roated_pyramid(5)
print("====================================================================================")

def pattern_11(n):
    string_pattern ="10"*n
    counter=0
    for i in range(1,n):
        
        if i%2==1: end=i+1
        print(f"{string_pattern[i%2:end]}")
        
pattern_11(5)
print("pattern11====================================================================================")


def pattern_12(n):
    for i in range(1,n+1):

        for j in range(1,i+1):
            print(j,end=" ")
        print(". "*2*(n-i),end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        
        print()
pattern_12(4)
print("pattern12====================================================================================")


def pattern13(n):
    counter=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(counter,end=" ")
            counter+=1
        print()

pattern13(5)
        
print("pattern13====================================================================================")

def pattern14(n):
    for i in range(1, n):
        for j in range(65, 65+i):
            a = chr(j)
            print(a, end="")
        print()

pattern14(5)

print("pattern14====================================================================================")

def pattern15(n):
    for i in range(n,0,-1):
        for j in range(65, 65+i):
            a = chr(j)
            print(a, end="")
        print()

pattern15(5)

print("pattern15====================================================================================")

def pattern16(n):
    character=65
    for i in range(1,n):
        
        print(f"{chr(character)}"*i)
        character+=1

pattern16(5)

print("pattern16====================================================================================")

def pattern17(n):
    # def euqilateral_angle_triangle(n):
    # for i in range(1,n+1):
    #     print(" "*(n-i)+"*"*int((2*i)-1))

    for i in range(1,n):
        print(" "*(n-i),end="")
        for j in range(65,65+i):
        #     print(f"{j}",end="")
            print(f"{chr(j)}",end="")
        for j in range(65+i-2,64,-1):
            # print(f"{j}",end="")
            print(f"{chr(j)}",end="")
        print()

pattern17(5)

print("pattern17====================================================================================")


def pattern18(n):

    for i in range(1,n+1):

        for j in range(65+n-i,65+n):
            print(f"{chr(j)}",end="")
        print()

pattern18(5)

print("pattern18====================================================================================")


def pattern19(n):
    for i in range(n,0,-1):
        print(i*"*"+".."*(n-i)+i*"*")
    for j in range(1,n+1):
        print(j*"*"+".."*(n-j)+j*"*")
pattern19(5)

print("pattern19====================================================================================")

def pattern20(n):
    for i in range(1,n+1):
        print(i*"*",2*(n-i)*".",i*"*")
    for j in range(n,0,-1):
        print(j*"*",2*(n-j)*".",j*"*")
pattern20(5)

print("pattern20====================================================================================")

def pattern21(n):
    for i in range(1,n+1):
        if i==1 or i==n:
            print("* "*n)
        else:
            print("* "," "*(n-2),"*")
pattern21(5)

print(chr(65))
