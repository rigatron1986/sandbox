from core.db_connect import mySql_lib


bundle_data = {}
sql = "SELECT * FROM `bundles` WHERE 1 ORDER BY id DESC"
result = mySql_lib.runquery("rigasite", sql)
print(result)
if result['Has Succeded']:
    for data in result['message']:
        if data[1] not in bundle_data:
            bundle_data[data[1]] = {}
        if data[2] not in bundle_data[data[1]]:
            bundle_data[data[1]][data[2]] = []
        bundle_data[data[1]][data[2]].append(data[3])
    # self.bundle_data = result['message']
print(bundle_data)
