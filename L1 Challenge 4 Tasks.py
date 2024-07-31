#Task 1 solution to 'Office 1:Outed' on codewars.
def outed(meet, boss):
  for k, v in meet.items():
    if boss == k:
      meet[k] = v*2
  sum_happiness = 0
  for v in meet.values():
    sum_happiness += v
  overall_happiness = sum_happiness/(len(meet))
  if overall_happiness <= 5:
    print("Get Out Now!")
  else:
    print("Nice Work Champ!")


coworkers = {'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}
#Check if the function works as intended
outed(coworkers, 'laura')

#Level 4 task solution for 'The Office 2: Boredo
def boredom(staff):
  cumulative_score = 0
  department_map = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}
  for v in staff.values():
    for k in department_map.keys():
      if v == k:
        cumulative_score += department_map[k]
  
  if cumulative_score <= 80:
    return "kill me now"
  elif cumulative_score > 80 and cumulative_score < 100:
    return "i can handle this"
  else:
    return "party time!!"


#Test using arguments from codewars.
coworkers = {"tim": "change", "jim": "accounts",
  "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
  "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
  "mr": "finance" }
print(boredom(coworkers))