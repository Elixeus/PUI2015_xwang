import sys
# class/function definition

if __name__=='__main__':
    myList = []
    for fileName in sys.argv[1:]:
        inputFile = open(fileName, 'r')
        for line in inputFile:
            myList.append(float(line.strip()))
    print sum(myList)/len(myList)
