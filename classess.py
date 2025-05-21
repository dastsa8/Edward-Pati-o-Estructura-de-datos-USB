class dog:
  def __init__(self,size,color,race,price,name):
    self.size = size
    self.color = color
    self.race = race
    self.price = price
    self.name = name
Rufo = dog("big", "black", "huskey", 3000, "Rufo")
Cosi = dog("medium", "white", "french bulldog", 3000, "Cosi")
Elos = dog("small", "white, brown and black", "yorkshire terrier", 1500, "Elos")
Bita = dog("small", "brown", "chihuahua", 300, "Bita")
Kuni = dog("big", "orange", "chow chow", 2000, "Kuni")
class movie:
  def __init__(self,name,rating,benefit,mainactor,gender):
    self.name = name
    self.rating = rating
    self.benefit = benefit
    self.mainactor = mainactor
    self.gender = gender
Interestellar = movie("Interestellar", 4, 900000000, "Matthew McConaughey", "fiction science")
The_Lord_of_the_Rings_The_Fellowship_of_the_Ring = movie("The Lord of the Rings: The Fellowship of the Ring", 9.0, 897693338, "Elijah Wood", "Fantasy, Adventure")
Parasite = movie("Parasite", 8.6, 263206514, "Song Kang-ho", "Drama, Thriller, Black Comedy")
La_La_Land = movie("La La Land", 8.0, 446092134, "Ryan Gosling", "Musical, Drama, Romance")
Scarface = movie("Scarface", 8.3, 65830625, "Al Pacino", "Crime, Drama")
class footballteams:
  def __init__(self,name,leaguetitles,legend,championstitles,rating):
      self.name = name
      self.leaguetitles = leaguetitles
      self.legend = legend
      self.championstitles = championstitles
      self.rating = rating
FC_Barcelona = footballteams("FC Barcelona", 27, "Lionel Messi", 5, 5)
Real_Madrid = footballteams("Real Madrid", 36, "Alfredo Di Stéfano", 14, 5)
AC_Milan = footballteams("AC Milan", 19, "Paolo Maldini", 7, 4)
Bayern_Munich = footballteams("Bayern Munich", 33, "Franz Beckenbauer", 6, 5)
Ajax = footballteams("Ajax", 36, "Johan Cruyff", 4, 3)



print()