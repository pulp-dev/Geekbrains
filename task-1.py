class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def make_int(cls, element):
        nums = element.data.split('-')
        return int(nums[0]), int(nums[1]), int(nums[2])

    @staticmethod
    def is_data_valid(element):
        months = {'january': '1', 'february': '2', 'march': '3', 'april': '4',
                  'may': '5', 'june': '6', 'july': '7', 'august': '8', 'september': '9',
                  'october': '10', 'november': '11', 'december': '12'}
        nums = element.data.split('-')

        try:
            int(nums[1])
        except:
            nums[1] = months[nums[1].lower()]
            print(nums[1])

        if int(nums[0]) > 29 and nums[1] == '2':
            print('Неправильное число')
            nums[0] = input()
        elif int(nums[0]) > 30 and nums[1] in ['4', '6', '9', '11']:
            print('Неправильное число')
            nums[0] = input()
            element = Data.is_data_valid(element)
        elif int(nums[0]) > 31 and not nums[1] in ['2', '4', '6', '9', '11']:
            print('Неправильное число')
            nums[0] = input()

        try: int(nums[2])
        except:
            print('Неверный год')
            nums[2] = input()

        element.data = '-'.join(nums)
        return element


data = Data(input())
data = Data.is_data_valid(data)
print(Data.make_int(data))