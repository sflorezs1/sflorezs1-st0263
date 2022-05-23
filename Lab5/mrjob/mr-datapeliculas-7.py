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
            yield (movie, genre), rating

    def reducer(self, movgen, values):
        l = list(values)
        yield movgen, sum(l)/len(l)

    def mapper2(self, movgen, value):
        yield movgen[1], (value, movgen[0])

    def reducer2(self, genre, values):
        l = list(values)
        yield genre, ("Worst:", min(l), "Best:", max(l))

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(mapper=self.mapper2, reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MR.run()