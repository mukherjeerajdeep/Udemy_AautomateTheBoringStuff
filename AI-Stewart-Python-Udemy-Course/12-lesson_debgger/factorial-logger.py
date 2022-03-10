import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# This means disable all the logging messages which are 'CRITICAL' or lower
# As all the other log levels are lower than the 'CRITICAL' so everything is disabled
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1

    # The range method is wrong, it should start with 1 not zero,
    # by default the range starts from zero
    for i in range(n + 1):
        total = total * i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % total)
    return total


print(factorial(5))

logging.debug('End of program')
