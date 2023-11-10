from Interfaces import JDK23
for chan in [15,16]:
    for choice in JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"]:
        index = JDK23.AITest.CHES['{:02X}'.format(chan)]["tpvs"].index(str(choice))
        v_pp = JDK23.AITest.CHES['{:02X}'.format(chan)]['v_pp'][index]
        print(index,choice,v_pp)
