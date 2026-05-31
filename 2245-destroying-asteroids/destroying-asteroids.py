class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids = sorted(asteroids)

        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True