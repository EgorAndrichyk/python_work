countres = ['tai', 'usa', 'spanish', 'italian', 'japan']

print(countres)
print(sorted(countres))
print(countres)

print(sorted(countres, reverse=True))
print(countres)

countres.reverse()
print(countres)
countres.reverse()
print(countres)

countres.sort()
print(countres)

countres.sort(reverse=True)
print(countres)

print(len(countres))

games = ['diablo', 'call of duty', 'portal', 'dota', 'cs']

print(games[0].title())
print(games[1].upper())
print(games[2].lower())

games.insert(0, 'bioshok')
print(games)

games.append('spider-man')
print(games)

del games[0]
print(games)

one_games = games.pop(2)
print(games)
print(one_games)

print(sorted(games))
print(len(games))

games.sort()
print(games)

print(sorted(games, reverse=True))
print(games) 