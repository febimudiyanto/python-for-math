'''
sebuah segitiga setiap sisinya saling bergantung, persamaan yang umum kita tahu adalah a^2 + b^2 = c^2
namun itu hanya untuk segitiga siku-siku. persamaan umum untuk suatu segitiga adalah c^2 = a^2 + b^2 - 2.a.b.cos <C

'''


def isTriangle(a,b,c):
    '''
    a,b,c = nilai integer yang menyatakan panjang sisi a,b,c
    
    return True jika a,b,c segitiga yang valid
    /return False jika a,b,c tidak membentuk segitiga.
    '''
    if (a+b <= c) or (b+c <= a) or (c+a <= b):
        return False
    return True
