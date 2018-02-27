# coding:UTF-8
import json

fd = open('result.txt')
lines = fd.readlines()
print(type(lines))
print(len(lines))
print lines[0]
obj = json.loads(lines[0])
print obj['index'], obj['name']
