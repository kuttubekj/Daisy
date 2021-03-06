from brownie import accounts, web3, Wei, reverts
from brownie.network.transaction import TransactionReceipt
from brownie.convert import to_address
import pytest
from brownie import Contract
from settings import *


# reset the chain after every test case
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


def test_init_mkr_chief(mkr_chief):
    # not the hat yet
    assert mkr_chief.isUserRoot(accounts[0], {'from': accounts[0]}) == False

# def test_init_iou_token(iou_token):
#     assert iou_token.symbol() == IOU_NAME
