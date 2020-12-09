def playlist(songs):
    # Write your code here
    c = [0] * 60
    res = 0
    for time in songs:
      complement = -time % 60
      leftover = time % 60
      res += c[complement]
      c[leftover] += 1
    return res


assert(playlist([30, 20, 150, 100, 40]) == 3)
