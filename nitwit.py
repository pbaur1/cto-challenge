import tweepy
import sys

consumerKey = input("Enter Consumer Key (API Key): ")
consumerSecret = input("Enter Consumer Secret (API Secret): ")
accessToken = input("Enter Access Token: ")
secretAccessToken = input("Enter Access Token Secret: ")

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, secretAccessToken)
api = tweepy.API(auth)

# Find if user exists
userFound = True
while userFound:
    try:
        user = api.get_user(input("Twitter username to lookup: "))
        print("User found")
        userFound = False
        break
    except:
       print("User not found")       
       continue
    
# Get the lists for that user
lists = api.lists_all(user.screen_name)
length = len(lists)
if length == 0:
    print ("This user has no lists")
    sys.exit()

index = -1

for i, listName in enumerate(lists):
    print ("{}. {} ({} members)".format(i + 1, listName.name, listName.member_count))
index = int (input("Choose a group number from the list to follow all members: "))

# Validate Group Number
if (index < 1 or index > length):
    print("Invalid Group Number")
    sys.exit()

print("Group {} has been selected".format(index))
index = index - 1

print("{}'s {} list has been selected. Following all {} members.".format(user.screen_name, lists[index].name, lists[index].member_count))

# Retrieve all members of chosen list
groupList = api.list_members(list_id = lists[index].id, slug = user.screen_name)

# List all members in group and follow
for member in groupList:
    api.create_friendship(member.screen_name)
    print(member.screen_name)



