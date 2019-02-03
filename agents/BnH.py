import numpy as np

class BnH:
    def __init__(self):
        self.a_dim=0
        self.is_start=True

    def predict(self,s,a):
        if self.is_start==True:
            w = np.ones(len(a[0])) / (len(a[0])-1)
            w[0] = 0
            w = w[None,:]
            self.is_start=False
            return w
        else:
            return a
