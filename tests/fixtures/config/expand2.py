import os

unexpanded_yaml = """
session_name: sampleconfig
start_directory: '~'
windows:
- window_name: focused window
  layout: main-horizontal
  focus: true
  panes:
  - shell_command:
    - cd ~
  - shell_command:
    - cd /usr
    focus: true
  - shell_command:
    - cd ~
    - echo "moo"
    - top
- window_name: window 2
  panes:
  - shell_command:
    - top
    focus: true
  - shell_command:
    - echo "hey"
  - shell_command:
    - echo "moo"
- window_name: window 3
  panes:
  - shell_command: cd /
    focus: true
  - pane
  - pane
"""

expanded_yaml = """
session_name: sampleconfig
start_directory: {HOME}
windows:
- window_name: focused window
  layout: main-horizontal
  focus: true
  panes:
  - shell_command:
    - cd ~
  - shell_command:
    - cd /usr
    focus: true
  - shell_command:
    - cd ~
    - echo "moo"
    - top
- window_name: window 2
  panes:
  - shell_command:
    - top
    focus: true
  - shell_command:
    - echo "hey"
  - shell_command:
    - echo "moo"
- window_name: window 3
  panes:
  - shell_command:
    - cd /
    focus: true
  - shell_command: []
  - shell_command: []
""".format(
    HOME=os.path.expanduser('~')
)
