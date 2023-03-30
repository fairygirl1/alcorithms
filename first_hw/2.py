#You are given an integer n, the number of teams in a tournament that has strange rules:
#If the current number of teams is even, each team gets paired with another team. A total of
# n / 2 matches are played, and n / 2 teams advance to the next round.
#If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired.
# A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.



#сложность O(n)
#сложность такая, потому что работет цикл while и каждую операцию выполняем по одному разу. Условие окончания программы
# - число равно 1, поэтому ставлю в условие строгое неравенство 1, потому что когда условие нарушится, цикл прервется.
# Делаю проверку числа на четность и нечетность, увеличиваю счетчик match и произвожу действие с данной переменной a,
# чтобы использовать ее при следующей итерации.

a = 7
def team(a):
    match = 0
    while a > 1:
        if a%2 == 0:
            match = match + a//2
            a = a//2
        else:
            match = match + (a-1)//2
            a = (a-1)//2+1
    return match



print(team(a))