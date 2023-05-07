class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0 # количество периодов спада цен
        for i, x in enumerate(prices): 
        # первый элемент в списке цен, не нужно проверять, есть ли период падения цен до него
            if i == 0 or prices[i-1] != x + 1: cnt = 0
            # or - сравниваю цену на предыд индексе с текущей, при равенстве увеличиваю cnt = продолжаю старый период, иначе - начинаю новый период падения цен
            cnt += 1
            ans += cnt 
        return ans 
