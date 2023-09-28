"""

    03_ctxmgr02.py
    Context Manager life cycle.

"""
class MyContextManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        print(self.filepath)
        print('in enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('in exit')


with MyContextManager('filepath') as obj:
    # print(obj.filepath)
    print(obj)

x = MyContextManager('some string')
print(x.filepath)
