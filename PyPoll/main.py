#main.pay in PyPoll
candidates = {'name': [] ,'votes': []}
answer= "y"
votes = 0
while answer =="y":
   candidate = input("Enter the Candidate Name:  ")
   list1 = candidates['name']
   if candidate in list1:
       list2 = candidates['votes']
       candidate_num = list1.index(candidate)
       list2[candidate_num] = list2[candidate_num]+ 1
       print(f"votes {votes}")
       candidates.update({'votes': list2})
       print(f" dic. {candidates}")
   else:
       votes = 1
       candidates['name'].append(candidate)
       candidates['votes'].append(votes)
       print(f" dic. {candidates}")
   answer = input("Do you want to add another Candidate? y(es) or n(o)? ")
print(f" candidates { candidates}")