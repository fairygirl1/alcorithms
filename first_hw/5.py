#A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.

#For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B,
# with A and B nonempty valid parentheses strings.

#Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are
# primitive valid parentheses strings.

#Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


#сложность O(n)
#задаем счетчик и пустой список, который будем пополнять в процессе
#для каждого элемента данной строки S если скобочка открывается и счетчик больше нуля пополняем список и увеличиваем
# счетчик на 1, если скобочка закрывается и счетчик больше 1 - тоже пополняем список. Возвращаем из функции пустую
# строку, которую заполняем значениями из списка.

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        stack = []
        for i in s:
            if i == '(' and count > 0:
                stack.append(i)
            if i == ')' and count > 1:
                stack.append(i)
            count += 1 if i == '(' else -1

        return "".join(stack)