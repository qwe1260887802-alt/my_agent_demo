def add(a, b):
    """返回两个数的和。"""
    return a + b


def average(numbers):
    """返回列表中所有数字的平均值。

    空列表没有平均值，抛出 ValueError。
    """
    if not numbers:
        raise ValueError("不能计算空列表的平均值")
    return sum(numbers) / len(numbers)
