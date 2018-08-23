from setuptools import setup

package = 'todo-hook'
version = '0.1'

setup(name=package,
      version=version,
      install_requires=[
          "ansicolor",
          "click"
      ],
      entry_points={
          "console_scripts": [
              "todo-hook=todo_hook.todo_hook:cli"
          ]
      }
)
