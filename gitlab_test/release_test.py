import re

result = "origin  git@gitatron.local:support/pipeline_setup.git (fetch) \
origin  git@gitatron.local:support/pipeline_setup.git (push)"
match = re.match(r'.*:(.*)\/(.*).git', result)
if match and len(match.groups()) == 2:
    namespace = match.group(1)
    project_name = match.group(2)
print(namespace)
print(project_name)
