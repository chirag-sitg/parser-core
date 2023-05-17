import faust
import requests
from bs4 import BeautifulSoup
# from parser_core.config import kafka_broker
from dto.parserRequestDto import ParserRequestDTO

app = faust.App('faust-worker', broker=f'kafka://localhost:9092')

# class ParserRequestDTO(faust.Record, serializer='json'):
#     requestId: str
#     parserType: int
#     merchantId: str
#     s3BlobId: str

extract_coupon_topic = app.topic('extract_coupon_via_api', value_type=ParserRequestDTO)

@app.agent(extract_coupon_topic)
async def process_coupon_request(requestDtos):
    async for requestDto in requestDtos:
        print(f"Extracted data for website: {requestDto}")
        if requestDto.parserType == 1:
            print("Go To MailParser")
        else:
            print("Go To SiteParser")

if __name__ == '__main__':
    app.main()

