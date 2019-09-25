import csv


gaps_list = [656, 706, 1728, 1767, 2791, 2830, 3858, 3896, 4921, 4960, 5994, 6048, 7064, 7104]

gaps = zip(gaps_list[::2], gaps_list[1::2])
print(list(gaps))

with open('output.csv', 'a') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerow(['Slot', 'Gap Start', 'Gap End', 'Gap'])
    for idx, gap in enumerate(list(gaps)):
        print('{}. Gap Start: {}. Gap End: {}. Gap: {}'.
              format(idx + 1, gap[0], gap[1], gap[1] - gap[0]))
        gaps = [idx + 1, gap[0], gap[1], gap[1] - gap[0]]
        writer.writerow(gaps)
#gap_starts = []
# for idx, gap in enumerate(list(gaps)):
#      print('{}. Gap Start: {}. Gap End: {}. Gap: {}'.
#                format(idx + 1, gap[0], gap[1], gap[1] - gap[0]))
# #     gap_starts.append(gap[0])
# print('Delta Between Gap Starts')
# print([y - x for x, y in zip(gap_starts, gap_starts[1:])])

# with open('output.csv', 'a') as f:
#     writer = csv.writer(f, dialect='excel')
#     writer.writerow(['Slot', 'Gap Start', 'Gap End', 'Gap'])
#     for idx, gap in enumerate(list(gaps)):
#         gaps = [idx + 1, gap[0], gap[1], gap[1] - gap[0]]
#         writer.writerow(gaps)

# gap_start_list = []
# with open('output.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row['Gap Start'] != 'Gap Start':
#             gap_start = row['Gap Start']
#             gap_start_list.append(int(gap_start))

#print(gap_start_list)
# my_list = [0, len(gap_start_list), 7]
# for i in my_list:
#     print(i)

# for i in range(0, len(gap_start_list), 7):
#     print(i)
#print(gap_start_list)
# print(gap_start_list[0:len(gap_start_list):1])
# print(gap_start_list[0:len(gap_start_list):2])
# print(gap_start_list[0:len(gap_start_list):3])
# print(gap_start_list[0:len(gap_start_list):4])
# print(gap_start_list[0:len(gap_start_list):5])
# print(gap_start_list[0:len(gap_start_list):6])


# xyz = [y - x for x, y in zip(gap_start_list, gap_start_list[1:])]
# bb = []
# print('Delta Between Gap Starts')
# for idx, item in enumerate([y - x for x, y in zip(gap_start_list, gap_start_list[1:])]):
#     if item > 0:
#         #print('{}. Delta {}.'.format(idx + 1, item))
#         bb.append('{}. Delta {}.'.format(idx + 1, item))
# print(bb)