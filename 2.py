def get_client():
    # Use your API key to create a client
    youtube = build('youtube', 'v3', credentials=Credentials.from_authorized_user_info(info=None, client_id=<YOUR_CLIENT_ID>))
    return youtube
