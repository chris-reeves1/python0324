import os

subfolder = "feedback_files"

os.makedirs(subfolder, exist_ok=True)

# list of students
students = ["alice", "David", "James"]

def get_input(prompt): # wrapper - changes behaviour fo another function. 
    return input(prompt)


for student in students:
    print(f"\nEntering feedback for {student}: ")

    # General understanding
    understanding_level = get_input("Enter understanding level (1: basic, 2: good 3: excellent): ")
    contribution_level = get_input("Enter contribution level (1: min, 2: mod 3: high): ")
    completion_level = get_input("Enter completion level (1: partial, 2: most 3: all): ")

    # Learner punctuality and engagement
    punctuality_level = get_input("Enter punctuality level (1: basic, 2: good 3: excellent): ")
    engagement_level = get_input("Enter engagement level (1: basic, 2: good 3: excellent): ")

    # Recommendations on further learning
    further_learning = get_input("Enter further learning level (1: basic, 2: good 3: excellent): ")

    # map input to descritions
    understanding_descriptions = {"1": "basic understanding", "2": "good understanding", "3": "excellent understanding"}
    contribution_descriptions = {"1": "contributed when asked", "2": "moderately contributed to discussions", "3": "actively contributed and helped collegues"}
    completion_description = {"1": "completed some of the labs as required", "2": "completed most of the labs as required", "3": "went beyond the completion of the labs"}
    punctuality_description = {"1": "was sometimes punctual", "2": "was generally punctional", "3": "was always punctual"}
    engagement_description = {"1": "engaged to some extent", "2": "enaged well", "3": "was highly engaged"}
    further_learning_description = {"1": "the basics of python", "2": "intermediate areas of python", "3": "advanced areas in python"}
    learning_concepts = {"1": "iteration/conditionals/collections", "2": "functions/files/modules", "3": "OOP/testing"}


    # template for feedback
    feedback = f"General comments\n{student} demonstrated {understanding_descriptions[understanding_level]} of Python and general programming concepts. {student} {contribution_descriptions[contribution_level]} and {completion_description[completion_level]}.\n\n"
    feedback += f"Learner punctionality and Engagement\n{student} {punctuality_description[punctuality_level]} throughout the module and {engagement_description[engagement_level]}.\n\n"
    feedback += f"Recommendations on further learning\nContinue to practice {further_learning_description[further_learning]}, such as {learning_concepts[further_learning]}."

    # write the feedback to a file
    filename = os.path.join(subfolder, f"{student}_feedback.txt")
    with open(filename, "w") as file:
        file.write(feedback)
        print(f"Feedback for {student} written to file {filename}")