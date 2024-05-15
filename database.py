import sqlite3

import json


class Database:
    def __init__(self):
        self.con = sqlite3.connect("elements.db")
        self.cursor = self.con.cursor()

    def get_element_by_symbol(self, symbol: str):
        self.cursor.execute(f'SELECT Itemname, symbol, serialnumber, period, elementgroup, subgroup, atomicweight, '
                            f'Outerlayerelectronconfiguration, elementtype, Latinname, scientist FROM elements WHERE '
                            f'symbol = "{symbol}"')
        result = self.cursor.fetchone()

        element_dict = {
            'Name': result[0],
            'Symbol': result[1],
            'Number': result[2],
            'Period': result[3],
            'Group': result[4],
            'Subgroup': result[5],
            'AtomicWeight': result[6],
            'Outerlayerelectronconfiguration': result[7],
            'ElementType': result[8],
            'LatinName': result[9],
            'Scientist': result[10]
        }
        return element_dict

