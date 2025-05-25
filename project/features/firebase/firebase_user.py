from firebase_admin import auth

def get_user_by_id(user_id):
 try:
    user=auth.get_user(user_id)
    return {
        "uid":user.uid,
        "email":user.email
    }
 except auth.UserNotFoundError:
   return None
def list_all_users():
    users = []
    page_number = 0
    page = auth.list_users()  # Get the first page of users
    while page:
        page_number += 1
        print(f"Processing page {page_number}")
        for user in page.users:
            users.append({
                "uid": user.uid,
                "email": user.email,
            })
        page = page.get_next_page()
    print(f"Total users retrieved: {len(users)}")
    return users


def create_user(validated_data):
    user = auth.create_user(
        email=validated_data.email,
        password=validated_data.password
    )
    return {
        "uid": user.uid,
        "email": user.email
    }
def delete_user(user_id):
    try:
      auth.delete_user(user_id)
    except auth.UserNotFoundError:
        raise Exception(f"User with UID {user_id} not found.")
 