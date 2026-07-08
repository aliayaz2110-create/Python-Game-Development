def panagram(s):
    letters = {}
 
    for c in 'abcdefghijklmnopqrstuvwxyz':
        letters[c] = 0
    
    for c in s.lower():
        if c in letters:
            letters[c] += 1
            
    for value in letters.values():
        if value == 0:
            return False
    return True

line = input("Enter String: ")

if panagram(line) == True:
    print("It's A Panagram")
else:
    print("It's Not A Panagram")