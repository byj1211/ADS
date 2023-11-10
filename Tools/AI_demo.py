def do_AI_test_FUNC(chan,choice):
    # 0 , 0.5

    print(chan, choice)
    # write value to device1
    # read value from device2
    # value1,value2=1,2
    dic = {'device': str(chan), 'device2': str(choice)}
    return dic