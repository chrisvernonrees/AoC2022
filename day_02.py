# Part 1

a_dict = dict(X = 'D', Y = 'W', Z = 'L')
b_dict = dict(X = 'L', Y = 'D', Z = 'W')
c_dict = dict(X = 'W', Y = 'L', Z = 'D')

result_dict = dict(A = a_dict, B = b_dict, C = c_dict)

result_score = dict(W = 6, D = 3, L = 0)
throw_score = dict(X = 1, Y = 2, Z = 3)

score = 0

with open("day2input.txt","r") as f:
    for line in f:
        
        line_list = list(line.rstrip())
        
        opp = line_list[0]
        me = line_list[2]
        
        outcome = result_dict[opp][me]
        
        score += result_score[outcome]
        score += throw_score[me]
        
print(score)


#  Part 2


a_dict2 = dict(X = 'S', Y = 'R', Z = 'P')
b_dict2 = dict(X = 'R', Y = 'P', Z = 'S')
c_dict2 = dict(X = 'P', Y = 'S', Z = 'R')

result_dict2 = dict(A = a_dict2, B = b_dict2, C = c_dict2)

result_score2 = dict(Z = 6, Y = 3, X = 0)
throw_score2 = dict(R = 1, P = 2, S = 3)

score = 0

with open("day2input.txt","r") as f:
    for line in f:
        
        line_list = list(line.rstrip())
        
        opp = line_list[0]
        me = line_list[2]
        
        my_throw = result_dict2[opp][me]
        
        score += result_score2[me]
        score += throw_score2[my_throw]


        
print(score)

