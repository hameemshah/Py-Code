import art
import game_data

def play(score):
    for i in range(0,len(game_data.data)):
      print(art.logo)
      
      name = game_data.data[i]['name']
      country = game_data.data[i]['country']
      description = game_data.data[i]['description']
      print(f"Compare A: {name},a {description} from {country}")
      print(art.vs)
      
      name = game_data.data[i+1]['name']
      country = game_data.data[i+1]['country']
      description = game_data.data[i+1]['description']
      print(f"Against B: {name},a {description} from {country}")
      answer = input().upper()
      
      if answer == 'A' and game_data.data[i]['follower_count']>game_data.data[i+1]['follower_count']:
        score+=1
        print(f"You are right, Current Score = {score}")
      elif answer == 'A' and game_data.data[i]['follower_count']<game_data.data[i+1]['follower_count']:
        print("You Lose")
        print(f"Your Score is {score}")
        exit()
      elif answer == 'B' and game_data.data[i]['follower_count']<game_data.data[i+1]['follower_count']:
        score+=1
        print(f"You are right, Current Score = {score}")
      elif answer == 'B' and game_data.data[i]['follower_count']>game_data.data[i+1]['follower_count']:
        print("You Lose")
        print(f"Your Score is {score}")
        exit()
      else:
        print("Please input A or B only!")

score = 0
play(score)

