from StatusUpdate import statusupdate
import unittest


class StatusUpdateTest(unittest.TestCase):

    def test_CalculateBar(self):

        '''
        This test will validate that the _calculatebar function
        returns the proper analysis for an entire run of the status bar
        '''

        resultA = 0
        resultB = 30

        for x in range(10):

            self.assertEqual(statusupdate._CalculateBar(x, 10), (resultA, resultB))

            resultA += 3
            resultB -= 3

    def test_determineCharacter(self):

        '''
        Tests the determineCharacter method through a single iteration
        '''

        expectedResult = (2, 1, '|')
        self.assertEqual(statusupdate._determineCharacter(1, 1), expectedResult)

        expectedResult = (3, 1, '/')
        self.assertEqual(statusupdate._determineCharacter(2, 1), expectedResult)

        expectedResult = (4, 1, '-')
        self.assertEqual(statusupdate._determineCharacter(3, 1), expectedResult)

        expectedResult = (1, 2, '\\')
        self.assertEqual(statusupdate._determineCharacter(4, 1), expectedResult)






from time import sleep

if __name__ == '__main__':

    unittest.main()
    '''

    print('Status block, 2 iterations, square brackets, and persistence set, with trailing text')
    StatusUpdate.StatusBlock(iterations=2, brackets='[]', persistence=True, trailingtext='Process is running')

    print('Status block, 2 iterations, square brackets, and persistence set, with trailing text, and preceeding text')
    StatusUpdate.StatusBlock(iterations=2, brackets='[]', persistence=True, preceding_text='Checking for process')


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
        StatusUpdate.StatusBar(n, 90, persistence=True, percentage=False)
        sleep(.1)
    '''