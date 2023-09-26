#WORKOUT PLANNER

import random

cp_exercises = ["squat","deadlift","bench press","barbell row"]
bw_exercises = ["push ups", "pull ups", "dips", "crunches"]
db_exercises = ["bicep curls", "skull crushers", "lateral raises","hammer curls"]
cardio = ["treadmill","bike","skip","walk"]




days = int(input("Enter amount of sessions per week: "))
for i in range(days):

    print("\n")
    print("Session {}".format(4))
    print(" ".join(random.sample(cp_exercises, k=2)))
    print(" ".join(random.sample(db_exercises, k=3)))
    print(" ".join(random.sample(bw_exercises, k=2)))
    print(" ".join(random.sample(cardio, k=1)))
    
    