import art
import random
import game_data

a = random.choice(game_data.data)
b = random.choice(game_data.data)

score = 0
while score >= 0:
    followers_a = a["follower_count"]
    followers_b = b["follower_count"]

    print(art.logo)
    print(f"Current score {score}")
    print(f'Compare A:', a["name"],'a',a["description"],'from',a["country"])
    print(art.vs)
    print(f'Against B:', b["name"],'a',b["description"],'from', b["country"])

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)

    if followers_a > followers_b and answer == "a":
        score +=1
        a = b
        b = random.choice(game_data.data)
    elif followers_b > followers_a and answer == 'b':
        score += 1
        a = b
        b = random.choice(game_data.data)
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()





#compare(followers_a,followers_b)

#for i in game_data.data:
#    print(i["follower_count"])


# print(f'Compare A:',a["name"],a["description"],a["country"],a["follower_count"])
# print(f'Against B:',b["name"],b["description"],b["country"],b["follower_count"])

# followers_a = a["follower_count"]
# followers_b = b["follower_count"]

# answer = input("Who has more followers? Type 'A' or 'B': ").lower()

# def compare(fa, fb):
#     if fa > fb:
#         #print(a)
#         print(a["name"],a["description"],a["country"],a["follower_count"])
#     else:
#         #print(b)
#         print(b["name"],b["description"],b["country"],b["follower_count"])
