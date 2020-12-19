import json

def selection_string_converter(lst):
    comm = ''
    column_names_from_select = []
    for x in lst:
        column_names_from_select.append(x['column'])
        if lst.__len__() != (lst.index(x)+1):
            comm = comm + x['column'] + ", "
        else:
            comm = comm + x['column']
    return comm, column_names_from_select

def operation_handler(list_of_data):
    operations_str = ''
    column_names__from_operations = []
    for operation in list_of_data:
        column = operation['column']
        function = operation['type']
        new_column = '%s_of_%s' %(function, column)
        operations_str = operations_str + ', ' + function + '(%s) ' %column + 'AS ' + new_column
        column_names__from_operations.append(new_column)
    return operations_str, column_names__from_operations

class SqlParse:

    @classmethod
    def choice_select(cls, json_data):
        if "select_list" in json_data.keys():
            lst = json_data['select_list']
            comm, column_names_from_select = selection_string_converter(lst)
            sel_string = comm
            return column_names_from_select, sel_string
        elif "aggregate" in json_data.keys():
            lst = json_data['groupby']
            comm, column_names_from_select = selection_string_converter(lst)
            sel_string = comm
            return column_names_from_select, sel_string
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
            comm, column_names_from_select = selection_string_converter(colm)
            return " GROUP BY " + comm

def sql_wrappr(json_data):
    SQL = ""
    column_names = []
    column_names_from_select, sel_string = SqlParse.choice_select(json_data)
    column_names = column_names + column_names_from_select
    SQL = SQL + sel_string
    if "aggregate" in json_data.keys():
        operations_str, column_names__from_operations = SqlParse.operation(json_data)
        column_names = column_names + column_names__from_operations
        SQL = SQL + operations_str
    SQL = SQL + " FROM " + "tours_"+json_data['worksheet_id']
    if "groupby" in json_data.keys():
        SQL = SQL + SqlParse.group_by(json_data)
    final_sql = 'SELECT ' + SQL
    return final_sql, column_names
    




# def raw_sql_to_json(raw_sql, column):
#     for x in raw_sql:
#         for 
