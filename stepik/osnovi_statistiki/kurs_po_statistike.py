import math
import statistics
from icecream import ic

some_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# Среднее значение - μ (мю)
average1 = statistics.mean(some_list1)
average2 = statistics.mean(some_list2)
x1 = some_list1[5]
x2 = some_list2[5]

# Дисперсия - средний квадрат отклонений индивидуальных значений признака от их средней величины
def find_variance(list):
    d = 0
    average = statistics.mean(list)
    for num in list:
        d += (num - average)**2
    # -1 для выборки; для генеральной совокупности - число элементов
    d = d / (len(list) - 1)
    return d

d1 = find_variance(some_list1)
d2 = find_variance(some_list2)

# Стандартное отклонение (σ) - корень из дисперсии
# 68% всех элементов лежат в диапазоне +- 1 сигма, 95% +- 2 сигмы, 99% +- 3 сигмы
sd1 = math.sqrt(d1)
sd2 = math.sqrt(d2)

# Z-преобразование
xz1 = (x1 - average1) / sd1
xz2 = (x2 - average2) / sd2

# Стандартная ошибка среднего
se1 = sd1 / math.sqrt(len(some_list1))
se2 = sd2 / math.sqrt(len(some_list2))

# Распределение Стьюдента (t-распределение). Применяется, когда число наблюдений невелико и 
# стандартное отклонение генеральной совокупности неизвестно. Важный параметр, определяющий форму
# распределения - степень свободы (df = n - 1). Чем больше df, тем ближе распределение к нормальному.

# Обратите внимание, что для расчета стандартной ошибки мы используем именно стандартное отклонение 
# в генеральной совокупности - σ. Ранее мы уже обсуждали, что на практике σ нам практически никогда 
# неизвестна, и для расчета стандартной ошибки мы используем выборочное стандартное отклонение.

# Так вот, строго говоря в таком случае распределение отклонения выборочного среднего и среднего в 
# генеральной совокупности, деленного на стандартную ошибку, теперь будет описываться именно при 
# помощи t - распределения.
t = (x1 - average1) / se1

# t-критерий Стьюдента - позволяет сравнить между собой два выборочных средних.
t_test = ((x1 - x2) - (average1 - average2)) / math.sqrt(((sd1**2) / len(some_list1)) + ((sd2**2) / len(some_list2)))
df_sum = len(some_list1) + len(some_list2) - 2

# ic(len(some_list1))
# ic(d1)
# ic(sd1)
# ic(xz1)
# ic(se1)
# ic(t)
# ic(t_test)
# ic(df_sum)

# Задача 2.2.12
x = 89.9
sd = 11.3
n = 20
df = n - 1
se = (sd / math.sqrt(n)) * 2.093
x11 = x + se
x12 = x - se
# ic(se)
# ic(x11)
# ic(x12)

# Задача 2.2.13
xm = 45
sdm = 9
nm = 1000
xw = 34
sdw = 10
nw = 100
df_sum = nm + nw - 2
t_test = (xm - xw) / math.sqrt(((sdm**2) / nm) + ((sdw**2) / nw))
# ic(df_sum)
# ic(t_test)

#TODO Тест Шапиро-Вилка
#TODO U-критерий Манна-Уитни

# Однофакторный дисперсионный анализ. m - число групп.
m = 3

list1 = [3, 1, 2]
list1_avg = statistics.mean(list1)
list2 = [5, 3, 4]
list2_avg = statistics.mean(list2)
list3 = [7, 6, 5]
list3_avg = statistics.mean(list3)
x_avg = (list1[0] + list1[1] + list1[2] + 
         list2[0] + list2[1] + list2[2] + 
         list3[0] + list3[1] + list3[2]) / (len(list1) + len(list2) + len(list3))
# Общая изменчивость данных (сумма квадратов). 
# Подразделяется на сумму квадратов межгрупповую (SSB) и сумму квадратов внутригрупповая (SSW)
sst = (list1[0] - x_avg)**2  + (list1[1] - x_avg)**2 + (list1[2] - x_avg)**2 + (list2[0] - x_avg)**2  + (list2[1] - x_avg)**2 + (list2[2] - x_avg)**2 + (list3[0] - x_avg)**2  + (list3[1] - x_avg)**2 + (list3[2] - x_avg)**2
df_t = len(list1) + len(list2) + len(list3) - 1

ssw = (list1[0] - list1_avg)**2  + (list1[1] - list1_avg)**2 + (list1[2] - list1_avg)**2 + (list2[0] - list2_avg)**2  + (list2[1] - list2_avg)**2 + (list2[2] - list2_avg)**2 + (list3[0] - list3_avg)**2  + (list3[1] - list3_avg)**2 + (list3[2] - list3_avg)**2
df_w = len(list1) + len(list2) + len(list3) - m

ssb = len(list1) * (list1_avg - x_avg)**2  + len(list2) * (list2_avg - x_avg)**2 + len(list3) * (list3_avg - x_avg)**2
df_b = m - 1

# sst = ssw + ssb. Если ssb > ssw, то группы значительно отличаются между собой. 
# В противном случае большая часть имеющейся изменчивости обеспечивается внутри группы.

f = (ssb / df_b) / (ssw / df_w)

ic(x_avg)
ic(sst)
ic(df_t)
ic(ssw)
ic(df_w)
ic(ssb)
ic(df_b)
ic(f)

# Множественные сравнения. Поправка Бонферрони - чтобы удержать требуемый р-уровень значимости, 
# необходимо его разделить на (кол-во групп * (кол-во групп - 1) / 2)

#TODO Критерий Тьюки
