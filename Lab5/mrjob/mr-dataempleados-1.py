from mrjob.job import MRJob

class MR(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        try: 
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield sector, salary

    def reducer(self, sector, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield sector, avg

if __name__ == '__main__':
    MR.run()