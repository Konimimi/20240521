def generate_racing_horse_dict():
    ret_dict = {
        'Symboli Rudolf': {
            'birthdate': '19830413',
            'race_num': 16,
            'win_num': 13,
            'win_ratio': 13/16,
            'Sire': 'Partholon',
            'Dam': 'Sweet Luna'},
        'Contrail': {
            'birthdate': '20170401',
            'race_num': 11,
            'win_num': 8,
            'win_ratio': 8/11,
            'Sire': 'Deep Impact',
            'Dam': 'Rhodochrosite'},
        'Deep Impact': {
            'birthdate': '20020325',
            'race_num': 14,
            'win_num': 12,
            'win_ratio': 12/14,
            'Sire': 'Sunday Silence',
            'Dam': 'Wind in Her Hair'}
        }
    return ret_dict

def get_top():
    race_horse_dict = generate_racing_horse_dict()
    comp_race = 0
    comp_win = 0
    comp_ratio = 0
    top_race = ''
    top_win = ''
    top_ratio = ''
    for horse in race_horse_dict.keys():
        info = race_horse_dict[horse]
        if int(info['race_num']) >= int(comp_race):
            comp_race = info['race_num']
            top_race = horse
        if int(info['win_num']) >= int(comp_win):
            comp_win = info['win_num']
            top_win = horse
        if int(info['win_ratio']) >= int(comp_ratio):
            comp_tatio = info['win_ratio']
            top_ratio = horse
    return {'top_run': top_race,'topwin': top_win,'top_ratio': top_ratio}
    


if __name__ == '__main__':
    horses = get_top()
    print(horses)
