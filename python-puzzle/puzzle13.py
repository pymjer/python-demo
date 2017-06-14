if __name__ == '__main__':

    f = open('evil2.gfx', 'rb')

    data = f.read()

    for i in range(5):
        file = open('evil_%d.jpg' % i, 'wb')
        file.write(data[i::5])
        file.close()

    f.close()
