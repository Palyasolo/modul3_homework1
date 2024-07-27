calls = 0
def count_call():
    global calls
    calls += 1

def string(a):
    b = (len(a),str.lower(a),str.upper(a))
    print (b)
    count_call()

def s_contains(a, b):
    str(a)
    list(b)
    c = True
    for i in b:
        if i == a:
            c = True
            break
        else: c = False
    print(c)
    count_call()

string('sdf')
s_contains('sDf', ('sDf', 'fds'))
print (calls)


