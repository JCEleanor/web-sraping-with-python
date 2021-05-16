#to convert ['兒童', '合作', '策略'] into '兒童 合作 策略'
def get_str(lst):
    string = ''
    for item in lst:
        string += item + ','
    return(string)  