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
            yield cmp, (price, date)

    def reducer(self, cmp, values):
        l = list(values)
        d_min = min(l)
        d_max = max(l)
        yield cmp, ("Min:", d_min, "Max:", d_max)

if __name__ == '__main__':
    MR.run()
