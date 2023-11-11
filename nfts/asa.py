from typing import Any, Dict
from algosdk import transaction

from accounts.utils import get_algod_client
from accounts.models import Account
from nfts.models import NFT

# Setup
algod_client = get_algod_client()


# example: asset_create
# Account 1 creates an asset called `rug` with a total supply
# of 1000 units and sets itself to the freeze/clawback/manager/reserve roles
def asset_create(nft: NFT, url: str) -> int:
    sp = algod_client.suggested_params()
    txn = transaction.AssetConfigTxn(
        sender=nft.creator.account.address,
        sp=sp,
        default_frozen=False,
        unit_name=nft.unit,
        asset_name=nft.name,
        manager=nft.manager,
        reserve=nft.reserve,
        freeze=nft.freeze,
        clawback=nft.clawback,
        url=url,
        total=nft.total,
        decimals=nft.decimals,
        strict_empty_address_check=False,
    )

    # Sign with secret key of creator
    stxn = txn.sign(nft.creator.account.private_key)

    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print(f"Sent asset create transaction with txid: {txid}")

    # Wait for the transaction to be confirmed
    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

    # grab the asset id for the asset we just created
    created_asset = results["asset-index"]
    return created_asset


def asset_config(acct: Account):
    sp = algod_client.suggested_params()
    # Create a config transaction that wipes the
    # reserve address for the asset
    txn = transaction.AssetConfigTxn(
        sender=acct.address,
        sp=sp,
        manager=acct.address,
        reserve=None,
        freeze=acct.address,
        clawback=acct.address,
        strict_empty_address_check=False,
    )
    # Sign with secret key of manager
    stxn = txn.sign(acct.private_key)
    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print(f"Sent asset config transaction with txid: {txid}")
    # Wait for the transaction to be confirmed
    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_info(created_asset: int) -> Any:
    # Retrieve the asset info of the newly created asset
    asset_info = algod_client.asset_info(created_asset)
    asset_params: Dict[str, Any] = asset_info["params"]
    print(f"Asset Name: {asset_params['name']}")
    print(f"Asset params: {list(asset_params.keys())}")
    # example: ASSET_INFO
    return asset_info


def asset_optin(acct: Account, created_asset: int):
    sp = algod_client.suggested_params()
    # Create opt-in transaction
    # asset transfer from me to me for asset id we want to opt-in to with amt==0
    optin_txn = transaction.AssetOptInTxn(
        sender=acct.address, sp=sp, index=created_asset
    )
    signed_optin_txn = optin_txn.sign(acct.private_key)
    txid = algod_client.send_transaction(signed_optin_txn)
    print(f"Sent opt in transaction with txid: {txid}")

    # Wait for the transaction to be confirmed
    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_transfer(acct: Account, receiver: Account, created_asset: int):
    sp = algod_client.suggested_params()
    # Create transfer transaction
    xfer_txn = transaction.AssetTransferTxn(
        sender=acct.address,
        sp=sp,
        receiver=receiver.address,
        amt=1,
        index=created_asset,
    )
    signed_xfer_txn = xfer_txn.sign(acct.private_key)
    txid = algod_client.send_transaction(signed_xfer_txn)
    print(f"Sent transfer transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_freeze(acct: Account, receiver: Account, created_asset: int):
    sp = algod_client.suggested_params()
    # Create freeze transaction to freeze the asset in acct2 balance
    freeze_txn = transaction.AssetFreezeTxn(
        sender=acct.address,
        sp=sp,
        index=created_asset,
        target=receiver.address,
        new_freeze_state=True,
    )
    signed_freeze_txn = freeze_txn.sign(acct.private_key)
    txid = algod_client.send_transaction(signed_freeze_txn)
    print(f"Sent freeze transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_clawback(acct: Account, receiver: Account, created_asset: int):
    sp = algod_client.suggested_params()
    # Create clawback transaction to freeze the asset in acct2 balance
    clawback_txn = transaction.AssetTransferTxn(
        sender=acct.address,
        sp=sp,
        receiver=acct.address,
        amt=1,
        index=created_asset,
        revocation_target=receiver.address,
    )
    signed_clawback_txn = clawback_txn.sign(acct.private_key)
    txid = algod_client.send_transaction(signed_clawback_txn)
    print(f"Sent clawback transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_opt_out(acct: Account, receiver: Account, created_asset: int):
    sp = algod_client.suggested_params()
    opt_out_txn = transaction.AssetTransferTxn(
        sender=receiver.address,
        sp=sp,
        index=created_asset,
        receiver=acct.address,
        # an opt out transaction sets its close_asset_to parameter
        # it is always possible to close an asset to the creator
        close_assets_to=acct.address,
        amt=0,
    )
    signed_opt_out = opt_out_txn.sign(receiver.private_key)
    txid = algod_client.send_transaction(signed_opt_out)
    print(f"Sent opt out transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")


def asset_delete(acct: Account, created_asset: int):
    sp = algod_client.suggested_params()
    # Create asset destroy transaction to destroy the asset
    destroy_txn = transaction.AssetDestroyTxn(
        sender=acct.address,
        sp=sp,
        index=created_asset,
    )
    signed_destroy_txn = destroy_txn.sign(acct.private_key)
    txid = algod_client.send_transaction(signed_destroy_txn)
    print(f"Sent destroy transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")
