def maxset(self, A):
        mxsum = -1
        l = []
        nl = []
        for i in range(len(A)):
            if A[i] < 0:
                if sum(nl) > mxsum:
                    mxsum = sum(nl)
                    l = []
                    for num in nl:
                        l.append(num)
                   
                elif sum(nl) == mxsum and len(l) < len(nl):
                    l = []
                    for num in nl:
                        l.append(num)
                
                nl = []
            else:
                nl.append(A[i])
        if sum(nl) > mxsum:
            mxsum = sum(nl)
            l = []
            for num in nl:
                l.append(num)
                nl = []
        elif sum(nl) == mxsum and len(l) < len(nl):
            l = []
            for num in nl:
                l.append(num)
                nl = []
        return l
