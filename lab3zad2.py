#2. Napisz program, który wyświetli plan wycieczki – wybierając losowo z listy 10 największych miast w Polsce miasta do odwiedzenia. Miast ma być 10, nie mogą się powtarzać. (20%)
import random

city_list = ["Warszawa", "Krakow", "Wroclaw", "Lodz", "Poznan", "Gdansk", "Szczecin", "Lublin", "Bialystok", "Katowice"]
list_to_visit = []

for i in range(len(city_list)):
    r = random.randrange(len(city_list))
    list_to_visit.append(city_list[r])
    city_list.remove(city_list[r])

for i in range(len(list_to_visit)):
    print(f"{i+1} place to visit is: {list_to_visit[i]}")