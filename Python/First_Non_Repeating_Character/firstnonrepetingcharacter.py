key=0
s=0

# a list of characters for reference
chars = "abcdefghijklmnopqrstuvwxyz"
# let the user type any word and load that word into the charset variable
charset=input("Type a sequence of letters:")

# the counter that keeps count of each letter in the typed word
count = {}

#if the letter int the counter repeats increment the counter, otherwise do not
for s in charset:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

# if the ammount of repeats is equal to 1 print it with the amount of repeats
for key in count:
  if count[key] == 1:
    print(key, count[key])