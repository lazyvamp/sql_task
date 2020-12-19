import json

def selection_string_converter(lst):
    comm = ''
    for x in lst:
        if lst.__len__() != (lst.index(x)+1):
            comm = comm + x['column'] + ","
        else:
            comm = comm + x['column']
    return comm

def operation_handler(list_of_data):
    operations_str = ''
    column_names = []
    for operation in list_of_data:
        column = operation['column']
        function = operation['type']
        new_column = '%s_of_%s' %(function, column)
        operations_str = operations_str + ', ' + function + '(%s) ' %column + 'AS ' + new_column
        column_names.append(new_column)
    return operations_str, column_names

class SqlParse:

    @classmethod
    def choice_select(cls, json_data):
        if "select_list" in json_data.keys():
            lst = json_data['select_list']
            return "id, " + selection_string_converter(lst)
        elif "aggregate" in json_data.keys():
            lst = json_data['groupby']
            return "id, " + selection_string_converter(lst)
        else:
            return "* "

    @classmethod
    def operation(cls, json_data):
        op_list = json_data['aggregate']
        return operation_handler(op_list) 

    @classmethod
    def group_by(cls, json_data):
        if "groupby" in json_data.keys():
            colm = json_data["groupby"]
            group_of = selection_string_converter(colm)
            return " GROUP BY " + group_of

def sql_wrappr(json_data):
    SQL = ""
    column_names = []
    selection = SqlParse.choice_select(json_data)
    column_names.append(selection)
    SQL = SQL + selection
    if "aggregate" in json_data.keys():
        operations_str, column_names = SqlParse.operation(json_data)
        SQL = SQL + operations_str
    SQL = SQL + " FROM " + "tours_"+json_data['worksheet_id']
    if "groupby" in json_data.keys():
        SQL = SQL + SqlParse.group_by(json_data)
    final_sql = 'SELECT ' + SQL
    return final_sql, column_names
    