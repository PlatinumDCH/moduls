def get_nums(num:int):
    list_ = list(str(num))
    return list_

def get_result(nums:list[str])->str:
    """
    num = abcd
    condition a+d == b-c
    """
    cond_1 = int(nums[0]) + int(nums[-1])
    cond_2 = int(nums[1]) - int(nums[2])
    print(cond_1)
    print(cond_2)
    return 'ДА' if cond_1 == cond_2 else 'НЕТ'

if __name__ == '__main__':
    num = int(input())
    prepear_nums = get_nums(num)
    result = get_result(prepear_nums)
    print(result)
