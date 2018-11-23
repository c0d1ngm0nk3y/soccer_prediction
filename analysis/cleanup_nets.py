import logging
import os
from analysis.Util import init_logging
from actions.CompareAction import CompareAction

LEAGUE = 'bl1'
DELTA = 3

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    action = CompareAction()
    nets = action.compare_nets(LEAGUE)
    logger.debug('%d nets found', len(nets))
    max_points = nets[0].points
    for ii in range(len(nets)):
        net = nets[ii]
        points = net.points
        if points + DELTA < max_points:
            logger.info('Removing %s', net.path)
            os.remove(net.path)

if __name__ == '__main__':
    init_logging()
    main()
