from functools import reduce
from mrjob.job import MRJob, MRStep

class MR(MRJob):

    def mapper1(self, _, line):
        cmp, price, date = line.split(',')
        try:
            price = float(price)
        except ValueError:
            pass
        else:
            yield cmp, (price, date)

    def reducer1(self, cmp, values):
        yield cmp, min(list(values))
    
    def mapper2(self, cmp, value):
        yield value[1], 1
    
    def reducer2(self, date, values):
        yield None, (sum(values), date)
    
    def reducer3(self, _, values):
        yield 'Black day', max(values)

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
            MRStep(reducer=self.reducer3)
        ]

if __name__ == '__main__':
    MR.run()