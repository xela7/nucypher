import pytest
from web3.contract import Contract


@pytest.fixture()
def escrow(testerchain):
    # Creator deploys the escrow
    escrow, _ = testerchain.interface.deploy_contract('MinersEscrowForPolicyMock', 1)
    return escrow


@pytest.fixture(params=[False, True])
def policy_manager(testerchain, escrow, request):
    creator, client, bad_node, node1, node2, node3, *everyone_else = testerchain.interface.w3.eth.accounts

    # Creator deploys the policy manager
    contract, _ = testerchain.interface.deploy_contract('PolicyManager', escrow.address)

    # Give client some ether
    tx = testerchain.interface.w3.eth.sendTransaction({'from': testerchain.interface.w3.eth.coinbase, 'to': client, 'value': 10000})
    testerchain.wait_for_receipt(tx)

    if request.param:
        dispatcher, _ = testerchain.interface.deploy_contract('Dispatcher', contract.address)

        # Deploy second version of the government contract
        contract = testerchain.interface.w3.eth.contract(
            abi=contract.abi,
            address=dispatcher.address,
            ContractFactoryClass=Contract)

    tx = escrow.functions.setPolicyManager(contract.address).transact({'from': creator})
    testerchain.wait_for_receipt(tx)

    # Register nodes
    tx = escrow.functions.register(node1).transact()
    testerchain.wait_for_receipt(tx)
    tx = escrow.functions.register(node2).transact()
    testerchain.wait_for_receipt(tx)
    tx = escrow.functions.register(node3).transact()
    testerchain.wait_for_receipt(tx)

    return contract
