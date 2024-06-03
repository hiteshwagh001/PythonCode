player=["rohit","rahul","virat","shreyash","shubman"]
print(player[0])

print(player[2::])
print(player[2:4:2])
print(player[2:4:1])
print(player[:3:1])
print(player[:3:2])
print(player[4:2:-1])
print(player[-4:-2:])
print(player[-1::-1])


player.append("sky")
print(player)

player.extend(["jaddu","bumrah","shami"])
print(player)

player.insert(2,"Hardik")
print(player)

player.remove("shami")
print(player)

player.pop()
print(player)

player.pop(2)
print(player)

# player.clear()
print(player)


print(player.count("jaddu"))

player.reverse()
print(player)

player.sort()
print(player)


