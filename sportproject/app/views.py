
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from database import users_collection
from .models import User, LoginUser


@csrf_exempt
def register(request):

    data = json.loads(request.body)

    user = User(**data)

    users_collection.insert_one(user.model_dump())

    return JsonResponse({
        "message": "Registration Successfully"
    })



@csrf_exempt
def login(request):

    data = json.loads(request.body)

    user = LoginUser(**data)

    result = users_collection.find_one({
        "username": user.username,
        "password": user.password
    })

    if result:

        request.session["username"] = user.username

        return JsonResponse({
            "message": "Login Successfully"
        })

    return JsonResponse({
        "message": "Invalid Username or Password"
    }, status=401)




@csrf_exempt
def profile(request, username):
    if request.method != "GET":
        return JsonResponse({"error": "GET method required"}, status=405)

    try:
        user_data = users_collection.find_one(
            {"username": username},
            {"password": 0, "_id": 0}
        )

        if user_data:
            return JsonResponse({
                # "message": "Profile fetched successfully",
                "profile": user_data
            }, status=200)

        return JsonResponse({
            "message": "User not found"
        }, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    

@csrf_exempt
def logout(request):

    if "username" in request.session:

        request.session.flush()

        return JsonResponse({
            "message": "Logout Successfully"
        })

    return JsonResponse({
        "message": "User Not Logged In"
    }, status=401)
    
    
    
    

@csrf_exempt
def profile_update(request, username):

    if request.method != "PUT":
        return JsonResponse({
            "error": "PUT method required"
        }, status=405)

    try:

        data = json.loads(request.body)

        result = users_collection.update_one(
            {"username": username},
            {"$set": data}
        )

        if result.matched_count > 0:

            return JsonResponse({
                "message": "Profile Updated Successfully"
            }, status=200)

        return JsonResponse({
            "message": "User not found"
        }, status=404)

    except Exception as e:

        return JsonResponse({
            "error": str(e)
        }, status=500)
    