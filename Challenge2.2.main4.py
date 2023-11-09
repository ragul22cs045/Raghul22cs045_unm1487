#define the base class player
class player:
  def play(self):
    print("The Player Is Playing Cricket.")
   #define the derived class bastman
class Batsman(player):
  def play(self):
    print("The Batsman Is Bating.")
       #define the derived class of bolwet
class Bowler(player):
  def play(self):
    print("The Bowler Is Bowling")
         #create objects of batsman & Bowlerclass
batsman = Batsman()
bowler = Bowler()
#calling the paly()method for each object
batsman.play()
bowler.play()
