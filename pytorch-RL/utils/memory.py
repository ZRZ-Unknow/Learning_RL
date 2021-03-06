import random
from collections import namedtuple
'''class ReplayBuffer():
    def __init__(self,capacity):
        self.capacity=int(capacity)
        self.buffer=[]
        self.point=0
        self.transition=namedtuple("transition",field_names=['state','action','reward','next_state','done'])
    
    def add(self,s,a,r,s_,done):
        t=self.transition(s,a,r,s_,done)
        if self.point<self.capacity:
            self.buffer.append(t)
        else:
            self.buffer[self.point%self.capacity]=t
        self.point+=1
    
    def sample(self,batch_size):
        return random.sample(self.buffer,batch_size)
    
    def is_full(self):
        return len(self.buffer)==self.capacity'''

class ReplayBuffer():
    def __init__(self,capacity):
        self.capacity=int(capacity)
        self.buffer=[]
        self.point=0
    
    def add(self,transition):
        if self.point<self.capacity:
            self.buffer.append(transition)
        else:
            self.buffer[self.point%self.capacity]=transition
        self.point+=1
    
    def sample(self,batch_size):
        return random.sample(self.buffer,batch_size)
    
    def __len__(self):
        return len(self.buffer)

    def is_full(self):
        return len(self.buffer)==self.capacity

