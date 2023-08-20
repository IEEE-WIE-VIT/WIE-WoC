def max_steps(self, A):
        
        steps = [0] * (A+1)
        
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        
        p = 10**9+7
        
        for i in range(3,A+1):
            steps[i] = steps[i-1]%p ++ steps[i-2]%p
            
        return steps[A]%p
