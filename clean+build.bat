rmdir /s /q build
rmdir /s /q dist
python setup.py build
python setup.py bdist_msi