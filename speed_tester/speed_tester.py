import mySql_lib as sqlDb
import speedtest
import json

database = "rigasite"


def get_data():
    sql = "SELECT * FROM `init_pipeline` WHERE 1 ORDER BY id DESC"
    result = sqlDb.runquery(database, sql)
    json_data = []
    # print result
    if result["Has Succeded"]:
        for one in result["message"]:
            data = list(one)
            # print(data)
            json_data.append([data[1] + "-" + str(data[2]), data[3]])
    else:
        raise Exception
    return json_data


def get_create_database():
    sql = "CREATE TABLE IF NOT EXISTS Speed_Test (`id` INT NOT NULL AUTO_INCREMENT , `upload` DOUBLE(20) NOT NULL , " \
          "`download` DOUBLE(20) NOT NULL , `ping` DOUBLE(20) NOT NULL , " \
          "`timestamp` TIMESTAMP NOT NULL , PRIMARY KEY (`id`));"
    result = sqlDb.runcommand(database, sql)
    print(result["Has Succeded"])


def update_database(metadata):
    sql = "INSERT INTO `Speed_Test` " \
          "(`id`, `upload`, `download`, `ping`, `share`, `metadata`, `timestamp`) " \
          "VALUES (NULL, '{upload}', '{download}', '{ping}', '{share}', '{metadata}', " \
          "current_timestamp());".format(**metadata)
    result = sqlDb.runcommand(database, sql)
    return result


def get_speed():
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()
    results_dict['metadata'] = json.dumps(results_dict)
    return results_dict


def speed_test():
    print("Hello world!")
    get_create_database()
    # print(get_data())
    results = get_speed()
    result = update_database(results)
    print(result)


speed_test()
