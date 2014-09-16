
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import connection
from calendar import monthrange
import datetime

from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

# serializers
from serializers import BranchSerializer
from serializers import ContactSerializer
from serializers import DealSerializer
from serializers import DealBranchSerializer

# models
from models import Branch
from models import Contact
from models import Deal
from models import DealBranch

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def branches(request, id=0):
    if request.method == 'GET':
        all_branches = Branch.objects.get(user=request.user)
        serializer = BranchSerializer(all_branches)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BranchSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.data.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        branch = Branch(id=id)
        serializer = BranchSerializer(branch, data=request.DATA)
        if serializer.is_valid():
            serializer.data.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        branch = Branch(id=id)
        branch.delete()
        return Response("DELETED", status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def branch_info(request, id=0):
    branch = Branch.objects.get(pk=id)
    serializer = BranchSerializer(branch)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def branch_contacts(request, id=0):
    contacts = Contact.objects.select_related('branch').filter(branch__id=id).order_by('id')
    serializer = ContactSerializer(contacts)
    return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def contacts(request, id=0):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        contact = Contact(id=id)
        serializer = ContactSerializer(contact, data=request.DATA)
        if serializer.is_valid():
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact = Contact(id=id)
        contact.delete()
        return Response("DELETED", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def contact_info(request, id=0):
    contact = Contact.objects.get(pk=id)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def deals(request, id=0):
    if request.method == 'GET':
        all_deals = Deal.objects.all().order_by('id')
        serializer = DealSerializer(all_deals)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DealSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        deal = Deal(id=id)
        serializer = DealSerializer(deal, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        deal = Deal(id=id)
        deal.delete()
        return Response("DELETED", status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def deal_info(request, id=0):
    deal = Deal.objects.get(pk=id)
    serializer = DealSerializer(deal)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def deal_branches(request, id=0):
    if request.method == 'GET':
        branches = DealBranch.objects.select_related('deal').filter(deal__id=id).order_by('id')
        serializer = DealBranch(branches)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DealBranchSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        deal = DealBranch(id=id)
        serializer = DealBranchSerializer(deal, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        deal_branch = DealBranch(id=id)
        deal_branch.delete()
        return Response("DELETED", status=status.HTTP_200_OK)