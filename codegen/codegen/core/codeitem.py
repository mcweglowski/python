class code_item(object):
    def __init__(self, dest_file, start_key, start_offset, end_key, line_pattern):
        self.dest_file    = dest_file
        self.start_key    = start_key
        self.start_offset = start_offset
        self.end_key      = end_key
        self.line_pattern = line_pattern

    def generate_code(dataset):
        column_field = 0
        column_id    = 1
        column_type  = 2
        return [line_pattern.format(field_name        = row[column_field].value, 
                                    field_name_quoted = "\"{}\"".format(row[column_field].value), 
                                    id                = row[column_id].value, 
                                    data_type         = row[column_type].value,
                                    field_name_field  = "{}Field".format(row[column_field].value),
                                    field_name_short  = "{}Short".format(row[column_field].value),
                                    field_name_descr  = "{}Description".format(row[column_field].value),
                                    field_id          = 485 + row[column_id].value * 3 + 0,
                                    short_id          = 485 + row[column_id].value * 3 + 1,
                                    descr_id          = 485 + row[column_id].value * 3 + 2)
                for row in worksheet_fields]