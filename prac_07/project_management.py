"""
CP1404 Practical 07 - Project Management
Estimate: 70 minutes
Actual: 90 minutes
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    """Main function to manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    if projects:
        print(f"Loaded {len(projects)} projects from {FILENAME}.")
    else:
        print(f"No projects loaded from {FILENAME}.")
    display_menu()
    choice = input(">>> ").strip().upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice. Please enter a valid menu option.")

        display_menu()
        choice = input(">>> ").strip().upper()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice in ['y', 'yes']:
        save_projects(projects, FILENAME)

    print("Thank you for using custom-built project management software.")





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
    projects = []
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

def display_projects(projects, filtered=False):
    """Display all the projects and their details """
    if not projects:
        print("No projects to display.")
        return
    if not filtered:
        incomplete_projects = sorted([project for project in projects if not project.is_complete()])
        completed_projects = sorted([project for project in projects if project.is_complete()])
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")
    else:
        for project in projects:
            print(f"  {project}")



def filter_projects_by_date(projects):
    """filter the user input date """
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date >= start_date]
        display_projects(filtered_projects, filtered=True)
    except ValueError:
        print("Invalid date format.")


def add_new_project(projects):
    """adding the new projects into the list """
    print("Let's add a new project")
    name = input("Name: ").strip()
    date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        projects.append(Project(name, start_date, priority, cost, completion))
    except ValueError:
        print("Invalid input. Project not added.")

def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)
            new_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")

            if new_percentage:
                project.completion_percentage = int(new_percentage)
            if new_priority:
                project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid choice or input.")





main()