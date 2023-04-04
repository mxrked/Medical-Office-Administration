"""
db.py - A set of functions for working with the clinics database.
Author: Jessica Weeks, Christian Fortin
"""

from misc_data_manger import MiscDataManager

if __name__ == "__main__":
    mdm = MiscDataManager()

    print(mdm.get_locations())
    
    mdm.__del__()
