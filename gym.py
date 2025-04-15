# Gym tracker
# user input their names,and gender, ay least 3 days; specific, how many hours you train, cardio or weightlifting 
# what body part you train, how many reps in total, how heavy did you lift,
# how many kilometres did you run, 
# output: the current rank, leaderboard

# calculation formula for the ranking: 
# Everybody starts at (0 points), first 10 km runner will get 500 points per 1 km, 
# after 10 km, will get 1000 points per km
# for weightlifting in total weight: 1st 100 kg get 5 points per 1 kg, after will get 8 points per 1 kg.
# after calculation if female, will be multiplied by 1.5x.

# Ranking system:
# bronze rank is from 0-10,000 points,
# silver is from 10,001 to 25,000
# diamond is > 25,000



userNames = ["Chupa","Chu","Pachu","Achup"]
userGenders = ["Male","Female","Male","Male"]


userTypes = [True, False, True, False] # True = running, False = weightlifting
userDistance = [0,0.1,0,4.5]# kilometers
userReps = [124,0,90,0] #reps
userWeight = [30,0,70,0] #kilograms




def gym_calculate (gender, distance, reps, weight):
    point = 0
    if distance <= 10:
        point = point + (distance * 500)
    else:
        point = point + (10 * 500) + ((distance - 10) * 1000)

    totalWeight = reps * weight
    
    if totalWeight <=100: 
        point = point + (totalWeight * 5)
    else:
        point = point + (100 * 5) + ((totalWeight - 100)* 8)
    
    if gender == "Female":
        point = point * 1.5
    return point



