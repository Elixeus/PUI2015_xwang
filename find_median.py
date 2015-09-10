import sys

# class/function definition

if __name__=='__main__':
    myList = []
    for fileName in sys.argv[1:]:
        inputFile = open(fileName, 'r')
        for line in inputFile:
            myList.append(int(line.strip()))
    myList.sort()
    print myList[len(myList)/2]
