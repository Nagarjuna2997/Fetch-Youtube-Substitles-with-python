def get_captions(client, video_id):
    # Call the YouTube Data API's captions().list() method
    results = client.captions().list(
        part='snippet',
        videoId=video_id,
        onBehalfOfContentOwner=<CONTENT_OWNER_NAME>
    ).execute()
    return results
