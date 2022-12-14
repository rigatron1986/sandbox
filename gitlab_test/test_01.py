import gitlab
import subprocess

# private_token = 'j-ZmH55UmNwTfA2esxQQ'
private_token = 'Q_m9tNwHcYJkDgzsCTjF'
gl = gitlab.Gitlab('http://192.168.1.11', private_token=private_token, ssl_verify=False)
gl.auth()
projects = gl.projects.list()
# for project in projects:
#     # print(project)
#     print project.name
maya_repo = [x for x in projects if x.name == 'core'][0]
print(maya_repo)
# branch = maya_repo.branches.create({'branch': 'test_branch',
#                                     'ref': 'master'})
print(maya_repo.attributes)  # displays all the attributes
git_url = maya_repo.ssh_url_to_repo
new_url = git_url.replace('.local', '.local:8080')
web_url = maya_repo.http_url_to_repo
print(git_url)
# tet = maya_repo.http_url_to_repo
# new_url1 = tet.replace('.local', '.local:8080')
subprocess.call(['git', 'clone', git_url + ' D:/test'])
t = {u'lfs_enabled': True, u'forks_count': 0, u'autoclose_referenced_issues': True, u'container_registry_enabled': True,
     u'shared_runners_enabled': True, u'wiki_enabled': True, u'builds_access_level': u'enabled', u'archived': False,
     u'build_timeout': 3600, u'star_count': 0, u'pages_access_level': u'private', u'service_desk_enabled': False,
     u'resolve_outdated_diff_discussions': False,
     u'_links': {u'repo_branches': u'http://raspberrypi.local/api/v4/projects/36/repository/branches',
                 u'merge_requests': u'http://raspberrypi.local/api/v4/projects/36/merge_requests',
                 u'self': u'http://raspberrypi.local/api/v4/projects/36',
                 u'labels': u'http://raspberrypi.local/api/v4/projects/36/labels',
                 u'members': u'http://raspberrypi.local/api/v4/projects/36/members',
                 u'events': u'http://raspberrypi.local/api/v4/projects/36/events',
                 u'issues': u'http://raspberrypi.local/api/v4/projects/36/issues'},
     u'snippets_access_level': u'enabled', u'repository_access_level': u'enabled', u'visibility': u'internal',
     u'restrict_user_defined_variables': False, u'ssh_url_to_repo': u'git@raspberrypi.local:main/extend_maya.git',
     u'build_coverage_regex': None, u'remove_source_branch_after_merge': True, u'emails_disabled': None,
     u'only_allow_merge_if_all_discussions_are_resolved': False, u'import_status': u'none',
     u'permissions': {u'group_access': {u'notification_level': 3, u'access_level': 50}, u'project_access': None},
     u'empty_repo': False, u'open_issues_count': 0, u'name': u'extend_maya', u'auto_devops_enabled': True,
     u'container_expiration_policy': {u'name_regex_keep': None, u'enabled': False, u'keep_n': 10, u'cadence': u'1d',
                                      u'next_run_at': u'2021-06-15T23:30:14.416Z', u'name_regex': u'.*',
                                      u'older_than': u'90d'}, u'allow_merge_on_skipped_pipeline': None,
     u'issues_access_level': u'enabled', u'auto_devops_deploy_strategy': u'continuous', u'request_access_enabled': True,
     u'operations_access_level': u'enabled', u'can_create_merge_request_in': True, u'service_desk_address': None,
     u'ci_forward_deployment_enabled': True, u'http_url_to_repo': u'http://raspberrypi.local/main/extend_maya.git',
     u'web_url': u'http://raspberrypi.local/main/extend_maya', u'id': 36, u'merge_requests_access_level': u'enabled',
     u'merge_requests_enabled': True, u'snippets_enabled': True, u'packages_enabled': True, u'merge_method': u'merge',
     u'namespace': {u'kind': u'group', u'web_url': u'http://raspberrypi.local/groups/main', u'name': u'main',
                    u'parent_id': None, u'avatar_url': None, u'path': u'main', u'id': 37, u'full_path': u'main'},
     u'ci_default_git_depth': 50, u'issues_enabled': True, u'path_with_namespace': u'main/extend_maya',
     u'repository_storage': u'default', u'ci_config_path': None, u'shared_with_groups': [], u'description': u'',
     u'default_branch': u'master', u'forking_access_level': u'enabled',
     u'readme_url': u'http://raspberrypi.local/main/extend_maya/-/blob/master/README.md', u'public_jobs': True,
     u'path': u'extend_maya', u'only_allow_merge_if_pipeline_succeeds': False, u'tag_list': [],
     u'last_activity_at': u'2021-07-31T23:39:20.228Z', u'suggestion_commit_message': None,
     u'printing_merge_request_link_enabled': True, u'name_with_namespace': u'main / extend_maya',
     u'created_at': u'2021-06-14T23:30:14.117Z', u'wiki_access_level': u'enabled',
     u'analytics_access_level': u'enabled', u'creator_id': 36, u'avatar_url': None,
     u'auto_cancel_pending_pipelines': u'enabled', u'jobs_enabled': True}
