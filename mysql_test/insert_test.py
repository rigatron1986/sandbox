import mySql_lib as sqlDb

database = "rigasite"


def get_create_database():
    sql = "CREATE TABLE IF NOT EXISTS speed_test (`id` INT NOT NULL AUTO_INCREMENT , `upload` FLOAT(20) NOT NULL , " \
          "`download` FLOAT(20) NOT NULL , `timestamp` TIMESTAMP NOT NULL , PRIMARY KEY (`id`));"
    result = sqlDb.runcommand(database, sql)
    print(result["Has Succeded"])

get_create_database()

sql = '''INSERT INTO `speed_test` (`id`, `upload`, `download`, `ping`, `share`, `metadata`, `timestamp`) VALUES (NULL, '68721848.12653466', '100714792.85406314', '23.817', 'http://www.speedtest.net/result/13535206714.png', '{"download": 100714792.85406314, "upload": 68721848.12653466, "ping": 23.817, "server": {"url": "http://spmaa.airgenie.co.in:8080/speedtest/upload.php", "lat": "13.0827", "lon": "80.2707", "name": "Chennai", "country": "India", "cc": "IN", "sponsor": "Airgenie", "id": "30878", "host": "spmaa.airgenie.co.in:8080", "d": 21.062655049650402, "latency": 23.817}, "timestamp": "2022-08-13T14:27:14.925712Z", "bytes_sent": 85999616, "bytes_received": 126167322, "share": "http://www.speedtest.net/result/13535206714.png", "client": {"ip": "122.174.229.157", "lat": "12.8996", "lon": "80.2209", "isp": "Airtel Broadband", "isprating": "3.7", "rating": "0", "ispdlavg": "0", "ispulavg": "0", "loggedin": "0", "country": "IN"}}', current_timestamp());'''

result = sqlDb.runcommand(database, sql)
print(result)
