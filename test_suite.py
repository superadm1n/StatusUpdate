import StatusUpdate
from time import sleep

if __name__ == '__main__':


    print('Status block, 2 iterations, square brackets, and persistence set')
    StatusUpdate.StatusBlock(iterations=2, brackets='[]', persistence=True)

    print('Test Bar without Percent, 5 Iterations')
    for n in range(1, 6):
        StatusUpdate.StatusBar(n, 5, character='|', persistence=True)
        sleep(1)

    print('Test Bar with Percent, 5 Iterations')
    for n in range(1, 6):
        StatusUpdate.StatusBar(n, 5, persistence=True, percentage=True)
        sleep(1)


    print('Test Bar with Percent, 40 Total Iterations')
    for n in range(1, 41):
        StatusUpdate.StatusBar(n, 40, persistence=True, percentage=True)
        sleep(.2)

    print('Test Bar without Percent, 90 Iterations')
    for n in range(1, 91):
        StatusUpdate.StatusBar(n, 90, persistence=True, percentage=True)
        sleep(.1)
