if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        res = 0
        if i == query_name:
            res = sum(student_marks[i])/3
            print(f'{res:.2f}')
    
