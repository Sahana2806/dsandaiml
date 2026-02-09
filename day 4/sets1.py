friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
print("Shared Interests:", shared_interests)
all_interests = friend_a | friend_b
print("All Interests:", all_interests)
unique_to_a = friend_a - friend_b
print("Friend A Only Interests:", unique_to_a)
Shared Interests: {'Python', 'Hiking'}
All Interests: {'Python', 'Cooking', 'Hiking', 'Movies', 'Gaming', 'Photography'}
Friend A Only Interests: {'Cooking', 'Movies'}
