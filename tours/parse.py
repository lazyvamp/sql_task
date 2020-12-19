import json

def sel_made(lst):
    comm = ''
    for x in lst:
        if lst.__len__() != (lst.index(x)+1):
            comm = comm + x['column'] + ","
        else:
            comm = comm + x['column']
    return comm

class SqlParse:
    pre = 'SELECT '

    @classmethod
    def choice_select(cls, json_data):
        if "select_list" in json_data.keys():
            lst = json_data['select_list']
            return sel_made(lst)
        elif "aggregate" in json_data.keys():
            lst = json_data['groupby']
            return sel_made(lst)
        else:
            return "* "

    @classmethod
    def operation(cls, json_data):
        fun = json_data['aggregate'][0]['type']
        return ',' + fun + '(%s)'

    @classmethod
    def group_by(cls, json_data):
        pass



    