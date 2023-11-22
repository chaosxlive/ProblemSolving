# https://leetcode.com/problems/create-a-new-column/

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(2, 'bonus', employees.loc[:, ['salary']].mul(2))
    return employees
