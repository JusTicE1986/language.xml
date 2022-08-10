import re
class Language():
    #def __init__(self):

    @staticmethod
    def read_languages(filename):
        value_entry = {}
        with open(f'Source/{filename}', "r", encoding="UTF-8") as source_file:
            keys = source_file.readlines()
            for key in keys:
                if re.search("gentext", key):
                    value_entry.update({key.split('"')[1]: key.split('"')[3]})
        return value_entry

    @staticmethod
    def read_dict():
        dict_key = []
        with open(f'Source/Language_de.xml', "r", encoding="UTF-8") as source_file:
            keys = source_file.readlines()
            for key in keys:
                if re.search("gentext", key):
                    dict_key.append(key.split('"')[1])
        return dict_key