class DictionaryMaker:


    if __name__ == "__main__":
        fileList = []
        count = 0

        #only the first word of each line in the adj.txt and index.txt files needs to be parsed
        adj_file = open('adj.txt','r')
        af_lines = adj_file.readlines()
        for phrase in af_lines: 
            fileList.append(phrase.split()[0])
            count += 1
        adj_file.close()
        #print fileList


        index_file = open('index.txt','r')
        if_lines = index_file.readlines()
        for phrase in if_lines:
            fileList.append(phrase.split()[0])
            count += 1
        index_file.close()
        # print fileList

        file = open("foo.txt", "wb")

        for line in fileList:
            line += "\n"
            file.write(line)

