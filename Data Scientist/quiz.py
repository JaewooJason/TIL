question = ['Q2', 'Q3', 'Q4', 'Q5', 'Q6_1', 'Q6_2', 'Q6_3', 'Q6_4', 'Q6_5', 'Q6_6',
       'Q6_7', 'Q6_8', 'Q6_9', 'Q6_10', 'Q6_11', 'Q6_12', 'Q7_1', 'Q7_2',
       'Q7_3', 'Q7_4', 'Q7_5', 'Q7_6', 'Q7_7', 'Q8', 'Q9', 'Q10_1', 'Q10_2',
       'Q10_3']
questions = []

for i in question:
    if len(i) == 2:
           questions.append(i)
print(questions)

quetion1 = [i for i in question if '_' not in i]
print(quetion1)

# 리스트 컴프레션을 잘 사용하는 법 공부하기


