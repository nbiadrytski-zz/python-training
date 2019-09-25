# # def get_temperature(self):
# #     lines = self._read_temp_raw(self.device)
# #     if lines[0].strip()[-3:] == 'YES':
# #         equals_pos = lines[1].find('t=')
# #         if equals_pos != -1:
# #             temp_string = lines[1][equals_pos + 2:]
# #             return round(float(temp_string) / 1000.0, 1)
# #     return -1
# #
# #
# # round(float(temp_string) / 1000.0, 1)
#
# # t = 36187
# # print(round(float(t) / 1000.0, 1))
#
# # f = open("tm.txt", "r")
# # f.read()
# # equals_pos = lines[1].find('t=')
# file_variable = open("tm.txt", "r")
# all_lines_variable = file_variable.readlines()
# #print(all_lines_variable[1 - 1])
# equals_pos = all_lines_variable[1 - 1].find('t=')
# print(equals_pos)
#
# temp_string = all_lines_variable[1 - 1][equals_pos + 2:]
# print(round(float(temp_string) / 1000.0, 1))


def get_temperature():
    lines = _read_temp_raw("tm.txt")
    if lines[0].strip()[-3:] == 'YES':
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            return round(float(temp_string) / 1000.0, 1)

    return -1


def _read_temp_raw(device):
    f = open(device, 'r')
    lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    vv = get_temperature()
    print(vv)