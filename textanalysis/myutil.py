import sys

#stolen from http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(barLength * iteration // total)
    bar = fill * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

#
# Sample Usage
#

def main():

    l = 10000
    i = 0

    printProgress(i, l, prefix='Progress:', suffix='Complete', barLength=50)
    for i in range(0,l):
        printProgress(i, l, prefix='Progress:', suffix='Complete', barLength=50)
    print("done")
if __name__ == '__main__':
    main()
