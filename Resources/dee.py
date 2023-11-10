import sys

sys.path.append(u'E:\\app\yanhuaDriver\DAQNavi\Examples\Python')
sys.path.append(u'E:\\app\yanhuaDriver\DAQNavi\Examples\Python\DO_StaticDO')
sys.path.append(u'E:\\app\yanhuaDriver\DAQNavi\Examples\Python\AI_InstantAI')

import staticDO
import InstantAI
if __name__ == '__main__':

    staticDO.AdvInstantDO_1('0x10')

    # staticDO_1.AdvInstantDO(0x30)
    # staticDO_1.AdvInstantDO(0x00)
    #
    # data = InstantAI_1.AdvInstantAI()
    # print(data)
    #
    # data = InstantAI_0.AdvInstantAI()
    # print(data)