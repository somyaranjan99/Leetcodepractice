class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      countSandwich=0
      while sandwiches and students:
        if sandwiches[0]==students[0]:
          sandwiches.pop(0)
          students.pop(0)
          countSandwich=0
        else:
          top=students.pop(0)
          students.append(top)
          countSandwich +=1
          if countSandwich==len(students):
            break
      return len(students)


        