from dataclasses import dataclass

@dataclass(frozen=True)
class ParserRequestDTO:
    requestId: str
    parserType: int
    merchantId: str
    s3BlobId: str
