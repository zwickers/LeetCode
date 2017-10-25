class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stringlist = []
        for i in range(1,n+1):
            if i % 15 == 0:
                stringlist.append("FizzBuzz")
            elif i % 3 == 0:
                stringlist.append("Fizz")
            elif i % 5 == 0:
                stringlist.append("Buzz")
            else:
                stringlist.append(str(i))
        return stringlist
