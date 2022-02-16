#!/usr/bin/python3

import os
from brownie import Token, accounts, Test, network


def main():
    # return Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
    myacc = accounts.add(os.getenv("PRIVATE_KEY"))
    test =  Test.deploy({'from': myacc},publish_source=True)
    # print("test.address --------->", test.address)
    # res = test.getValue()
    # print("res --------->", res)
    # ContractContainer.publish_source(deployed_contract
    if(network.show_active() == 'rinkeby'):
        print("rinkeby")
    return "res"

