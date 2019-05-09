# -*- coding: utf-8 -*-


class Bitmap:
    def __init__(self, maxValue=31, array=None):
        if maxValue < 0:
            raise BaseException("最大值不能小于0。")
        self.max = maxValue
        if array:
            self.max = int(max(array))
        self.size = self.__getIndex(self.max)[0] + 1
        self.array = [0] * self.size
        if array:
            for i in range(len(array)):
                self.set(array[i])

    # 获取数组的索引、位的索引
    def __getIndex(self, num):
        aIndex = int(num / 32)
        bIndex = num % 32
        return aIndex, bIndex

    # 改变数组长度
    def __changeLength(self, aIndex, bIndex):
        self.max = aIndex * 32 + bIndex
        self.size = aIndex + 1
        newArray = [0] * self.size
        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        self.array = newArray

    '''
     添加数据
     先求得该数对应的数组索引以及位的索引
     如果要将该数对应的位置为1（value=True）,则用当前数组的数与1右移该数对应的位索引求或
     如果要将该数对应的位置为0（value=False）,则用当前数组的数与1右移该数对应的位索引取反后求与
    '''

    def set(self, num, value=True):
        aIndex, bIndex = self.__getIndex(int(num))
        if aIndex >= self.size:
            self.__changeLength(aIndex, bIndex)
        arrayNum = self.array[aIndex]
        if value:
            self.array[aIndex] = arrayNum | (1 << bIndex)
        else:
            temp = 1 << bIndex
            ft = ~temp
            self.array[aIndex] = arrayNum & ft

    '''
    判断某个数是存在
    先求得该数对应的数组索引以及位的索引，用数组当前索引对应的数与1右移该数对应位的索引位求与
    结果不为0表示存在，否则不存在
    '''

    def isExist(self, num):
        aIndex, bIndex = self.__getIndex(num)
        arrayNum = self.array[aIndex]
        if arrayNum & (1 << bIndex):
            return True
        return False

    def __getNewMaxValue(self, newArray):
        for i in range(len(newArray) - 1, -1, -1):
            if newArray[i]:
                isEnd = False
                for n in range((i + 1) * 32 - 1, i * 32 - 1, -1):
                    aIndex, bIndex = self.__getIndex(n)
                    arrayNum = newArray[aIndex]
                    if arrayNum & (1 << bIndex):
                        return n
        return 0

    '''
    求自身与bitmap的交集，返回一个新的Bitmap对象
    例如：
    self表示养猫的人，bitmap表示养狗的人
    那么，and_的结果表示猫狗都养的人
    '''

    def and_(self, bitmap):
        size = self.size if self.size < bitmap.size else bitmap.size
        newArray = [0] * size
        for i in range(size):
            newArray[i] = self.array[i] & bitmap.array[i]
        maxValue = self.__getNewMaxValue(newArray)
        newBitmap = Bitmap(maxValue)
        newBitmap.array = newArray
        return newBitmap

    '''
    求自身与bitmap的并集，返回一个新的Bitmap对象
    例如：
    self表示养猫的人，bitmap表示养狗的人
    那么，or_的结果表示养猫或养猫或者猫狗都养的人
    '''

    def or_(self, bitmap):
        newArray = []
        if self.size > bitmap.size:
            newArray = self.array.copy()
        else:
            newArray = bitmap.array.copy()
        size = self.size if self.size < bitmap.size else bitmap.size
        for i in range(size):
            newArray[i] = self.array[i] | bitmap.array[i]
        maxValue = self.__getNewMaxValue(newArray)
        newBitmap = Bitmap(maxValue)
        newBitmap.array = newArray
        return newBitmap

    '''
    除去在bitmap中存在的自身元素，返回一个新的Bitmap对象
    例如：
    self表示养猫的人，bitmap表示养狗的人
    那么，andNot的结果表示只养猫的人
    '''

    def andNot(self, bitmap):
        andBitmap = self.and_(bitmap)
        newArray = self.array.copy()
        for i in range(andBitmap.size):
            newArray[i] = self.array[i] ^ andBitmap.array[i]
        maxValue = self.__getNewMaxValue(newArray)
        newBitmap = Bitmap(maxValue)
        newBitmap.array = newArray.copy()
        return newBitmap

    '''
    求出自身与bitmap的并集元素，再去除自身与bitmap的交集元素
    例如：
    self表示养猫的人，bitmap表示养狗的人
    那么，xor的结果表示只养猫或者只养狗的人
    '''

    def xor(self, bitmap):
        orBitmap = self.or_(bitmap)
        andBitmap = self.and_(bitmap)
        newArray = orBitmap.array
        for i in range(andBitmap.size):
            newArray[i] = newArray[i] ^ andBitmap.array[i]
        maxValue = self.__getNewMaxValue(newArray)
        newBitmap = Bitmap(maxValue)
        newBitmap.array = newArray
        return newBitmap

    '''
    排序，返回排序后的列表
    desc为True降序，否则升序
    '''

    def sort(self, desc=False):
        result = []
        for i in range(self.max + 1):
            if self.isExist(i):
                result.append(i)
        if desc:
            return result[::-1]
        else:
            return result


if __name__ == "__main__":
    # 利用bitmap对数组排序
    array1 = [1, 31, 15, 45, 123, 344]
    bitmap1 = Bitmap(array=array1)
    print("原数组：" + str(array1))
    print("升序排序：" + str(bitmap1.sort()))
    print("降序排序：" + str(bitmap1.sort(desc=True)))

    # 利用bitmap对数组去重
    array2 = [1, 33, 34, 1, 33, 532, 232, 532, 543, 99]
    bitmap2 = Bitmap(array=array2)
    print("原数组：" + str(array2))
    print("去掉重复数据后的数组为：" + str(bitmap2.sort()))

    # 判断某个数据是否在数组中
    num = 99
    judge = "在" if bitmap2.isExist(num) else "不在"
    print("%d%s数组中" % (num, judge))

    '''
    集合操作
    例子：列表list1表示喜欢刘亦非的人的id，列表list2表示喜欢angelababy的人
    '''
    list1 = [2, 10, 12, 43, 45, 112, 345, 645, 1243, 10982]
    list2 = [4, 16, 12, 48, 49, 345, 564, 786, 6554, 10982, 50982]
    bitmap1 = Bitmap(array=list1)
    bitmap2 = Bitmap(array=list2)
    bitmap3 = bitmap1.or_(bitmap2)
    print("喜欢刘亦非或者喜欢angelababy的人有：" + str(bitmap3.sort()))
    bitmap3 = bitmap1.and_(bitmap2)
    print("既喜欢刘亦非又喜欢angelababy的人有：" + str(bitmap3.sort()))
    bitmap3 = bitmap1.andNot(bitmap2)
    print("喜欢刘亦非但不喜欢angelababy的人有：" + str(bitmap3.sort()))
    bitmap3 = bitmap1.xor(bitmap2)
    print("只喜欢刘亦非或只喜欢angelababy的人有：" + str(bitmap3.sort()))
