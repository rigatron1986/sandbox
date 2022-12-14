import sys

sys.path.append(r"C:\Users\user\Downloads\TACTIC-4.8.0.b01\src\client")

from tactic_client_lib import TacticServerStub
import json


class UserData(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    def __repr__(self):
        s = self.__class__.__name__ + "("
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                s += "{}={}, ".format(k, v)
        s = s.rstrip(", ") + ")"
        return s


def dict2obj(d):
    return json.loads(json.dumps(d), object_hook=UserData)


site = "avn"

server = TacticServerStub.get(protocol='xmlrpc', setup=False)
server.set_server('192.168.1.14')
server.set_project('avn')
server.set_site(site)
ticket = server.get_ticket(login='admin', password='admin@321')  # , site=site)
server.set_ticket(ticket)

# expr = "@SOBJECT(sthpw/login['login','rohit'])"
# expr = "@GET(sthpw/login['login','pavith'].email)"
# expr = "@SOBJECT(config/prod_setting['key', 'project coordinator'])"
# expr = "@GET(config/prod_setting['key', 'project coordinator'].value)"
# expr = "@GET(sthpw/login['login', @GET(config/prod_setting['key', 'project coordinator'].value)].email)"
# expr = "@SOBJECT(sthpw/task['search_code', @GET(.code)])"
expr = "@GET(sthpw/task['search_code', 'shot_01']['process', 'roto'].status)"
# expr = "@SOBJECT(vfx/shot['code', 'shot_01'])"
print(server.eval(expr))

# datas = server.eval(expr)
# obj_data = []
# for data in datas:
#     print(data['key'])
#     obj_data.append(dict2obj(data))
# print(obj_data)
