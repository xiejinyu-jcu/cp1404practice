""" 1.Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
Use open and close for this question.
"""

name=input("Enter your name: ")
out_file=open("name.txt", 'w')
print(name, file=out_file)
out_file.close()


""" 2.In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
(or whatever the name is in the file). Do not simply print the user's input variable!"""

in_file=open("name.txt", 'r')
name=in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


"""3. Create a text file called and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens , reads only the first two numbers, adds them together then prints the result"""
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
    print(first_number+second_number)


"""4.Now write a fourth block of code that prints the total for all lines in .
 This should work for a file with any number of numbers. """
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)