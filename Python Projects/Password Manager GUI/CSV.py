import pandas

data = pandas.read_csv("../../Downloads/password.csv")
data_dict = {row.website: {"username": row.username, "password": row.passwords} for (index, row) in data.iterrows()}

# data = pandas.DataFrame(data_dict)
# data.to_csv("passwords")


print(data_dict)
