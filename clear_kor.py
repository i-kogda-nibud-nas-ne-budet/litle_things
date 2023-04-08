def clear_kor(filename):
    with open(filename, 'r') as f:
        data=f.readlines()
        first_index=data.index('layout\n')+1
        second_index=data.index('end\n')
        data=data[first_index:second_index]
        with open('clear_'+filename, 'w') as cl:
            cl.write(''.join(data))
clear_kor('0000.krs')