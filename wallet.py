import ecdsa
import hashlib


class Wallet:
    def __init__(self):
        """
        Generates a new ECDSA private/public key pair
        """
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign_transaction(self, transaction_data):
        """
        Signs transaction data with private key
        """
        return self.private_key.sign(transaction_data.encode()).hex()

    def get_address(self):
        """
        Generates wallet address from public key
        """
        public_key_bytes = self.public_key.to_string()
        sha = hashlib.sha256(public_key_bytes).hexdigest()
        return sha
