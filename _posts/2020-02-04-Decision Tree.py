import time
import numpy as np
import pandas as pd


# def bin_transf(x):

#     if x < 5:
#         return -1
#     else:
#         return 1

# Label = Label[0].apply(lambda x: bin_transf(x))

def loadData(fileName):

    Data = pd.read_csv(fileName, header = None).drop([0], axis=1)   # 读取第 1 列及之后列的数据
    Label = pd.read_csv(fileName, usecols = [0], header = None)     # 读取第 0 列数据作为标签

    Data = Data.apply(lambda x: x // 128)                           # 二值化处理，大于128置为 1 ，反之置 0
    Label = Label.apply(lambda x: x // 5)                           # 二值化处理，大于5置 1 ， 反之置 0

    return Data.values, Label.values                                # 返回的是 numpy 数组的形式

def majorClass(Label):                                              # 选出待选样本中数量最多标签作为主标签

    classDict = {}                                                  # 建立空字典

    for i in range(len(Label)):                 

        if Label[i] in classDict.keys():                            # 遍历所有键， 并统计各各标签出现的次数
            classDict[Label[i]] += 1
        else:
            classDict[Label[i]] = 1

    classSort = sorted(classDict.items(), key=lambda x: x[1], reverse=True) # 排序，根据value，也就是每个键出现的次数选出最主要的键

    return classSort[0][0]

# Calculate the empirical entropy
def calc_HD(Label):                                                 # 根据公式计算经验熵的函数

    HD = 0                                                          # 初始化信息熵为0

    Label_set = set([label for label in Label])                     # 利用set函数选出Label的最小子集

    for i in Label_set:     

        Prob = Label[Label == 0].size / Label.size                  # 要对Dataframe使用类方法.values才能像数组一样调用他的值

        HD += -1 * Prob * np.log2(Prob)     

    return HD       

def calc_HDA(Features, Label):                                      # 计算经验条件熵

    HDA = 0                                                         # 初始化值

    Feature_set = set([feature for feature in Features])            # 找出单个特征取值范围的最小子集

    for feature in Feature_set:                                     # 计算条件经验熵

        HDA += (Features[Features == feature].size / Features.size) * calc_HD(Label[Features == feature])

    return HDA

def calc_BestFeature(Data, Label):                      # 选取信息增益最大的特征作为切分点对数据集进行切分

    feature_Num = Data.shape[0]                         # 获取当前数据集的特征数量，此处我们要求数据集的格式为 N x M 其中 N 为样本数量，M 为特征数量

    max_GDA = -1
    max_Feature = -1

    for loc in range(feature_Num):                      # 依次计算每个feature的信息增益，并返回信息增益最大的信息增益值 GDA 及对应 feature 的位置

        HD = calc_HD(Label)
        feature_single = Data[:][loc]

        GDA = HD - calc_HDA(feature_single, Label)

        if GDA > max_GDA:
            max_GDA = GDA
            max_Feature = loc

    return GDA, max_Feature

def getSubData(Data, Label, A, a):                      # 再选出最佳切分点之后就将最佳切分点的 feature 从数据集中剔除， 用剔除之后新的数据集来选择下一个最佳切分点。

    new_Data  = []
    new_Label = []

    for i in range(len(Data)):                          # 依次遍历所有样本，将第 A 个特征取值为 a 的的样本保存进新的子样本集中，同时剔除第 A 个特征

        if Data[i][A] == a:
            new_Data.append(Data[i][0:A].tolist() + Data[i][A+1:].tolist())
            new_Label.append(Label[i])

    return np.array(new_Data), np.array(new_Label)

def createTree(*DataSet):                               # 创建决策树

    epsilon = 0.1                                       # 信息增益的阈值为 0.1， 既如果信息增益低于 0.1， 那么就不再进行分叉，直接选取样本中数量最多的标签作为该节点的标签

    Data = DataSet[0]
    Label = DataSet[1].flatten()

    classDict = {label for label in Label}

    if len(classDict) == 1:
        return Label[0]

    elif len(Data[0]) == 0:
        return majorClass(Label)

    GDA, Ag = calc_BestFeature(Data, Label)

    if GDA < epsilon:
        return majorClass(Label)

    treeDict = {Ag:{}}

    treeDict[Ag][0] = createTree(getSubData(Data, Label, Ag, 0))
    treeDict[Ag][1] = createTree(getSubData(Data, Label, Ag, 1))

    return treeDict






Data, Label = loadData('mnist_test.csv')

Data.describe()

Data.shape[1]
temp = Data[:][784]
temp = calc_HDA(Data[:][1], Label)
len(Data)
a = []
b = [[1,2],[3,4]]
a.append(Data[1][1:])

len(a)
len(b)
b.shape

Data[:][784]
Data[0]
Data.values[0].size


Tree = {'label:': None, 'feature': 2, 'tree': {'否': {'label:': None, 'feature': 1, 'tree': {'否': {'label:': '否', 'feature': None, 'tree': {}}, '是': {'label:': '是', 'feature': None, 'tree': {}}}}, '是': {'label:': '是', 'feature': None, 'tree': {}}}}
features = ['老年', '否', '否', '一般']
Tree =  {2:{1:{}}}

Tree['tree']['否']['tree']['否']['label:']

Dic = {'姓名':'李南'}

for i in Dic:
    print(Dic[i])

(key, value), = Dic.items()

(key, value), = Tree.items()

key = Tree.keys()
value = Tree.values()

value.__name__

type(Tree[key]).__name__

Try_Tree = {89:{0:{38:{0:1, 1:0}}, 1:0}}

Try_Tree[89][0][38][1]

classDict = {label for label in Label.values.flatten()}

ziji = set(Data.values[0])
Data.values[0]


array = np.array([1,2,3,4,5])

for i in array:
    print(i)

array = Label.values

array

def Test(*DataSet):

    print(DataSet[0])
    print(DataSet[1])

Test(Data, Label)

temp = Label.flatten()
temp