def replace(symbol):
    return chr((ord(symbol) - 97 + 1) % 26 + 97)


def last_survivors(string):
    res = [*string]
    while True:
        len_0 = len_ = len(res)
        i = 0
        while i < len_ - 1:
            j = i + 1
            while j < len_:
                if res[i] == res[j]:
                    symbol = res.pop(j)
                    res[i] = replace(symbol)
                    len_ -= 1
                else:
                    j += 1
            i += 1
        if len_0 == len_:
            return ''.join(res)



if __name__ == '__main__':
    print(
        last_survivors('xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh'))