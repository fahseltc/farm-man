from cx_Freeze import setup, Executable


executables = [Executable("main.py")]

build_options = dict(include_files = ['data/'])

setup(name='farm-man',
      version='1.0',
      description='Farming game',
      author='Charlos Behr',
      options= dict(build_exe = build_options),
      executables=executables)
