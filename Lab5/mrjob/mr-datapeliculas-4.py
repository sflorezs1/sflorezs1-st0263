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
            yield movie, (usr, rating)

    def reducer(self, movie, values):
        l = list(values)
        yield movie, ("rating: ", sum([x[1] for x in l])/len(l), "users: ", len(l))

if __name__ == '__main__':
    MR.run()