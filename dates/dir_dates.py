import os
import time



def dir_create_date_list(path):
    """Получение списка даты создания директории (Win/Linux)"""
    created_dir = time.ctime(os.path.getctime(path))
    created_dir = created_dir.split()
    created_year = created_dir[4]
    month = created_dir[1]
    month = time.strptime(month,'%b').tm_mon
    if month < 10:
        created_month = '0' + str(month)
    else: 
        created_month = str(month)
    if int(created_dir[2]) < 10:
        created_day = '0' + created_dir[2]
    else:
        created_day = created_dir[2]
    created_time = created_dir[3]
    created_week_day = created_dir[0]

    return created_year, created_month, created_day, created_time, created_week_day


def dir_mod_date_list(path):
    """Получение списка даты последнего изменения директории (Win/Linux)"""
    last_modified = time.ctime(os.path.getmtime(path))
    last_modified = last_modified.split()
    modified_year = last_modified[4]
    month = last_modified[1]
    month = time.strptime(month,'%b').tm_mon
    if month < 10:
        modified_month = '0' + str(month)
    else: 
        modified_month = str(month)
    if int(last_modified[2]) < 10:
        modified_day = '0' + last_modified[2]
    else:
        modified_day = last_modified[2]
    modified_time = last_modified[3]
    modified_week_day = last_modified[0]

    return modified_year, modified_month, modified_day, modified_time, modified_week_day


def dir_create_date_dict(path):
    """Получение словаря даты создания директории (Win/Linux)"""
    created_dir = time.ctime(os.path.getctime(path))
    created_dir = created_dir.split()
    created_dir_dict = {}
    created_year = created_dir[4]
    month = created_dir[1]
    month = time.strptime(month,'%b').tm_mon
    if month < 10:
        created_month = '0' + str(month)
    else: 
        created_month = str(month) 
    created_week_day = created_dir[0]
    if int(created_dir[2]) < 10:
        created_day = '0' + created_dir[2]
    else:
        created_day = created_dir[2]
    created_time = created_dir[3]

    created_dir_dict.update({"created_year":created_year,
                             "created_month":created_month, 
                             "created_day":created_day, 
                             "created_time":created_time, 
                             "created_week_day":created_week_day})
    
    return  created_dir_dict


def dir_mod_date_dict(path):
    """Получение словаря даты последнего изменения директории (Win/Linux)"""
    last_modified = time.ctime(os.path.getmtime(path))
    last_modified = last_modified.split()
    modified_dir_dict = {}
    modified_year = last_modified[4]
    month = last_modified[1]
    month = time.strptime(month,'%b').tm_mon
    if month < 10:
        modified_month = '0' + str(month)
    else: 
        modified_month = str(month)
    if int(last_modified[2]) < 10:
        modified_day = '0' + last_modified[2]
    else:
        modified_day = last_modified[2]
    modified_time = last_modified[3]
    modified_week_day = last_modified[0]
    
    modified_dir_dict.update({"modified_year":modified_year,
                              "modified_month":modified_month, 
                              "modified_day":modified_day, 
                              "modified_time":modified_time, 
                              "modified_week_day":modified_week_day})
    
    return modified_dir_dict



# path = r"C:\Program Files"
# path = r"/home"
# print("dir_create_list: ", dir_create_date_list(path))
# print("last_modified_list: ", dir_mod_date_list(path))
# print("dir_create_dict: ", dir_create_date_dict(path))
# print("last_modified_dict: ", dir_mod_date_dict(path))
