from numpy import *

def loadDataSet(filename): #读取数据
    dataMat=[]
    labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=line.strip().split('   ')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        # dataMat.append([float(lineArr[0][0])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat #返回数据特征和数据类别



#主程序
def main():
    # filename_traindata='C:\\Users\\Administrator\\Desktop\\data\\traindata.txt'
    filename_traindata="/Users/catch/Documents/courses/cs124/assignments/svm/data/traindata.txt"
    # filename_testdata='C:\\Users\\Administrator\\Desktop\\data\\testdata.txt'
    # testRbf(filename_traindata,filename_testdata)
    print(loadDataSet(filename_traindata))
    return loadDataSet(filename_traindata)

if __name__=='__main__':
    main()


