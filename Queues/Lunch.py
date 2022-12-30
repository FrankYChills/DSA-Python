# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the
# ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the
# jth student in the initial queue (j = 0 is the front of the queue).
# Return the number of students that are unable to eat.

def countStudents(students, sandwiches):
    # same students checks if every student want the same sandwich that is not at top of stack
    def sameStudents(nums):
        prev = nums[0]
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            return False
        return True

    while students:
        # all the students will be unable to eat at this case
        if students[0] != sandwiches[0] and sameStudents(students):
            return len(students)
        # here place first student at last of queue
        elif students[0] != sandwiches[0]:
            first = students[0]
            students.pop(0)
            students.append(first)
        # here first students gets his sandwich and takes it out of stack
        else:
            students.pop(0)
            sandwiches.pop(0)

    # here all student will be able to take sandwiches so return 0
    return 0


print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
