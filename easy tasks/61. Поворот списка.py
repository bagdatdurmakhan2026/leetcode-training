class Solutin(object):
    def rotateRight(self, head, k):
        n = len(head)
        k %=n
        arr = [0]*n
        for i in range(n):
            arr[(i+k)%n] = head[i]
        return arr