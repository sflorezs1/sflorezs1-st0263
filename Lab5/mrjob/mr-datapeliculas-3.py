from mrjob.job import MRJob, MRStep

class MR(MRJob):

    def mapper(self, _, line):
        usr, movie, rating, genre, date = line.split(',')
        try: 
            # check if header
            rating = float(rating)
        except ValueError:
            pass
        else:
            yield date, 1

    def reducer(self, date, values):
        yield None, (sum(values), date)

    def reducer2(self, _, values):
        yield 'Least views on: ', min(values)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MR.run()