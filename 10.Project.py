class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        # Filter out empty strings and convert to float
        valid_scores = [float(s) for s in self.Grades if s.strip()]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):

        total_scores = [float(s) if s.strip() else 0.0 for s in self.Grades]
        if not total_scores:
            return 0.0
        return sum(total_scores) / len(total_scores)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

def main():
   
    header = f"{'First':<12} {'Last':<12} {'ID':<12} {'Running':<12} {'Semester':<12} {'Letter':<12}"
    sub_header = f"{'Name':<12} {'Name':<12} {'Number':<12} {'Average':<12} {'Average':<12} {'Grade':<12}"
    print(header)
    print(sub_header)
    print("-" * 72)

    try:
        with open("10.Project Student Scores.txt", "r") as file:
            for line in file:
                if not line.strip():
                    continue
                
                # Split line by comma
                parts = line.strip().split(',')
                

                fname = parts[0]
                lname = parts[1]
                tnum = parts[2]
                scores = parts[3:]
                
                # Create Student object
                student = Student(fname, lname, tnum, scores)
                
                # Display output in formatted manner
                print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} "
                      f"{student.RunningAverage():<12.2f} {student.TotalAverage():<12.2f} "
                      f"{student.LetterGrade():<12}")
    except FileNotFoundError:
        print("Error: '10.Project Student Scores.txt' not found.")

if __name__ == "__main__":
    main()