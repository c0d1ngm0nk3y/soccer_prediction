import logging
from analysis.Util import init_logging
from actions.CompareAction import CompareAction

LEAGUE = 'bl1'

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    action = CompareAction()
    nets = action.compare_nets(LEAGUE)
    logger.debug('%d nets found', len(nets))

if __name__ == '__main__':
    init_logging()
    main()
