def make_album(atrist,album,track=None):
	if track:
		result = {'atrist': atrist, 'album': album, 'track':track}
	else:
		result = {'atrist': atrist, 'album': album}
	return result

prodigy = make_album('The Prodigy', 'Omen')
stromae = make_album('Stromae','Alors on Danse')
isaak = make_album('Chris Isaak',' Wicked Game')
sean = make_album('Jay Sean','Ride it',track=10)

print (prodigy)
print (stromae)
print (isaak)
print (sean)