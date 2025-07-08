"""
CP1404 Practical 06 - languages
Estimate: 15 minutes
Actual:  19 minutes
"""

from programming_language import ProgrammingLanguage

def main():
    """create the programming lis t and print them """
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()



