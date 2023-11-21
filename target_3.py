import os

with (open('1.txt', 'r', encoding='UTF-8') as file_1):
    with open('2.txt', 'r', encoding='UTF-8') as file_2:
        with open('3.txt', 'r', encoding='UTF-8') as file_3:

            a = file_1.readlines()
            b = file_2.readlines()
            c = file_3.readlines()

            num_lines_1 = sum(1 for line in a)
            num_lines_2 = sum(1 for line in b)
            num_lines_3 = sum(1 for line in c)

            section_1 = ('1.txt', num_lines_1, a)
            section_2 = ('2.txt', num_lines_2, b)
            section_3 = ('3.txt', num_lines_3, c)

            info = {}
            info = {num_lines_1:(section_1), num_lines_2:(section_2),
                    num_lines_3:(section_3)}
            info_sort = sorted(info.items())

            story = dict(info_sort)
            print(*list(story.values()), sep=', ')
