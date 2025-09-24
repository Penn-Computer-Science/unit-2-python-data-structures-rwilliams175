import pandas as pd
b_names = ['Noah', 'Liam', 'Jacob', 'Williams', 'Mason', 'Ethan', 'Michael', 'Alexander', 'James', 'Elijah']
b_freq = [183330, 173981, 163266, 159945, 157875, 149082, 145171, 142142, 139652, 137093]
g_names = ['Emma', 'Olivia', 'Sophia', 'Isabella', 'Ava', 'Mia', 'Abigail', 'Emily', 'Charlotte', 'Madison']
g_freq = [195028, 184528, 181132, 170559, 155844, 129088, 118713, 117626, 102470, 98419]
df = pd.DataFrame{
    (
        "BoysNames":b_names, 
        "BFrequency":b_freq, 
        "GirlsNames":g_names,
        "GFrequency":g_freq
    )
}
print(df)
print (round[df.describe()])
