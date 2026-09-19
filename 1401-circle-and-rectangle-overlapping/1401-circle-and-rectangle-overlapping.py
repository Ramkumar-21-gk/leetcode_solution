class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Closest x-coordinate on rectangle to circle center
        x = max(x1, min(xCenter, x2))

        # Closest y-coordinate on rectangle to circle center
        y = max(y1, min(yCenter, y2))

        # Distance squared
        distance = (x - xCenter) ** 2 + (y - yCenter) ** 2

        return distance <= radius ** 2