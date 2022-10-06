# # Its base and height are both equal to n It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# # Write a program that prints a staircase of n size .

def staircase(n):
    stairs = ''
    for i in range(1, n + 1):
        stairs = ('#' * i) 
        print(f'{stairs :>{n}}')
        

staircase(6)
