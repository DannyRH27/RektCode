def rankTeams(votes):
  if len(votes) == 1:
    return votes[0]

  vote_count = {}
  
  for vote in votes:
    for i, letter in enumerate(vote):
      if letter not in vote_count:
        vote_count[letter] = [0] * len(vote)
      vote_count[letter][i] += 1

  rank = list(vote_count.items())
  # for rank in rank:
  #   print(rank[1],[-ord(rank[0])])

  rank.sort(reverse=True, key = lambda x: x[1] + [-ord(x[0])])

  ans = [x[0] for x in rank]
  return "".join(ans)

assert(rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"])== "ACB")
