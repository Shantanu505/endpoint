from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, UserInput
from .serializers import UserSerializer, UserInputSerializer

@api_view(['POST'])
def bfhl_post(request):
    data = request.data.get('data', [])  # Extract the 'data' array from the request

    # Extract user information from the request or replace with actual user data
    user_info = {
        'user_id': 'yash_saini_24062003',
        'college_email_id': 'ys9280@srmist.edu.in',
        'college_roll_number': 'RA2011050010053',
    }

    # Separate numbers and alphabets from the input data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Find the highest alphabet (case insensitive)
    highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else None

    # Create a response dictionary
    response_data = {
        'is_success': True,  # You can change this based on your logic
        **user_info,
        'numbers': numbers,
        'alphabets': alphabets,
        'highest_alphabet': [highest_alphabet] if highest_alphabet else [],
    }

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def bfhl_get(request):
    # Your logic for the GET request goes here
    response_data = {'operation_code': 1}
    return Response(response_data, status=status.HTTP_200_OK)