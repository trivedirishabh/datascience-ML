import pandas as pd

data = pd.read_csv("2018.csv")

gray = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])
print(gray,black,red)

data_dict = {"fur Color" : ['Gray', 'Cinnamon', 'Black'],
              "Count" : [gray, red, black]
              }

df = pd.DataFrame(data_dict)
df.to_csv('test.csv')