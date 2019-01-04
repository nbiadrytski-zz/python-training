grades = [10, 7, 8, 3, 5, 9, 8, 10]


def drop_first_last(grades):
    first_semester, *middle_semester, last_semester = grades
    avg = sum(middle_semester) / len(middle_semester)
    return print(avg)


drop_first_last(grades)