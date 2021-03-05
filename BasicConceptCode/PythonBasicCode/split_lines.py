# 여러줄('\n')로 되어 있는 문자열을 list로 분할하세요
def split_lines(s):
    return s.split('\n')

# examples
split_lines('This\nis a\nmultiline\nstring.\n') 
# ['This','is','a','multiline','string']