class DividerIsNull(Exception):
    def __init__(self, text):
        self.text = text

def div(a, b):
   try:
        if b == 0:
            raise DividerIsNull('Error')
        print(a // b)
   except DividerIsNull:
       print('b - не может быть 0')

div(int(input()), int(input()))