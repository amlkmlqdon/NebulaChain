from flask import Flask, request, jsonify
from blockchain import Blockchain
import json

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    Creates a new transaction
    """
    tx_data = request.get_json()
    required_fields = ["sender", "recipient", "amount"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 400

    blockchain.add_transaction(tx_data)
    return "Transaction added", 201


@app.route('/mine', methods=['GET'])
def mine():
    """
    Mines pending transactions
    """
    result = blockchain.mine()
    if not result:
        return "No transactions to mine", 200

    return f"Block #{result} mined successfully!", 200


@app.route('/chain', methods=['GET'])
def get_chain():
    """
    Returns full blockchain
    """
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({
        "length": len(chain_data),
        "chain": chain_data
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
