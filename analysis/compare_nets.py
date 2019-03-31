import logging
from analysis.Util import init_logging
from actions.CompareAction import CompareAction

LEAGUE = 'bl1'
TYPE = "default"


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    action = CompareAction()
    nets = action.compare_nets(LEAGUE, TYPE)
    logger.debug('%d nets found', len(nets))
    for ii in range(len(nets)):
        logger.info('%d. %s', ii+1, str(nets[ii]))

if __name__ == '__main__':
    init_logging()
    main()
