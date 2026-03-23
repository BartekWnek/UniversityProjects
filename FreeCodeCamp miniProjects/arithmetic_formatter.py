def arithmetic_arranger(problems, show_answers=False):
    lines = [[], [], [], [], []] #First num, operator, second num, problem length, ans
    for problem in problems:
        problem = problem.split()
        
        lines[0].append(problem[0])
        lines[1].append(problem[1])
        lines[2].append(problem[2])

        for i in lines[0]:
            if i.isdigit() == False:
                return ('Error: Numbers must only contain digits.')
        for (i) in (lines[2]):
            if i.isdigit() == False:
                return ('Error: Numbers must only contain digits.')


        problem_length = max(len(problem[0]), len(problem[2])) + 2
        if problem_length > 6:
            return ("Error: Numbers cannot be more than four digits.")
        lines[3].append(max(len(problem[0]), len(problem[2])) + 2)
        
        if problem[1] == '+':
            lines[4].append(str(int(problem[0]) + int(problem[2])))
        elif problem[1] == '-':
            lines[4].append(str(int(problem[0]) - int(problem[2])))
        else:
            return ("Error: Operator must be '+' or '-'.")
    if len(problems) > 5:
            return ("Error: Too many problems.")

    white_spaces = [[], [], [], [], [], []]
          
    #====================First line=======================#
    for idx in range(len(lines[0])):
        if idx != 0:
            space_between_operations = [" " for i in range(4)]
            white_spaces[0].append(space_between_operations)
        space_len = lines[3][idx]-len(lines[0][idx])
        space = [" " for i in range(space_len)]
        white_spaces[0].append(space)
    for space in white_spaces[0]:
        space = "".join(space)
        white_spaces[1].append(space)
    insert_index = 0
    for idx in range(len(white_spaces[1])):
        if insert_index%3 == 1:
            insert_index += 1
            lines[0].insert(insert_index, white_spaces[1][idx])
        else:
            lines[0].insert(insert_index,white_spaces[1][idx])
        insert_index +=1
    #=================== Second Line =============================#
    for idx in range(len(lines[2])):
        if idx != 0:
            space_between_operations = [" " for i in range(4)]
            white_spaces[2].append(space_between_operations)
        space_len = lines[3][idx]-len(lines[2][idx])-1
        space = [" " for i in range(space_len)]
        white_spaces[2].append(space)
    for space in white_spaces[2]:
        space = "".join(space)
        white_spaces[3].append(space)
    insert_index = 0
    for idx in range(len(white_spaces[3])):
        if insert_index%3 == 1:
            insert_index += 1
            lines[2].insert(insert_index, white_spaces[3][idx])
        else:
            lines[2].insert(insert_index,white_spaces[3][idx])
        insert_index +=1
    op_idx = 0
    for idx in range(len(lines[2]) + len(lines[1])):
        if idx%4 == 0:
            lines[2].insert(idx, lines[1][op_idx])
            op_idx += 1

    line1 = ''.join(lines[0]) + '\n'
    line2 = ''.join(lines[2]) + '\n'
    # =================== Seaparators ===========================
    separator = []
    for idx in range(len(problems)):
        if idx != 0:
            space_between_operations = ''.join([" " for i in range(4)])
            separator.append(space_between_operations)
        separator.append(''.join(['-' for i in range(lines[3][idx])]))

    for s in separator:
        s = ''.join(s)
    
    #Answers
    for idx in range(len(lines[4])):
        if idx != 0:
            space_between_operations = [" " for i in range(4)]
            white_spaces[4].append(space_between_operations)
        space_len = lines[3][idx]-len(lines[4][idx])
        space = [" " for i in range(space_len)]
        white_spaces[4].append(space)
    for space in white_spaces[4]:
        space = "".join(space)
        white_spaces[5].append(space)
    insert_index = 0
    for idx in range(len(white_spaces[5])):
        if insert_index%3 == 1:
            insert_index += 1
            lines[4].insert(insert_index, white_spaces[5][idx])
        else:
            lines[4].insert(insert_index,white_spaces[5][idx])
        insert_index +=1
    result = "\n" + ''.join(lines[4])

    separators_together = ''.join(separator)

    if show_answers == True:
        problem = line1 + line2 + separators_together + result
    else:
        problem = line1 + line2 + separators_together 
    
    return problem
    

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
