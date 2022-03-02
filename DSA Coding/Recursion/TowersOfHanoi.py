def Met(self, discs, start, helper, destination):
            if discs == 1:
                print(f"{start} to {destination}")
                return()
            else:                
                self. Met(discs-1, start, destination, helper)
                print(f"{start} to {destination}")
                self. Met(discs-1, helper, start, destination)
