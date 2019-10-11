# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values


def main():
    a = bytes([0x41, 0x42, 0x43, 0x44])
    print(a)

    b = 'This a string'
    print(b)

    # decode bytes into str to concatenate with string
    c = a.decode('utf-8')
    print(b + c)

    # encode str into bytes
    d = b.encode('utf-8')
    print(d + a)


if __name__ == "__main__":
    #main()

    msg = bytes([0x42])
    print(msg.decode('utf-8'))
