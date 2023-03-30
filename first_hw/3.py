#You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#Letters are case sensitive, so "a" is considered a different type of stone from "A".

#сложность O(n)
#проверяем каждый элемент в украшениях и потом каждый элемент в камнях, если есть совадение увеличиваем счетчик count. Сложность будет O(3n), потому что каждый символ нужно проверить в одной строке, потом во второй
#(украшени и камни соответственно) и потом проверить условие if


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for element in jewels:
            for item in stones:
                if element == item:
                    count += 1
        return count