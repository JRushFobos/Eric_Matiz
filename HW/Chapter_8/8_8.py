def make_album(artist,album,track=None)
	result = {'artist':artist, 'album': album}
	if track:
		result['track']=track
	return result

print('Input Artist, Album and count tracks*')
while = True:
	f_artist = input ('Input Artist name')
	if f_artist == 'q'
		break

	f_album = input('Input Album title')
	if f_album == 'q'
		break
	f_track = input ('Input count tracks')
	if f_track == 'q'
		break

	out = make_album(f_artist,f_album,f_track=None)
	print(out)