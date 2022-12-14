import gazu

gazu.set_host("http://192.168.1.14/api")
gazu.set_event_host("http://192.168.1.14")

gazu.log_in("admin@example.com", "admin@321")
# print(gazu.client.host_is_valid())
# project = gazu.project.all_projects()
# print(project)
# print(len(project))
project = gazu.project.get_project_by_name('avg')
# print(project)
asset = gazu.asset.get_asset_by_name(project, 'asset_name')
shots = gazu.shot.all_shots_for_project(project)
# print(shots)
data = {'shot_name': 'shot_01'}
shot_data = {}
for shot in shots:
    shot_name = shot['name']
    if shot_name not in ['shot_01']:
        continue
    task_types = gazu.task.all_tasks_for_shot(shot)
    data = {}
    print(shot_name)
    for _task in task_types:
        task_name = _task['task_type_name']
        assigned = _task['assignees']
        if task_name != 'Animation':
            continue
        print('\t ', task_name)
        time_spent = gazu.task.get_time_spent(_task, '2022-08-20')
        print('\t\t ', time_spent)
        for key in time_spent:
            if key == 'total':
                continue
            # print(key)
            artist_name = gazu.person.get_person(key)['full_name']
            print('\t\t\t  ', artist_name)
            datas = time_spent[key]
            for data in datas:
                print('\t\t\t\t ', data)
    # break
# print(shot_data)

"""
pavith 
{'id': '42582e5d-b82b-40ae-b24f-1860afb04e6b', 'created_at': '2022-07-31T05:53:18', 'updated_at': '2022-07-31T05:53:18', 'duration': 60, 'date': '2022-07-31', 'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'}
{'id': 'e9d89c0a-61d3-49da-8f32-ebc5f1cf1874', 'created_at': '2022-08-22T06:39:41', 'updated_at': '2022-08-22T12:09:43', 'duration': 0, 'date': '2022-08-16', 'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'}
{'id': 'fef76342-ad54-4c47-b7f6-9da32e7e0814', 'created_at': '2022-08-22T06:50:02', 'updated_at': '2022-08-22T12:20:03', 'duration': 0, 'date': '2022-08-11', 'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'}
{'id': '4091433d-ee43-4587-aec3-9853b43472bb', 'created_at': '2022-08-26T15:37:23', 'updated_at': '2022-08-26T21:08:01', 'duration': 0, 'date': '2022-08-03', 'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'}
{'id': 'ce995efd-a179-4876-890c-76514a5abc78', 'created_at': '2022-09-01T15:27:58', 'updated_at': '2022-09-01T21:06:04', 'duration': 5, 'date': '2022-08-24', 'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'}

"""
