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
            yield date, rating

    def reducer(self, date, values):
        l = list(values)
        yield None, (sum(l)/len(l), date)

    def reducer2(self, _, values):
        yield "Best rated day:", max(values)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MR.run()