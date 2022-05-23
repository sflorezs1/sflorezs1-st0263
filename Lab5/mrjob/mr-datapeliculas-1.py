from mrjob.job import MRJob

class MR(MRJob):

    def mapper(self, _, line):
        usr, movie, rating, genre, date = line.split(',')
        try: 
            # check if header
            rating = float(rating)
        except ValueError:
            pass
        else:
            yield usr, rating

    def reducer(self, usr, values):
        l = list(values)
        yield usr, ('Avg rating:', sum(l)/len(l), 'Quantity:', len(l))


if __name__ == '__main__':
    MR.run()