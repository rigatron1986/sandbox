import sys

sys.path.append(r"C:\Users\user\Downloads\TACTIC-4.8.0.b01\src\client")

from tactic_client_lib import TacticServerStub


site = "avn"

server = TacticServerStub.get(protocol='xmlrpc', setup=False)
server.set_server('192.168.1.19')
server.set_project('avn')
server.set_site(site)
ticket = server.get_ticket(login='admin', password='admin@321')  # , site=site)
server.set_ticket(ticket)


def get_data(project):
    # server = TacticServerStub()
    # expr = "@SOBJECT(sthpw/task['project_code', '{}']['process', 'ani'])".format(project)
    expr = "@GET(sthpw/task['project_code', '{}']['process', 'ani'].status)".format(project)
    # expr = "@SOBJECT(sthpw/login['login','rohit'])".format(project)
    print(expr)
    return server.eval(expr)


print(get_data("avn"))
print(len(get_data('avn')))
t = {'status': None, 'code': 'TASK00000001', 'milestone_code': None, 'description': None, 'bid_quantity': None,
     'process': 'animation', 'timestamp': '2021-08-22 14:38:54.554121', 's_status': None, 'assigned': 'pavith',
     'pipeline_code': 'task', 'bid_end_date': None, 'actual_quantity': None,
     '__search_key__': 'sthpw/task?code=TASK00000001', 'supervisor': 'admin', 'assigned_group': None,
     'search_code': 'shot_01', 'data': None, 'id': 1, '__search_type__': 'sthpw/task', 'completion': None,
     'search_type': 'vfx/shot?project=avg', 'actual_start_date': None, 'parent_task_code': None, 'discussion': None,
     'depend_id': None, 'actual_end_date': None, 'actual_duration': None, 'project_code': 'avg', 'bid_duration': None,
     'parent_id': None, 'sort_order': None, 'bid_start_date': None, 'context': 'animation', 'task_type': None,
     'login': None, 'search_id': 2, 'priority': 3}

shot_data = {'tc_frame_end': 1010, '__search_type__': 'vfx/shot?project=avg', 's_status': None, 'code': 'shot_01',
             'images': None, 'id': 2, 'priority': None, '__search_key__': 'vfx/shot?project=avg&code=shot_01',
             'type': None, 'status': 'online', 'tc_frame_start': 1001, 'description': None,
             'timestamp': '2021-08-22 09:22:29.544489', 'frame_note': None, 'frame_in': None, 'sort_order': None,
             'frame_out': None, 'short_code': None, 'complexity': 3, 'pipeline_code': 'avg/shot',
             'sequence_code': 'seq_001', 'parent_code': None, 'scan_status': None}

user = [{'code': 'admin', '__search_type__': 'sthpw/login', 's_status': None, 'last_name': '', 'keywords': None,
         'project_code': None, 'first_name': 'Admin', 'display_name': ', Admin', 'login_groups': None,
         'namespace': None, 'id': 1, 'hourly_wage': None, '__search_key__': 'sthpw/login?code=admin',
         'department': None, 'login_attempt': None, 'email': None, 'location': None, 'phone_number': None,
         'keywords_data': None, 'password': '$S$DWMSRGJXJRxhE8gWK6kYHx2JI4dMaPRn0kvVKMNEtRA5mpa32yC5', 'data': None,
         'upn': 'admin', 'snapshot': None, 'license_type': None, 'login': 'admin'},
        {'code': 'test', '__search_type__': 'sthpw/login', 's_status': None, 'last_name': None, 'keywords': None,
         'project_code': None, 'first_name': None, 'display_name': 'test', 'login_groups': None, 'namespace': None,
         'id': 9, 'hourly_wage': None, '__search_key__': 'sthpw/login?code=test', 'department': None,
         'login_attempt': None, 'email': None, 'location': None, 'phone_number': None, 'keywords_data': None,
         'password': '$S$DPTPPFUNEwNI6VLDUigytHZiZmQKjyZdv6l.QIYxTmrHKdANKhRw', 'data': None, 'upn': 'test',
         'snapshot': None, 'license_type': None, 'login': 'test'}]

all_ani = [
    {
        'status': 'Waiting', 'code': 'TASK00000017', 'milestone_code': None, 'description': None, 'bid_quantity': None,
        'process': 'ani', 'timestamp': '2021-10-13 00:15:26.708240', 's_status': None, 'assigned': None,
        'pipeline_code': 'task', 'bid_end_date': None, 'actual_quantity': None,
        '__search_key__': 'sthpw/task?code=TASK00000017', 'supervisor': None, 'assigned_group': None,
        'search_code': 'shot_02', 'data': None, 'id': 17, '__search_type__': 'sthpw/task', 'completion': None,
        'search_type': 'vfx/shot?project=avg', 'actual_start_date': None, 'parent_task_code': None, 'discussion': None,
        'depend_id': None, 'actual_end_date': None, 'actual_duration': None, 'project_code': 'avg',
        'bid_duration': None,
        'parent_id': None, 'sort_order': None, 'bid_start_date': None, 'context': 'ani/001', 'task_type': None,
        'login': None, 'search_id': 5, 'priority': None
    },
    {
        'status': 'approved', 'code': 'TASK00000010', 'milestone_code': None, 'description': None, 'bid_quantity': None,
        'process': 'ani', 'timestamp': '2021-08-29 10:30:33.158599', 's_status': None, 'assigned': None,
        'pipeline_code': 'PIPELINE00003', 'bid_end_date': '2021-09-24 12:00:00', 'actual_quantity': None,
        '__search_key__': 'sthpw/task?code=TASK00000010', 'supervisor': None, 'assigned_group': None,
        'search_code': 'shot_02', 'data': None, 'id': 10, '__search_type__': 'sthpw/task', 'completion': None,
        'search_type': 'vfx/shot?project=avg', 'actual_start_date': None, 'parent_task_code': None, 'discussion': None,
        'depend_id': 9, 'actual_end_date': '2021-08-29 10:35:15.265180', 'actual_duration': None, 'project_code': 'avg',
        'bid_duration': 8.0, 'parent_id': None, 'sort_order': None, 'bid_start_date': '2021-09-21 12:00:00',
        'context': 'ani', 'task_type': None, 'login': None, 'search_id': 5, 'priority': None
    }
]
