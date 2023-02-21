from collections import defaultdict


def readText():
    t = 0
    new_dict = defaultdict(list)
    with open("C:\\Users\\Hsoon\\Desktop\\pagerank\\2.txt", "r") as f:
        for x in f:
            if x[0] == "t" and x[1] == "=":
                t = float(x.replace("t=", "").rstrip("\n"))
            else:
                y = x.split(",")
                y[1] = y[1].rstrip("\n")
                new_dict[y[0]].append(y[1])
    f.close()
    return new_dict, t


def writeText(scores):
    with open("C:\\Users\Hsoon\\Desktop\\pagerank\\result.txt", "w") as f:
        for key in scores:
            f.write(key)
            f.write("---->")
            f.write(str(scores[key]))
            f.write("\n")
        # f.write(str(scores))


def dividOfPagerank(pr, o):
    return pr / o


def pagerank(dictOfNodes, t, n, countOfRepeat):
    scores = {}
    x1 = t / n
    x2 = 1 - t
    i = 0
    while i < countOfRepeat:
        for node in dictOfNodes:
            if i == 0:
                scores[node] = {i: 1}
            else:
                listOfkeys = []
                for key in dictOfNodes:
                    if node in dictOfNodes[key]:
                        listOfkeys.append(key)
                result = 0
                for j in listOfkeys:
                    print(j)
                    result = result + dividOfPagerank(scores[j][i - 1], len(dictOfNodes[j]))
                result = x1 + (x2 * result)
                scores[node][i] = result
        i = i + 1
    return scores


dictOfNodes, t = readText()
scores = pagerank(dictOfNodes, t, len(dictOfNodes), 12)
writeText(scores)
