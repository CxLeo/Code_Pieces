@api_view(['POST'])
def client_data_store(request):
    if request.method == 'POST':
        club_name = request.data["club_name"]
        city = request.data["location"].get("city")
        province = request.data["location"].get("province")
        sport_name = request.data["sport_name"]
        email = request.data["email"]
        involvement = request.data["involvement"]
        knowledge = request.data["knowledge"]
        position = request.data["position"]

        content = {
            "club_name":club_name, "city":city, "province":province, "sport_name":sport_name,
            "email":email, "involvement":involvement, "knowledge":knowledge, "position":position
            }
        serializer = client_serializer(data=content)
        if serializer.is_valid():
            serializer.save()
            content = {"status": 0, "message": "New client added", "id": serializer.data['client_id']}
            return Response(content, status=status.HTTP_200_OK)

@api_view(['GET'])
def client_all_view(request):
    if request.method == 'GET':
        client_objects = Client.objects.all()
        serializer = client_serializer_all(client_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def client_view(request, email):
    if request.method == 'GET':
        try:
            client_object = Client.objects.all().get(email=email)
            serializer = client_serializer(client_object)
            content = {
                    "client_id": serializer.data['client_id'],
                    "club_name": serializer.data['club_name'],
                    "location": {
                                "city": serializer.data['city'],
                                "province": serializer.data['province']
                                },
                    "sport_name": serializer.data['sport_name'],
                    "email": serializer.data['email'],
                    "involvement": serializer.data['involvement'],
                    "knowledge": serializer.data['knowledge'],
                    "position": serializer.data['position']
                    }
            return Response(content, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
          
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        try:
            user_database = User.objects.all().get(email=request.data['email'])
            user = authenticate(request, username=user_database.username, password=request.data['password'])
            
            if user is not None:
                login(request, user)
                return Response({"is_admin": user.is_staff}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def logout_view(request):
    if request.method == 'GET':
        try:
            logout(request)
            return Response({"state": "Successfully Log Out"}, status=status.HTTP_200_OK)
        except:
            return Response({"state": "Already Log Out or Not Sign In"}, status=status.HTTP_400_BAD_REQUEST)
