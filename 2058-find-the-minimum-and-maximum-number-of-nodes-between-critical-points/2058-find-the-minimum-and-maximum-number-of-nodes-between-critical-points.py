class Solution:
    def nodesBetweenCriticalPoints(self, head):
        
        # Less than 3 nodes means no critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        
        index = 1
        
        firstCritical = -1
        prevCritical = -1
        
        minDistance = float('inf')
        maxDistance = -1
        
        while curr.next:
            
            # Check local maxima
            isMax = prev.val < curr.val and curr.val > curr.next.val
            
            # Check local minima
            isMin = prev.val > curr.val and curr.val < curr.next.val
            
            if isMax or isMin:
                
                # First critical point
                if firstCritical == -1:
                    firstCritical = index
                
                # Calculate distance from previous critical point
                if prevCritical != -1:
                    minDistance = min(
                        minDistance,
                        index - prevCritical
                    )
                
                # Maximum distance = current - first
                maxDistance = index - firstCritical
                
                # Update previous critical point
                prevCritical = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        # Less than 2 critical points
        if minDistance == float('inf'):
            return [-1, -1]
        
        return [minDistance, maxDistance]