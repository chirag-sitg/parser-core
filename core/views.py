from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scripts.producer import push_to_kafka
from dto.parserRequestDto import ParserRequestDTO

class ExtractCouponCode(APIView):
    def post(self, request):
        requestDto = ParserRequestDTO(requestId= request.data.get('requestId'),
                                      parserType= request.data.get('parserType'),
                                      merchantId= request.data.get('merchantId'),
                                      s3BlobId= request.data.get('s3BlobId'))
        
        push_to_kafka(requestDto)
        return JsonResponse({ 'message':'Successfully queued for processing!' }, status=201)
