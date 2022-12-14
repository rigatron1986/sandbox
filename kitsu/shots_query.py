import gazu

gazu.set_host("http://192.168.1.15/api")

gazu.log_in("admin@example.com", "admin@321")
# print(gazu.client.host_is_valid())
# project = gazu.project.all_projects()
# print(project)
# print(len(project))
project = gazu.project.get_project_by_name('avg')
# print(project)
shots = gazu.shot.all_shots_for_project(project)
# print(shots)
data = {'shot_name': 'shot_01'}
shot_data = {}
for shot in shots:
    print(gazu.shot.get_asset_instances_for_shot(shot))
    task_types = gazu.task.all_tasks_for_shot(shot)
    # print(shot['name'])
    shot_name = shot['name']
    data = {}
    for _task in task_types:
        time_spent = gazu.task.get_time_spent(_task, '2022-08-05')
        # print(time_spent)
        task_name = _task['task_type_name']
        assigned = _task['assignees']
        # print(task_name)
        data[task_name] = {}
        for ass in assigned:
            artist_name = gazu.person.get_person(ass)['full_name']
            data[task_name][artist_name] = 0
    shot_data[shot_name] = data
    # break
print(shot_data)

data = {
    'Animation': {
        'selva': 5,
        'pavith': 8
    },
}
#     shot = {'description': 'this is a test'}
#     if shot['name'] == 'shot_01':
#         shot['description'] = "Updated using python"
#         _shot = gazu.shot.update_shot(shot)
#     asset_types = gazu.shot.all_asset_instances_for_shot(shot)
#     print(asset_types)
#     break
# all_persons = gazu.person.all_persons()
# for people in all_persons:
#     if people['first_name'] == 'pavith':
#         print(people)
# gazu.task.set_time_spent('1e4057b1-03bf-4f5e-a311-1803f9681aae',
#                          '202a28ca-fde1-4d35-8b59-ecab906825ec', '2022-08-24', 5)
# print(gazu.task.get_task_type_by_name("Animation"))
print(gazu.person.get_person('202a28ca-fde1-4d35-8b59-ecab906825ec'))
tas = {'assignees': ['2ef67bd8-3157-4577-afba-1671ae96ed17', '202a28ca-fde1-4d35-8b59-ecab906825ec'],
       'id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'created_at': '2022-07-30T16:49:04',
       'updated_at': '2022-09-01T21:06:04', 'name': 'main', 'description': None, 'priority': 0, 'duration': 65,
       'estimation': 0, 'completion_rate': 0, 'retake_count': 1, 'sort_order': 0, 'start_date': '2022-08-01T00:00:00',
       'due_date': '2022-08-05T00:00:00', 'real_start_date': '2022-09-01T12:01:22', 'end_date': None,
       'last_comment_date': '2022-09-01T06:31:22', 'nb_assets_ready': 2, 'data': None, 'shotgun_id': None,
       'project_id': '5abfcda3-1be1-48ce-a358-782dd680a670', 'task_type_id': '1e4057b1-03bf-4f5e-a311-1803f9681aae',
       'task_status_id': 'a3bf8bfa-d34e-4e3e-8694-8f3c0ee1ca1b', 'entity_id': 'a4d0287d-f440-4fa8-832b-a0bba2b2f698',
       'assigner_id': '4de2aa6f-f926-4f36-a88b-ef6f9d0c2a51', 'type': 'Task', 'project_name': 'avg',
       'task_type_name': 'Animation', 'task_status_name': 'Work In Progress', 'entity_type_name': 'Shot',
       'entity_name': 'shot_01'}

ts = {
    'total': 65, '202a28ca-fde1-4d35-8b59-ecab906825ec': [
        {
            'id': '42582e5d-b82b-40ae-b24f-1860afb04e6b', 'created_at': '2022-07-31T05:53:18',
            'updated_at': '2022-07-31T05:53:18', 'duration': 60, 'date': '2022-07-31',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec',
            'type': 'TimeSpent'},
        {
            'id': 'e9d89c0a-61d3-49da-8f32-ebc5f1cf1874', 'created_at': '2022-08-22T06:39:41',
            'updated_at': '2022-08-22T12:09:43', 'duration': 0, 'date': '2022-08-16',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e',
            'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'},
        {
            'id': 'fef76342-ad54-4c47-b7f6-9da32e7e0814', 'created_at': '2022-08-22T06:50:02',
            'updated_at': '2022-08-22T12:20:03', 'duration': 0, 'date': '2022-08-11',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec',
            'type': 'TimeSpent'},
        {
            'id': '4091433d-ee43-4587-aec3-9853b43472bb', 'created_at': '2022-08-26T15:37:23',
            'updated_at': '2022-08-26T21:08:01', 'duration': 0, 'date': '2022-08-03',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e',
            'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec', 'type': 'TimeSpent'},
        {
            'id': 'ce995efd-a179-4876-890c-76514a5abc78', 'created_at': '2022-09-01T15:27:58',
            'updated_at': '2022-09-01T21:06:04', 'duration': 5, 'date': '2022-08-24',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec',
            'type': 'TimeSpent'
        }
    ],
    '2ef67bd8-3157-4577-afba-1671ae96ed17': [
        {
            'id': '88a0c257-e904-4a60-b8cb-ec76894bd923', 'created_at': '2022-08-26T14:55:47',
            'updated_at': '2022-08-26T20:25:48', 'duration': 0, 'date': '2022-08-18',
            'task_id': '18fb37d7-7adc-46cb-8e25-b29232c46b3e', 'person_id': '2ef67bd8-3157-4577-afba-1671ae96ed17',
            'type': 'TimeSpent'
        }
    ]
}

ts_2 = {
    'total': 965, '2ef67bd8-3157-4577-afba-1671ae96ed17': [
        {
            'id': '2a9e1fd4-7e70-4938-84a7-b452d4b0bddd', 'created_at': '2022-07-31T05:53:38',
            'updated_at': '2022-07-31T11:23:40', 'duration': 240, 'date': '2022-07-31',
            'task_id': 'dca8482b-2218-4a75-9b92-9d861c7074e9', 'person_id': '2ef67bd8-3157-4577-afba-1671ae96ed17',
            'type': 'TimeSpent'
        },
        {
            'id': '43b36cd8-d9e7-4997-89fd-92463938b0ef', 'created_at': '2022-07-31T05:53:52',
            'updated_at': '2022-07-31T05:53:52', 'duration': 480, 'date': '2022-07-29',
            'task_id': 'dca8482b-2218-4a75-9b92-9d861c7074e9',
            'person_id': '2ef67bd8-3157-4577-afba-1671ae96ed17', 'type': 'TimeSpent'},
        {
            'id': '4e7ccdbb-7a10-411b-8307-8556796c52f2', 'created_at': '2022-08-26T14:52:07',
            'updated_at': '2022-08-26T14:52:07', 'duration': 240, 'date': '2022-08-09',
            'task_id': 'dca8482b-2218-4a75-9b92-9d861c7074e9', 'person_id': '2ef67bd8-3157-4577-afba-1671ae96ed17',
            'type': 'TimeSpent'
        }
    ],
    '202a28ca-fde1-4d35-8b59-ecab906825ec': [
        {
            'id': 'af371a43-d3b3-4465-b9fa-2c26b3c711e5', 'created_at': '2022-09-01T15:27:59',
            'updated_at': '2022-09-01T21:06:04', 'duration': 5, 'date': '2022-08-24',
            'task_id': 'dca8482b-2218-4a75-9b92-9d861c7074e9', 'person_id': '202a28ca-fde1-4d35-8b59-ecab906825ec',
            'type': 'TimeSpent'}]}
