import gitlab
import git
import subprocess

GL = gitlab.Gitlab('http://git01.base-fx.com:88', private_token='Upm3tJJ6HNExJcnAmib2')
GL.auth()

CURRENT_COMPUTER_USER = 'ppardiban'
CURRENT_USER = 'gitlab'
DEFAULT_DAYS = 30
PROJECT_GROUPS_LIST = ['bfx', 'support']
SEARCH_LINK = "/branches?utf8=&search="
project_groups_list = PROJECT_GROUPS_LIST
clone_list = {}
for project_group in project_groups_list:
    project_paths = GL.groups.get(project_group)
    projects_list = project_paths.projects.list(all=True)
    clone_list[project_group] = {}
    for current_project in projects_list:
        project_id = current_project.id
        project = GL.projects.get(project_id)
        project_name = project.name_with_namespace
        project_link = project.web_url
        branch_list = project.branches.list(all=True)
        bash_cmd = "git clone {}".format(project_link)
        clone_list[project_group][project_name] = {}
        clone_list[project_group][project_name]['url'] = project_link
        clone_list[project_group][project_name]['clone'] = bash_cmd
print clone_list
