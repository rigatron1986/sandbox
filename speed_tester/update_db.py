import mySql_lib as sqlDb

metadata = {
    'download': 88612752.23741339, 'upload': 47304184.204287864, 'ping': 72.164,
    'server':
        {
            'url': 'http://speedtestmh.airtelbroadband.in:8080/speedtest/upload.php', 'lat': '18.9647',
            'lon': '72.8258', 'name': 'Mumbai', 'country': 'India', 'cc': 'IN',
            'sponsor': 'Airtel Broadband',
            'id': '19081', 'host': 'speedtestmh.airtelbroadband.in:8080', 'd': 1038.8734366241058,
            'latency': 72.164}, 'timestamp': '2022-08-11T14:39:27.030428Z', 'bytes_sent': 59621376,
    'bytes_received': 111269994, 'share': 'http://www.speedtest.net/result/13526955268.png',
    'client':
        {
            'ip': '122.174.229.157', 'lat': '12.8996', 'lon': '80.2209', 'isp': 'Airtel Broadband',
            'isprating': '3.7', 'rating': '0', 'ispdlavg': '0', 'ispulavg': '0', 'loggedin': '0',
            'country': 'IN'
        }
}

import json
database = "rigasite"
metadata['metadata'] = json.dumps(metadata)
print(metadata)
_sql = "INSERT INTO `Speed_Test` (`id`, `upload`, `download`, `ping`, `share`, `metadata`, `timestamp`) " \
       "VALUES (NULL, '3435', '4534', '543534', 'tagg', 'gsg', current_timestamp());"
sql = "INSERT INTO `Speed_Test` (`id`, `upload`, `download`, `c_ping`, `share`, `metadata`, `timestamp`) " \
      "VALUES (NULL, '{upload}', '{download}', '{ping}', '{share}', '{metadata}', current_timestamp());".format(
    **metadata)
print(sql)
# sql = "INSERT INTO `speed_test` (`id`, `upload`, `download`, `ping`, `share`, `metadata`, `timestamp`) VALUES (NULL, '47304184.204287864', '88612752.23741339', '72.164', 'http://www.speedtest.net/result/13526955268.png', 'll', current_timestamp());"
sql = "SELECT  * FROM speed_test"
result = sqlDb.runquery(database, sql)
print(result)
"""
INSERT INTO `Speed_Test` (`id`, `upload`, `download`, `ping`, `share`, `metadata`, `timestamp`) VALUES (NULL, '47304184.204287864', '88612752.23741339', '72.164', 'http://www.speedtest.net/result/13526955268.png', '', current_timestamp());
"""
