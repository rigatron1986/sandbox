import gitlab
import subprocess
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# git_url = 'https://192.168.1.4'
git_url = 'http://192.168.1.171:8080/'
# private_token = '1sySXbesasa76wXU1m8X'
private_token = 'yLs-YyGdwP4kvW2KzBgY'
# private_token = 'T1KkkbCk2p1zCxnxmRvY'
gl = gitlab.Gitlab(git_url, private_token=private_token)
gl.auth()
# projects = gl.projects.list()
# groups = gl.groups.list()
# print dir(groups[0])
# print projects
# print dir(projects[0])
"""
git_data = {}

groups = gl.groups.list()
for each in groups:
    group_id = each.id
    group = gl.groups.get(each.id)
    # print dir(group)
    # print group.attributes
    project_lst = group.projects.list()  # pagination
    for item in project_lst:
        group_name = group.attributes['full_name']

        if group_name not in git_data:
            git_data[group_name] = []
        git_data[group_name].append({'project_name': item.name})
        print group_name
        print item
        print dir(item)
        print "\t", item.get_id()
        print '\t\t', group_id
        print '\t\t', item.attributes['group_id']
        print '\t\t\t', dir(item.attributes)
        # print item.branch
        # print 'project name : ', item.name
    #     project_id = gl.projects.get(item.attributes['id'])
    #     print project_id
print "__________________________________"
print git_data
"""
# git_data = {}
# projects = gl.projects.list()
# for project in projects:
#     group_name, project_name = project.path_with_namespace.split('/')
#     branches = project.branches.list()
#     if group_name not in git_data:
#         git_data[group_name] = {}
#     git_data[group_name][project_name] = {'branches': []}
#     for branch in branches:
#         branch_name = branch.attributes['name']
#         git_data[group_name][project_name]['branches'].append(branch_name)
#     # git_data[group_name].append(project_data)
# print(git_data)
all_data = {}
groups = gl.groups.list()
for group in groups:
    grp_name = group.name
    if grp_name in ['GitLab Instance']:
        continue
    if group not in all_data:
        all_data[group] = {}
    print(group.name)
    # print(dir(group.projects))
    for _project in group.projects.list():
        # print('\t', project)
        prj_name = _project.name
        project = gl.projects.get(_project.id)
        print('\t', _project.id)
        # print('\t', project)
        print('\t', project.branches.list())
        all_branches = project.branches.list()
        if _project not in all_data[group]:
            all_data[group][_project] = []
        all_data[group][_project] = all_branches
        print(_project.ssh_url_to_repo)
        for branch in all_branches:
            # print(dir(branch))
            print(branch.web_url)
        # print(dir(project))
        # if project.name == 'Monitoring':
        #     continue
        # for branch in project.branches.list():
        #     print(branch)
print(all_data)

gg = {u'support': {u'templates': {'branches': [u'master', u'tt_01']}, u'init_pipeline': {'branches': [u'master']}},
      u'nuke': {u'menu': {'branches': [u'master']}}, u'pavith': {u'extend_maya': {'branches': [u'master']}},
      u'pipeline_scripts': {u'core': {'branches': [u'master']}, u'extend_maya': {'branches': []}}}

# print(gg[u'support'])
rr = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__',
      '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
      '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
      '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api_version', '_base_url',
      '_build_url', '_check_redirects', '_get_base_url', '_get_session_opts', '_http_auth', '_merge_auth', '_objects',
      '_prepare_send_data', '_server_revision', '_server_version', '_set_auth_info', '_url', 'api_url', 'api_version',
      'appearance', 'applications', 'audit_events', 'auth', 'broadcastmessages', 'deploykeys', 'deploytokens',
      'dockerfiles', 'enable_debug', 'events', 'features', 'from_config', 'geonodes', 'get_license', 'gitignores',
      'gitlabciymls', 'groups', 'headers', 'hooks', 'http_delete', 'http_get', 'http_list', 'http_password',
      'http_post', 'http_put', 'http_request', 'http_username', 'issues', 'issues_statistics', 'job_token', 'keys',
      'ldapgroups', 'licenses', 'lint', 'markdown', 'merge_config', 'mergerequests', 'namespaces',
      'notificationsettings', 'oauth_token', 'order_by', 'pagesdomains', 'pagination', 'per_page',
      'personal_access_tokens', 'private_token', 'projects', 'retry_transient_errors', 'runners', 'search', 'session',
      'set_license', 'settings', 'sidekiq', 'snippets', 'ssl_verify', 'timeout', 'todos', 'topics', 'url', 'user',
      'user_activities', 'users', 'variables', 'version']
grp = ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
       '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
       '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
       '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_attrs',
       '_create_managers', '_created_from_list', '_get_updated_data', '_id_attr', '_module', '_parent_attrs',
       '_short_print_attr', '_update_attrs', '_updated_attrs', 'access_tokens', 'accessrequests', 'add_ldap_group_link',
       'attributes', 'audit_events', 'auto_devops_enabled', 'avatar_url', 'badges', 'billable_members', 'boards',
       'clusters', 'created_at', 'customattributes', 'default_branch_protection', 'delete', 'delete_ldap_group_link',
       'deploytokens', 'descendant_groups', 'description', 'emails_disabled', 'encoded_id', 'epics', 'exports',
       'full_name', 'full_path', 'get_id', 'hooks', 'id', 'imports', 'issues', 'issues_statistics', 'labels',
       'ldap_sync', 'lfs_enabled', 'manager', 'members', 'members_all', 'mentions_disabled', 'mergerequests',
       'milestones', 'name', 'notificationsettings', 'packages', 'parent_id', 'path', 'pformat', 'pprint',
       'project_creation_level', 'projects', 'request_access_enabled', 'require_two_factor_authentication', 'runners',
       'save', 'search', 'share', 'share_with_group_lock', 'subgroup_creation_level', 'subgroups', 'transfer',
       'transfer_project', 'two_factor_grace_period', 'unshare', 'variables', 'visibility', 'web_url', 'wikis']
dir_grp_prj = ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
               '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
               '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
               '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_compute_path', '_computed_path',
               '_create_attrs', '_from_parent_attrs', '_list_filters', '_obj_cls', '_parent', '_parent_attrs', '_path',
               '_types', '_update_attrs', 'gitlab', 'list', 'parent_attrs', 'path']

dir_prj = ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
           '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
           '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
           '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
           '_attrs', '_create_managers', '_created_from_list', '_id_attr', '_links', '_module', '_parent_attrs',
           '_short_print_attr', '_update_attrs', '_updated_attrs', 'allow_merge_on_skipped_pipeline',
           'analytics_access_level', 'archived', 'attributes', 'auto_cancel_pending_pipelines',
           'auto_devops_deploy_strategy', 'auto_devops_enabled', 'autoclose_referenced_issues', 'avatar_url',
           'build_coverage_regex', 'build_timeout', 'builds_access_level', 'can_create_merge_request_in',
           'ci_config_path', 'ci_default_git_depth', 'ci_forward_deployment_enabled', 'container_expiration_policy',
           'container_registry_enabled', 'created_at', 'creator_id', 'default_branch', 'description', 'emails_disabled',
           'empty_repo', 'encoded_id', 'forking_access_level', 'forks_count', 'get_id', 'group_id', 'http_url_to_repo',
           'id', 'import_status', 'issues_access_level', 'issues_enabled', 'jobs_enabled', 'last_activity_at',
           'lfs_enabled', 'manager', 'merge_method', 'merge_requests_access_level', 'merge_requests_enabled', 'name',
           'name_with_namespace', 'namespace', 'only_allow_merge_if_all_discussions_are_resolved',
           'only_allow_merge_if_pipeline_succeeds', 'open_issues_count', 'operations_access_level', 'packages_enabled',
           'pages_access_level', 'path', 'path_with_namespace', 'pformat', 'pprint',
           'printing_merge_request_link_enabled', 'public_jobs', 'readme_url', 'remove_source_branch_after_merge',
           'repository_access_level', 'repository_storage', 'request_access_enabled',
           'resolve_outdated_diff_discussions', 'restrict_user_defined_variables', 'service_desk_address',
           'service_desk_enabled', 'shared_runners_enabled', 'shared_with_groups', 'snippets_access_level',
           'snippets_enabled', 'ssh_url_to_repo', 'star_count', 'suggestion_commit_message', 'tag_list', 'visibility',
           'web_url', 'wiki_access_level', 'wiki_enabled']

br = ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
      '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
      '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
      '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_attrs', '_create_managers',
      '_created_from_list', '_id_attr', '_module', '_parent_attrs', '_short_print_attr', '_update_attrs',
      '_updated_attrs', 'attributes', 'can_push', 'commit', 'default', 'delete', 'developers_can_merge',
      'developers_can_push', 'encoded_id', 'get_id', 'manager', 'merged', 'name', 'pformat', 'pprint', 'project_id',
      'protected', 'web_url']
