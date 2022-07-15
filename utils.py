
import math


class SummaryStatistics:
    def __init__(self):
        return None

    def max(self, lst):
        max_num = 0
        for num in range(len(lst)):
            if len(lst) > 0 and float(lst[num]) > max_num:
                max_num = float(lst[num])
        return max_num

    def min(self, lst):
        min_num = self.max(lst)
        for num in range(len(lst)):
            if len(lst) > 0 and float(lst[num]) < min_num:
                min_num = float(lst[num])
        return min_num

    def mean(self, lst, column_name):
        total_value = 0
        for index in range(len(lst)):
            if len(lst) > 0:
                total_value += float(lst[index])
        if total_value:
            col_mean = total_value / len(lst)
        if column_name == 'age':
            round_up_age = math.floor(col_mean)
            return f'The average age of the patients is {round_up_age} years!'
        elif column_name == 'bmi':
            round_up_bmi = round(col_mean, 2)
            return f'The average bmi of the patients is {round_up_bmi}!'
        elif column_name == 'charges':
            round_up_charges = round(col_mean, 2)
            return f'The average charge of the patients is {round_up_charges}!'
        else:
            return col_mean

    def median(self, lst):
        mid_index = len(lst) // 2
        lst_mod = len(lst) % 2
        print(mid_index)
        lst.sort()
        if lst_mod == 1:
            col_median = lst[mid_index]
        else:
            num_median = float(lst[int((len(lst)/2))]) + \
                float(lst[int((len(lst)/2 - 1))])
            col_median = num_median / 2
        return col_median

    def mode(self, lst):
        pass

    def std(self, lst):
        sum__square_total = 0
        for element in lst:
            sum__square_total += (int(element) - self.mean(lst)) ** 2
        col_std = (sum__square_total / len(lst)) ** 0.5
        return col_std

    def range(self, lst, column_name):
        if column_name == 'age':
            return f'The patient age is within the range of {self.max(lst) - self.min(lst)}'
        elif column_name == 'bmi':
            return f'The patient bmi value is within the range of {self.max(lst) - self.min(lst)}'
        elif column_name == 'charges':
            return f'The charges is within the range of {self.max(lst) - self.min(lst)}'
        else:
            self.max(lst) - self.min(lst)


class PatientsByRegion:
    def __init__(self):
        return None

    def region(self, lst):
        region_dict = dict()
        for region in lst:
            if region in region_dict.values():
                region_dict[region] += 1
            else:
                region_dict[region] = 1
        return region_dict
