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


if __name__ == '__main__':
    horses = generate_racing_horse_dict()
    print(horses)
