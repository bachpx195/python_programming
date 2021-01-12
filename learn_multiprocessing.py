from multiprocessing import Pool

# def spawn(num, num2):
#     print('Spawn # {} {}'.format(num, num2))

# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=spawn, args=(i, i+1))
#         p.start()

def job(num):
    return num*2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(20)])
    p.close()
    print(data)
