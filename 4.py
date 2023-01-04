captions = get_captions(client, video_id)

if 'items' in captions:
    for caption in captions['items']:
        print(f'Caption track name: {caption["snippet"]["name"]}')
        print(f'Caption track language: {caption["snippet"]["language"]}')
else:
    print('No caption tracks found')
