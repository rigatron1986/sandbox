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
# shot = gazu.shot.get_shot_by_name('seq_01', 'shot_01')
shot = gazu.shot.get_shot('shot_01')
print(shot)
data = {'shot_name': 'shot_01'}
shot_data = {}
for shot in shots:
    shot_name = shot['name']
    if shot_name not in ['shot_01']:
        continue
    cast_datas = gazu.casting.get_shot_casting(shot)
    # print(cast_datas)
    for cast_data in cast_datas:
        print(cast_data)
