# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError
#
#
# height = float(input("Height: "))
# weight = int(input("Height: "))
#
# if height > 3:
#     raise ValueError("Human should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post["Likes"] = 0
else:
    print(total_likes)
