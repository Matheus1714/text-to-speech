# Read text file
text = ''
with open('text.txt', 'rb') as f:
    text = f.read().decode('utf-8')
    text = text.replace('\r','')
    text = text.replace('\t','')

print(text)