while True:
    try:
        N = int(input())
        
        students = []
        for i in range(N): 
            line = input().split()
            student_id = line[0]  
            name = line[1]          
            
            college = student_id[-1] 
            level = student_id[0]    
            
            students.append([college, level, i, name])

        students.sort()

        for s in students:
            print(s[0] + ": " + s[3])
            
    except EOFError:
        break
