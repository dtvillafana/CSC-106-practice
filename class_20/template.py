"""
CSC 106 Synthesis Project - Starter Template
Student Gradebook System
"""

# student_data.py
class Student:
    """Represents an undergraduate student with grades"""
    
    def __init__(self, name, student_id, major):
        """
        Initialize a student
        TODO: Set name, student_id, major attributes
        TODO: Initialize empty grades dictionary
        """
        pass
    
    def add_grade(self, course, score):
        """
        Add a grade for a course
        TODO: Add score to grades dictionary with course as key
        TODO: Consider validating score is between 0-100
        """
        pass
    
    def get_letter_grade(self, score):
        """
        Convert numeric score to letter grade
        TODO: Implement grade scale:
        - 90-100: A
        - 80-89: B
        - 70-79: C
        - 60-69: D
        - 0-59: F
        """
        pass
    
    def get_gpa(self):
        """
        Calculate GPA on 4.0 scale
        TODO: Use get_letter_grade to convert each score
        TODO: Calculate average: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
        TODO: Return 0.0 if no grades
        """
        pass
    
    def get_standing(self):
        """
        Get academic standing
        TODO: Return "Good Standing" if GPA >= 2.0
        TODO: Return "Academic Probation" otherwise
        """
        pass
    
    def __str__(self):
        """
        String representation of student
        TODO: Return formatted string with name, ID, major, GPA, standing
        """
        pass


class GraduateStudent(Student):
    """Represents a graduate student (inherits from Student)"""
    
    def __init__(self, name, student_id, major, thesis_topic="TBD"):
        """
        Initialize graduate student
        TODO: Call parent constructor
        TODO: Set thesis_topic attribute
        """
        pass
    
    def set_thesis_topic(self, topic):
        """
        Set thesis topic
        TODO: Update thesis_topic attribute
        """
        pass
    
    def get_gpa(self):
        """
        Calculate GPA with graduate grading scale
        TODO: Override parent method
        TODO: Use scale: A=4.0, B=3.5, C=2.5, D=1.0, F=0.0
        """
        pass


# gradebook.py
class Gradebook:
    """Manages a collection of students"""
    
    def __init__(self):
        """
        Initialize gradebook
        TODO: Create empty students dictionary (key: student_id, value: Student object)
        TODO: Create course_list with sample courses
        """
        pass
    
    def add_student(self, student):
        """
        Add a student to gradebook
        TODO: Check if student_id already exists
        TODO: Raise ValueError if duplicate
        TODO: Add to students dictionary
        """
        pass
    
    def remove_student(self, student_id):
        """
        Remove a student
        TODO: Check if student exists
        TODO: Raise KeyError if not found
        TODO: Remove from dictionary
        """
        pass
    
    def find_student(self, student_id):
        """
        EXTRA CREDIT:
        Find student using bisection search
        TODO: Get sorted list of student IDs
        TODO: Implement bisection search algorithm
        TODO: Return student if found, None otherwise
        """
        pass
    
    def get_top_students(self, n):
        """
        Get top n students by GPA
        TODO: Use sorted() with lambda key function
        TODO: Return list of top n students
        """
        pass
    
    def calculate_class_average(self):
        """
        Calculate average GPA of all students
        TODO: Sum all GPAs
        TODO: Divide by number of students
        TODO: Return 0.0 if no students
        """
        pass
    
    def get_students_by_standing(self):
        """
        Group students by academic standing
        TODO: Create dictionary with "Good Standing" and "Probation" keys
        TODO: Iterate through students and categorize
        TODO: Return dictionary with lists
        """
        pass
    
    def generate_statistics(self):
        """
        Generate overall statistics
        TODO: Calculate total students, average GPA, highest GPA, lowest GPA
        TODO: Return as tuple
        """
        pass
    
    def export_to_file(self, filename):
        """
        Export all student data to file
        TODO: Open file for writing
        TODO: Write each student's data
        TODO: Include error handling
        """
        pass
    
    def import_from_file(self, filename):
        """
        Import student data from file
        TODO: Open file for reading
        TODO: Parse each line and create Student objects
        TODO: Add to gradebook
        TODO: Include error handling
        """
        pass


# ============ main.py ============
def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("STUDENT GRADEBOOK SYSTEM")
    print("="*40)
    print("1. Add Student")
    print("2. Add Graduate Student")
    print("3. Record Grade")
    print("4. View Student")
    print("5. Remove Student")
    print("6. View Top Students")
    print("7. View Class Statistics")
    print("8. View Students by Standing")
    print("9. Search for Student (Bisection)") # EXTRA CREDIT
    print("10. Export Data")
    print("11. Import Data")
    print("12. Grade Distribution Analysis")
    print("13. Exit")
    print("="*40)


def add_student_interactive(gradebook):
    """
    Interactive function to add a student
    TODO: Prompt for name, ID, major
    TODO: Create Student object
    TODO: Add to gradebook with error handling
    """
    pass


def add_graduate_student_interactive(gradebook):
    """
    Interactive function to add a graduate student
    TODO: Similar to add_student_interactive
    TODO: Also prompt for thesis topic
    """
    pass


def record_grade_interactive(gradebook):
    """
    Interactive function to record a grade
    TODO: Prompt for student ID
    TODO: Find student
    TODO: Prompt for course and grade
    TODO: Add grade with validation
    """
    pass


def view_student_interactive(gradebook):
    """
    Interactive function to view a student
    TODO: Prompt for student ID
    TODO: Find and display student info
    TODO: Display all grades
    """
    pass


def grade_distribution_analysis(gradebook):
    """
    Analyze and display grade distribution
    TODO: Count A's, B's, C's, D's, F's across all students
    TODO: Display as formatted table
    """
    pass


def demo_system():
    """
    Demonstration of all system features
    TODO: Create gradebook
    TODO: Add 5 sample students
    TODO: Add grades for each
    TODO: Demonstrate each feature
    """
    print("Running demo...")
    # Create sample data
    gradebook = Gradebook()
    
    # TODO: Add students
    # TODO: Add grades
    # TODO: Display statistics
    # TODO: Test search
    # TODO: Export data
    
    print("Demo complete!")


def main():
    """Main program loop"""
    gradebook = Gradebook()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-13): ").strip()
            
            if choice == "1":
                add_student_interactive(gradebook)
            elif choice == "2":
                add_graduate_student_interactive(gradebook)
            elif choice == "3":
                record_grade_interactive(gradebook)
            elif choice == "4":
                view_student_interactive(gradebook)
            elif choice == "5":
                # TODO: Implement remove student
                pass
            elif choice == "6":
                # TODO: Implement view top students
                pass
            elif choice == "7":
                # TODO: Implement view statistics
                pass
            elif choice == "8":
                # TODO: Implement view by standing
                pass
            elif choice == "9":
                # TODO: Implement bisection search - EXTRA CREDIT
                pass
            elif choice == "10":
                # TODO: Implement export
                pass
            elif choice == "11":
                # TODO: Implement import
                pass
            elif choice == "12":
                grade_distribution_analysis(gradebook)
            elif choice == "13":
                print("Thank you for using the Gradebook System!")
                break
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    # Uncomment to run demo
    # demo_system()
    
    # Run main program
    main()
