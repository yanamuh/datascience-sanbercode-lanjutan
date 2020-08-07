import json
from openpyxl import Workbook, load_workbook

# open excel
def open_excel():
    data = load_workbook(filename='pokemon_db.xlsx')
    sheet = data.active
    return sheet

# conver excel to json
def convert_dict(sheet):
    pokemon_data = []
    for row_index in range(len(sheet['A'])):
        if sheet[row_index+1][0].value == 'Name':
            continue
        else:
            pokemon = {}
            pokemon['Name'] = sheet[row_index+1][0].value
            pokemon['Type'] = sheet[row_index+1][1].value
            pokemon['Total'] = sheet[row_index+1][2].value
            pokemon['HP'] = sheet[row_index+1][3].value
            pokemon['Attack'] = sheet[row_index+1][4].value
            pokemon['Defense'] = sheet[row_index+1][5].value
            pokemon['SpAttack'] = sheet[row_index+1][6].value
            pokemon['SpDefense'] = sheet[row_index+1][7].value
            pokemon['Speed'] = sheet[row_index+1][8].value
            pokemon_data.append(pokemon)
    return pokemon_data

# save json
def save_json(json_to_save):
    with open('yanamuh.json', 'w') as json_file:
        json.dump(json_to_save, json_file)

# run
data = open_excel()
poke_data = convert_dict(data)
save_json(poke_data)