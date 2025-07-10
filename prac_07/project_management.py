"""
CP1404 Practical 07 - Project Management
Estimate: 70 minutes
Actual:  minutes
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"



def display_menu():
    """display the menu options"""
    print("- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")


def load_projects(filename):
    """load the projects from the txt file"""
    projects=[]
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                    name, start_date, priority, cost, completion_percentage = line.strip().split('\t')
                    project = Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(),
                                      int(priority), float(cost), int(completion_percentage))
                    projects.append(project)
    except FileNotFoundError:
         print(f"File {filename} not found.")
    return projects

def save_projects(projects,filename):
    """save the projects into file """
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

