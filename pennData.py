import pandas as pd
import random

fNames = ["Adam","Nick","John","Steve","Ethan","Greyson","Eli","Jacob","Aiden","Landon","Kamryn","Ryleigh","Emily","Sarah","Jenna","Abby","Ava","Jocelyn"]
lNames = ["Smith","Jones","Williams","Johnson","Brown","Miller","Davis","Martinez","Thomas","Moore","Anderson","Garcia","Martin","Taylor","Lopez"]
years = ["Freshman","Sophomore","Junior","Senior","Victory Lap"]
pathways = ["Early College","Engineering","Computer Science","Business","Marketing","Early Childhood Education","Culinary","Criminal Justice","Biomed"]
names = []

for i in range(20):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}) 


data = {
    "Name":names,
    "Age":[random.randint(14,19) for _ in names],
    "GPA": [round(random.uniform(0.3,4.5),2) for _ in names],
    "Credits Completted": [random.randint(0,60) for _ in names]
    "Year":[random.choice(years) for _ in names]
    "Pathway":[random.choice(pathways) for _ in names]
}
pennData = pd.DataFrame(data)
print(pennData)