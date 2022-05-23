from mrjob.job import MRJob

class MR(MRJob):

    def mapper(self, _, line):
        cmp, price, date = line.split(',')
        try: 
            # check if header
            price = float(price)
        except ValueError:
            pass
        else:
            yield cmp, price

    def reducer(self, cmp, values):
        l = list(values)
        
        stable = True
        last_val = l[0]
        for val in l[1:]:
            if val < last_val:
                stable = False
            last_val = val
        if stable:
            yield cmp, 'stable'

if __name__ == '__main__':
    MR.run()