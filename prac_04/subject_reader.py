"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """ read the file data and return to the main function """
    data = load_data()
    display_subjects(data)



def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME, 'r') as input_file:
     for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    return subjects


def display_subjects(data):
    """ display the final result """
    for subject in data:
        print(f"{subject[0]:<4} is taught by {subject[1]:<12} and has {subject[2]:>4} students")

main()

