import os

cards_dir = os.path.join(os.getcwd(),'cards')
os.chdir(cards_dir)

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if not file_name in ['dog', 'dragon', 'mahjong', 'phoenix', 'cardBack']:
        new_name = '{}-{}{}'.format(file_name[-1], file_name[:-1], file_ext)
        print('Processing: ', f)
        os.rename(f, new_name)
    else:
        print('Leaving the same: ', f)

for f in os.listdir():
    name, ext = os.path.splitext(f)
    s_name = name.split('-')
    if len(s_name) > 1:
        if s_name[1] == 'rot':
            s_name[1] = 'r'
            if s_name[0] == 't':
                s_name[0] = '10'
            elif s_name[0] == 'k':
                s_name[0] = 'K'
            elif s_name[0] == 't':
                s_name[0] = 'Q'
            elif s_name[0] == 'j':
                s_name[0] = 'J'
            elif s_name[0] == 'a':
                s_name[0] = 'A'
            os.rename(f, ''.join(s_name) + ext)
        elif s_name[1] == 'blau':
            s_name[1] = 'c'
            if s_name[0] == 't':
                s_name[0] = '10'
            elif s_name[0] == 'k':
                s_name[0] = 'K'
            elif s_name[0] == 't':
                s_name[0] = 'Q'
            elif s_name[0] == 'j':
                s_name[0] = 'J'
            elif s_name[0] == 'a':
                s_name[0] = 'A'
            os.rename(f, ''.join(s_name) + ext)
        elif s_name[1] == 'gruen':
            s_name[1] = 'g'
            if s_name[0] == 't':
                s_name[0] = '10'
            elif s_name[0] == 'k':
                s_name[0] = 'K'
            elif s_name[0] == 't':
                s_name[0] = 'Q'
            elif s_name[0] == 'j':
                s_name[0] = 'J'
            elif s_name[0] == 'a':
                s_name[0] = 'A'
            os.rename(f, ''.join(s_name) + ext)
        elif s_name[1] == 'schw':
            s_name[1] = 'b'
            if s_name[0] == 't':
                s_name[0] = '10'
            elif s_name[0] == 'k':
                s_name[0] = 'K'
            elif s_name[0] == 't':
                s_name[0] = 'Q'
            elif s_name[0] == 'j':
                s_name[0] = 'J'
            elif s_name[0] == 'a':
                s_name[0] = 'A'
            os.rename(f, ''.join(s_name) + ext)