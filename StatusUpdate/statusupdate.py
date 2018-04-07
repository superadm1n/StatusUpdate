from time import sleep


def StatusBar(current_run, total_runs, character='=', persistence=False, percentage=False):

    '''
    Generates a Status bar that is 32 characters wide, based on the parameters provided it will either
    have a percentage counter, stay persistent on the console after completion, and have various characters
    for the auctual bar

    :param current_run: number of times the function has already been run
    :param total_runs: Total times this function will be run
    :param character: Character you wish to use for the status bar, can be any string
    :param persistence: Set to true if you wish to not overwrite the status bar after it completes
    :param percentage: Set to True to display a percentage to the right of the status bar
    :return: Prints status bar with completion based on current_run and total_runs parameters
    '''

    character = str(character)

    # This is the algorithm for calculating number of bar characters and space characters required to
    # keep the status bar the proper size regardless of the total number of times run

    key = total_runs / 30
    number_of_bar_characters = int(current_run / (total_runs / 30))
    number_of_spaces = 30 - number_of_bar_characters

    # if the percentage flag is set to True it will print out a percentage of completion after the status bar
    if percentage is True:
        print('[{}]'.format('{}{}'.format(character * number_of_bar_characters, ' ' * number_of_spaces)), end='')
        print(' {}%'.format(int(100 * current_run / total_runs)), end='\r')

    # If the percentage flag is not set to True it will run this code, omitting the percentage calculation
    else:
        print('[{}]'.format('{}{}'.format(character * number_of_bar_characters, ' ' * number_of_spaces)), end='\r')

    # if the persistence flag is set to true it will do one last standard print with a \n character so it wont be overwritten by
    # the prompt
    if persistence is True and current_run == total_runs:
        print('[{}]'.format('{}{}'.format(character * number_of_bar_characters, ' ' * number_of_spaces)))

def StatusBlock(iterations=1, delay=.5, brackets=None, persistence=False, trailingtext='', preceding_text=''):

    '''
    Creates a spinning status block that you often see on Linux software installs "[/]" Based on the parameters
    provided it will loop for longer times, stay persistent, change bracket characters or not have brackets at all.

    :param iterations: Number of circles you wish the block to make
    :param delay: Float: number of seconds you wish to wait until the circle moves
    :param brackets: Beginning and closing character you wish to use if you want to enclose your wheel in brackets
    :param persistence: Bool: Set to True if you wish to not have the block overwritten after running
    :return: Prints spinning status block
    '''

    def print_with_brackets(open_bracket, character, end_bracket):
        print('{} {}{}{} {}'.format(preceding_text, open_bracket, character, end_bracket, trailingtext), end='\r')

    iter_counter = 0
    counter = 1

    while iter_counter != iterations:

        if counter == 1:
            character = '|'
            counter += 1

        elif counter == 2:
            character = '/'
            counter += 1

        elif counter == 3:
            character = '-'
            counter += 1

        else:
            counter = 1
            iter_counter += 1
            character = '\\'

        # This if statement handles printing the status block
        if brackets:
            if len(brackets) == 2:
                open_bracket = brackets[0]
                end_bracket = brackets[1]
                print_with_brackets(open_bracket, character, end_bracket)

            else:
                print('{} {}'.format(preceding_text, character, trailingtext), end='\r')
        else:
            print('{} {}'.format(preceding_text, character, trailingtext), end='\r')

        sleep(delay)

    # if the persistence flag is set the last line of output will be a new line so the block does not get overwritten
    if persistence == True:
        print('')