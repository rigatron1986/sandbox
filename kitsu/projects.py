import gazu

gazu.set_host("http://192.168.1.14/api")

gazu.log_in("admin@example.com", "admin@321")
projects = gazu.project.all_projects()
# print(projects)
for project in projects:
    print(project['name'])

avg_project = (gazu.project.get_project(projects[0]['id']))

task_statuses = avg_project['task_statuses']

