import os
import re

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

with open(path,'r') as file:
    for line in file:
        result = None
        line = line.strip()
        print(f'{line}')

        try:
            num, denom = re.split(r'[|,\s\n]+',line,maxsplit=3)[:2]
            result = float(num) /float(denom)
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            print(f'{num}/{denom} = {result:.2f}')
        finally:
            print('Success ✅\n' if result else 'Error ❌\n')