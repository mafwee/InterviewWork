deviders_list = [3, 5, 9, 10]


def test(deviders, range_from, range_to):
    final_message = [str(num) for num in range(range_from, range_to)]
    all_match = [True] * len(deviders)

    for step in range(len(final_message)):
        mark=[]
        for devider in deviders:
            if (step+1) % devider == 0:
                mark += [True]
                if mark == all_match:
                    final_message[step] = 'Кратно всем значениям'
                else:
                    if 'Кратно' in final_message[step]:
                        final_message[step] += f',{devider}'
                    else:
                        final_message[step] = f'Кратно {devider}'
    return final_message

print(test(deviders_list, 1, 201))
