import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.emailField',
      version='0.0.4',
      description=('A docassemble extension.'),
      long_description="Creates one email field that will send an attachement with\r\ncustomizations possible, such as email subject line and\r\nemail contents. Includes a 'Send' button on the same line\r\nas the email field. Should remain so for various device widths.\r\n\r\nArrangement remains the same for\r\n\r\n``` yaml\r\n---\r\nfeatures:\r\n  labels above fields: True\r\n---\r\n```\r\n\r\nShould this be optional? Choice of css files?\r\n\r\n## Example\r\n\r\nSee email_labels_above_fields_test.yml and\r\nemail_default_label_position_test.yml for example use.\r\n\r\n## TODO\r\n- Create separate css files for different label placement style choices?\r\n\r\n## Stretch Goals\r\n- Test multiple email fields\r\n",
      long_description_content_type='text/markdown',
      author='knod ding',
      author_email='lsquery@example.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/emailField/', package='docassemble.emailField'),
     )

