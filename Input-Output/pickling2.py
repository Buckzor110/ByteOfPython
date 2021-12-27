import pickle
a = 'example.data'
message = "Бля братан ты думал здесь че-то будет?"

f = open(a, "wb")
pickle.dump(message, f)
f.close()

del message

f = open(a, "rb")
b = pickle.load(f)
print(b)
