result = []
def divider(a,b):
 # Якщо ми будемо ставити > або < то відповідно буде помилка (value чи index, і буде жалітись res)
 if a == b:
  raise Exception(ValueError)
 if b > 100:
  raise Exception(IndexError)
 return a/b
data = {10: 2, 2: 5, 123: 4, 18: 1, 0: 15, 8: 4}
for key in data:
 res = divider(key, data[key])
 result.append(res)

print(result)
print('a != b')