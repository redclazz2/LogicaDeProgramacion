import pandas as pd
titanic = pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv', index_col = 0)
print(titanic.head(100))