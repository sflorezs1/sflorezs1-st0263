from mrjob.job import MRJob

class MR(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        try: 
            # check if header
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield idemp, sector

    def reducer(self, idemp, values):
        l = list(values)
        yield idemp, len(l)

if __name__ == '__main__':
    MR.run()