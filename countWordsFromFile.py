def countWordsFromFile():
    fileName=input("Enter The Filename: ")
    noOfWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split(",")
        noOfWords=noOfWords+len(words)
    print("Number Of Words:-",noOfWords)

countWordsFromFile()


