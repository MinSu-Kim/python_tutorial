import sys

with open('myfile.txt', 'r', encoding='utf-8') as f:
    for line in list(f):
        try:
            i = int(line.strip())
            print('line : ', line, ' i : ', i)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            print(f.name, 'has', len(line), 'lines')
