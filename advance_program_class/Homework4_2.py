class SalaryDistribution():
    def __init__(self,lst):
        self.lst=lst
    def min(self):
      return min(self.lst)
    def max(self):
      return max(self.lst)
    def median(self):
      tmp = sorted(self.lst)
      mid = round(len(tmp)/2)
      return tmp[mid]
    def mean(self):
      return sum(self.lst)/len(self.lst)