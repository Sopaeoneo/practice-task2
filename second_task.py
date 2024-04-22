import re
filename = (r"\tovar.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
result = ''
for i in lines:
    if re.match(r"^(.*)(,\s*)(г|кг|мл|л)$", i):
        continue
    else:
        result += i       
result = re.sub(r'\u00AE|\u2122', '', result)
result = re.sub(r'^(.*)(,\s*|\s+)(ГОСТ )(\d*-\d*|\d*.\d*-\d*|\w*\s*\d*-\d*|\d*)(.*)$', r'\1\5, \3\4', result, flags=re.MULTILINE)
result = re.sub(r'^(.*)(массовая доля жира|жирность|жирности|жира)(.*,?\s*)(\b\d{1,2}\s*)(\s*,|.\s*)(\d+\s*)(\s*%)(.*)$', r'\1\2\3\4\5\6\7\8\t\4.\6', result, flags=re.MULTILINE)
result = re.sub(r'^(.*,?\s*)(\b\d+\s*)(\s*,|.\s*)(\d+\s*)(\s*%)(.*)(массовая доля жира|жирность|жирности|жира)(.*)$', r'\1\2\3\4\5\6\7\8\t\2.\4', result, flags=re.MULTILINE)
result = re.sub(r'^(.*)(массовая доля жира|жирность|жирности|жира)(.*,?\s*)(\b(?<![.,])\d+\b)(\s*%)(.*)$', r'\1\2\3\4\5\6\t\4', result, flags=re.MULTILINE)
result = re.sub(r'^(.*,?\s*)(\b(?<![.,])\d+\b)(\s*%)(.*)(массовая доля жира|жирность|жирности|жира)(.*)$', r'\1\2\3\4\5\6\t\2', result, flags=re.MULTILINE)
print(result)