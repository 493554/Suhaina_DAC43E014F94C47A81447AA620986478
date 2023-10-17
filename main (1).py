class player:

  def play(self):
    print("The player is playing cricket.")


class batsman(player):

  def play(self):
    print("The batsman is batting.")


class bowler(player):

  def play(self):
    print("The bowler is bowling.")


Batsman = batsman()
Bowler = bowler()
Batsman.play()
Bowler.play()
