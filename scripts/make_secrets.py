"""Makes the three secrets the PDS needs. Paste them into Railway's variables and keep a private copy somewhere safe:
the rotation key controls every account's identity, and losing it means accounts can no longer be moved.

    python3 scripts/make_secrets.py
"""
import secrets

# secp256k1's group order: a private key is any number from 1 to N-1
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def k256_key():
    while True:
        k = int.from_bytes(secrets.token_bytes(32), "big")
        if 0 < k < N:
            return "%064x" % k


if __name__ == "__main__":
    print("PDS_JWT_SECRET=" + secrets.token_hex(16))
    print("PDS_ADMIN_PASSWORD=" + secrets.token_hex(16))
    print("PDS_PLC_ROTATION_KEY_K256_PRIVATE_KEY_HEX=" + k256_key())
