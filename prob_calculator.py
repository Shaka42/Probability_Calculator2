import random
import copy
class Hat:
    def __init__(self,*c):
        self.dict = {}
        self.contents = []
        for i in c:
            a = i.split('=')
            self.dict[a[0]] = int(a[1])
        print(self.dict)
        for i,v in self.dict.items():
            n = 0
            while n < v:
                self.contents.append(i)
                n += 1
        print(self.contents)

    def draw(self,m):
        hat = []
        s = {}
        if len(self.contents) < m:
            for i in self.contents:
                 hat.append(i)
            return hat
        else:
            for i in range(m):
                a = random.choice(self.contents)
                hat.append(a)
            for i in hat:
                s[i]=s.get(i,0)+1
            return s





def experiments(hat,expected_ball,num_balls_draw,num_experiments):
    hat = copy.copy(hat)
    n = 0
    m = 0
    print(expected_ball)
    while n < num_experiments:
        hat1 = hat.draw(num_balls_draw)
        print(hat1)
        s = 0
        for i, v in hat1.items():
            if i not in expected_ball:
                s += 1
                continue
            elif hat1[i] < expected_ball[i] or hat1[i] > expected_ball[i]:
                s += 1
                continue
            elif hat1[i] == expected_ball[i]:
                s += 1
                if n == len(hat1.items()):
                    m += 1
                else:
                    continue
        n += 1
    return f'probability = {m}/{n}'