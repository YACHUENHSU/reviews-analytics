data = []
count = 0
with open('reviews-analytics/reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 ==0: # %用來求餘數
			print(len(data))
print('檔案讀取完，共有', (len(data)),'筆資料')

print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)
print('每則留言平均是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言裡出現good字眼')

#文字計數
wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你要查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為:',wc[word])
	else:
		print('裡面沒有這個字唷！')

print(word,'謝謝你的查詢')




