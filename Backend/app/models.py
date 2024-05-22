from pydantic import BaseModel
from typing import Any, List, Dict

class BlockData(BaseModel):
    number: str
    difficulty: str
    extraData: str
    gasLimit: str
    gasUsed: str
    hash: str
    logsBloom: str
    miner: str
    mixHash: str
    nonce: str
    parentHash: str
    receiptsRoot: str
    sha3Uncles: str
    size: str
    stateRoot: str
    timestamp: str
    totalDifficulty: str
    transactions: List[Dict[str, Any]]
    transactionsRoot: str
    uncles: List[str]
