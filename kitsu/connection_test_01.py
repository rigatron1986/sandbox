import gazu

# gazu.set_host('https://wizz.cg-wire.com/')
# print(gazu.client.host_is_valid())

gazu.set_host("http://192.168.1.14/api")
# gazu.set_event_host("https://kitsu.mystudio.com")
gazu.log_in("admin@example.com", "admin@321")
print(gazu.client.host_is_valid())
project = gazu.project.all_projects()
print(project)
print(len(project))
project = gazu.project.get_project_by_name('avg')
print(project)
