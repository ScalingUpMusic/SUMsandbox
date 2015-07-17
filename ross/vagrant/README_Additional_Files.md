README for "Additional Files"

# Text Files

## subset_artist_location.txt

Contains artist of each track and location

For example

	AR00A6H1187FB5402A<SEP>42.73383<SEP>-84.59334<SEP>TRAKWGL12903CB8529<SEP>The Meatmen
	AR00MBZ1187B9B5DB1<SEP>29.95244<SEP>-90.05202<SEP>TRAFCPP128F426EC01<SEP>Memphis Minnie
	AR01IP11187B9AF5D2<SEP>28.33268<SEP>-80.73486<SEP>TRAZNKG12903CDCF8A<SEP>Call To Preserve
	AR01VU31187B997DA0<SEP>43.0026<SEP>-83.7826<SEP>TRAKZMB128F427B44F<SEP>Grand Funk
	AR01W2D1187FB5912F<SEP>40.01574<SEP>-105.27924<SEP>TRASHYD128F93119EE<SEP>3OH!3

Indicates you can find a track by The Meatmen in TRAKWGL12903CB8529.h5
The corresponding .h5 file is in A/K/W/ as indicated by the 3rd, 4th, and 5th letters of the filename.
I guess the numbers are latitude and longitude.
Not sure what the first ID is... artist.

## subset_tracks_per_year.txt

Pretty simple. It is ordered by year, has the track ID (same as above), the artist, and the song name. For example:

	1926<SEP>TRBHUOU128F423625E<SEP>Blind Lemon Jefferson<SEP>Long Lonesome Blues
	1926<SEP>TRBFMCN128F423625D<SEP>Blind Lemon Jefferson<SEP>Got The Blues
	1927<SEP>TRAUSMF12903CE71E5<SEP>Blind Lemon Jefferson<SEP>Wartime Blues
	1927<SEP>TRAGJGZ128F421EE19<SEP>Blind Willie McTell<SEP>Writing Paper Blues

## subset_unique_artists.txt

This clearly gives the Artist name and the Track ID. Again, not sure if the first file name is the artist ID. I guess so "AR" stands for artist and "TR" stands for track. If it's unique artist, why give the track? Not sure what the 2nd ID is either.

	AR009211187B989185<SEP>9dfe78a6-6d91-454e-9b95-9d7722cbc476<SEP>TRAWSCW12903CD6C7E<SEP>Carroll Thompson
	AR00A6H1187FB5402A<SEP>312c14d9-7897-4608-944a-c5b1c76ae682<SEP>TRAKWGL12903CB8529<SEP>The Meatmen
	AR00LNI1187FB444A5<SEP>7e836d29-fc2d-4a1f-b8da-566d47c49eed<SEP>TRAHVYQ128F429826B<SEP>Bruce BecVar
	AR00MBZ1187B9B5DB1<SEP>ff748426-8873-4725-bdc7-c2b18b510d41<SEP>TRAFCPP128F426EC01<SEP>Memphis Minnie
	AR01IP11187B9AF5D2<SEP>dbd2ebce-623d-4639-946e-c558bf56a0e3<SEP>TRAZNKG12903CDCF8A<SEP>Call To Preserve
	AR01VU31187B997DA0<SEP>103241b0-6adf-4b4f-9cff-5c87459f61a4<SEP>TRAKZMB128F427B44F<SEP>Grand Funk


## subset_unique_mbtags.txt

Each track file has music brain tags. This looks like a unique list of those (so all possible values)
	
	...
	60s
	70s
	8 mile
	80 s punk
	80s
	...

## subset_unique_terms.txt

Each track file also has "artist terms" that I think come from this list.

	00s
	00s country
	00s pop
	1800s
	1910s
	1960s soul
	1970s soul
	19th century
	19th century classical
	19th century opera


## subset_unique_tracks.txt

Looks like a list of all the tracks (duh) TrackID, ???, Artist, SongTilte.
As indicated by the ??? I don't know what the SO* ID's are. Gun to my head, I'd guess SOng, but I don't know how that would differ from track.

	TRAAAAW128F429D538<SEP>SOMZWCG12A8C13C480<SEP>Casual<SEP>I Didn't Mean To
	TRAAABD128F429CF47<SEP>SOCIWDW12A8C13D406<SEP>The Box Tops<SEP>Soul Deep
	TRAAADZ128F9348C2E<SEP>SOXVLOJ12AB0189215<SEP>Sonora Santanera<SEP>Amor De Cabaret
	TRAAAEF128F4273421<SEP>SONHOTT12A8C13493C<SEP>Adam Ant<SEP>Something Girls
	TRAAAFD128F92F423A<SEP>SOFSOCN12A8C143F5D<SEP>Gob<SEP>Face the Ashes
	TRAAAMO128F1481E7F<SEP>SOYMRWW12A6D4FAB14<SEP>Jeff And Sheri Easter<SEP>The Moon And I (Ordinary Day Album Version)
	TRAAAMQ128F1460CD3<SEP>SOMJBYD12A6D4F8557<SEP>Rated R<SEP>Keepin It Real (Skit)


# .db Files

TODO, These are SQLite db's but I haven't looked at these yet...

## subset_artist_similarity.db

## subset_artist_term.db

## subset_track_metadata.db


# .h5 File

## subset_msd_summary_file.h5

Looks like a summary of each track in the million song dataset.

	analysis
	 songs
	  (22050, 'a600d65cf157a306be60f26ecbf218f4', 0.0, 280.21506, 0.238, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0.555, -3.306, 1, 0.5, 275.528, 173.205, 5, 0.12, 'TRACCVZ128F4291A8A')
	  (22050, 'c64d75b0588e5ab552ee94548b50a4fa', 0.0, 191.68608, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.501, -10.764, 1, 0.71, 184.128, 150.955, 4, 0.6, 'TRACCMH128F428E4CD')
	  (22050, '0cadd310865701bb93ced1cd78e8910a', 0.0, 222.92853, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.329, -9.035, 1, 0.407, 216.3, 93.056, 4, 1.0, 'TRACCSW128F148C7C3')
	  (22050, '14be4fc1170152c445b3be7b8d18dfec', 0.0, 278.38649, 0.496, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0.313, -23.095, 1, 0.387, 278.386, 127.113, 1, 0.446, 'TRACCXJ128F428F0CF')
	  (22050, '1def5d8298e8cb29a188a5a7c0e9429a', 0.0, 89.15546, 4.847, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0.0, -20.359, 1, 0.0, 79.203, 90.66, 3, 0.524, 'TRACCVS12903D014F8')
	  (22050, '79ed013fa65b4fc3424dd1ef0ab76dd5', 0.0, 255.73832, 0.156, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0.556, -5.724, 1, 0.455, 252.012, 101.167, 1, 1.0, 'TRACCKS128F42B77AE')
	  (22050, '6f8cc33a8ed925e2077a876de3a11977', 0.0, 239.59465, 0.403, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0.167, -10.653, 1, 0.372, 231.805, 173.841, 3, 0.302, 'TRACCQM12903CACC1E')
	  (22050, 'ee8450e2e32b8adc9623d95ba6633b2f', 0.0, 156.96934, 0.322, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0.772, -20.816, 0, 0.524, 142.286, 127.547, 1, 0.168, 'TRACCUS128F92E1FEB')
	  (22050, '60d56ccbced3db74f86bddc21bb4c92f', 0.0, 197.19791, 0.276, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0.665, -29.75, 1, 0.582, 187.582, 127.782, 4, 0.226, 'TRACCJA128F149A144')
	  (22050, '19a1d23af6018cdfb32e8e751932d662', 0.0, 262.5824, 2.328, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0.317, -5.644, 1, 0.357, 257.155, 90.013, 5, 0.386, 'TRACCGB12903CD1B90')
	  ...(10000)
	metadata
	 songs
	  ('', 29785, 0.7804617487770407, 0.5742747305168561, 'ARMQHX71187B9890D3', nan, 'Atlanta, GA', nan, 'bc5e2ad6-0a4a-4d90-b911-e9a7e6861727', 'Mastodon', -1, '', 0, 0, 'Call of the Mastodon', 223563, 0.5976407977147769, 'SOVLGJY12A8C13FBED', 'Deep Sea Creature', 2442524)
	  ('', 167867, 0.5615899458566065, 0.4205703072083738, 'AR2PT4M1187FB55B1A', nan, '', nan, 'd54ea4a6-0b9c-4e47-bed0-289ae9ff4037', 'Los Chichos', 1880, '', 0, 0, 'Adelante', 221677, nan, 'SOGDQZK12A8C13F37C', 'No Quieras Marcharte', 2423472)
	  ('', 7725, 0.6876874858721554, 0.4066860994666606, 'ARDI88R1187B98DAB2', nan, '', nan, 'fd87374e-ffde-4d36-89a8-8a073f795666', 'Foxy Brown', -1, '', 0, 0, 'Ill Na Na', 47304, 0.5889221675559065, 'SODMVJR12A6D4F985D', 'If I...', 507029)
	  ('', 2799, 0.39174139414810444, 0.2912648117531004, 'ARUKJUP12086C14589', nan, '', nan, '8a5f2736-bcde-4a2e-8d50-72631d66a7ef', 'Ram\xc3\xb3n Vargas;Vladimir Jurowski', 20111, '', 0, 0, 'Massenet: Werther', 295123, nan, 'SOIWBDR12A8C13A4AC', "Werther - Lyric Drama in four Acts/Act I/Alors_ c'est bien ici la maison du bailli?", 3343102)
	  ('', 74269, 0.5934160487797832, 0.39570954770762196, 'ARZEWUR1187FB53DC8', 50.45663, 'Belgica -- Namur, Namur/Ghent, East Flanders', 4.87137, '0be59867-0da4-4e45-9b64-728cdf25487c', 'Enthroned', 55656, '', 0, 0, 'Pentagrammaton', 785362, nan, 'SOHCCIA12AC907577F', 'Ad Te Clamamus Exsvles Mortva Liberi', 8688607)
	  ('', 49956, 0.8159234203436856, 0.5551383219226409, 'ARUZRFN1187B98AC05', nan, 'Cleveland, OH', nan, '2fa45bbb-0efb-4950-9d40-94bf23cbfec1', 'Bone Thugs-N-Harmony', 5412, '', 0, 0, 'BTNHRESURRECTION', 310248, 0.47405483093120077, 'SOBOAQC12A8C13E3E9', 'Murder One', 3510188)
	  ('', 25694, 0.5439365518845259, 0.4303002791079415, 'ARHBWOZ1187FB3FD53', nan, 'ITALY', nan, 'e6ff2839-5ccb-451b-b07e-f485bc143118', 'Utopia', 6721, '', 0, 0, 'Utopia', 576541, nan, 'SOKVLHX12AB0187B39', 'On My Feet Again', 6389516)
	  ('', 588, 0.9290302874411605, 0.7504265510189179, 'ARR3ONV1187B9A2F59', 54.31407, 'UK', -2.23001, 'fd857293-5ab8-40de-b29e-55a69d4e4d0f', 'Muse', -1, '', 0, 0, 'Plug In Baby', 521383, 0.6528356953891383, 'SOMMSMW12A8C13FCCC', 'Bedroom Acoustics', 5764770)
	  ('', 11301, 0.6451923387467661, 0.47122432991900803, 'AR3THYK1187B999F1F', nan, '', nan, '286ec4c2-b5ca-4f85-b331-280a6d73dd14', 'Jo\xc3\xa3o Gilberto', -1, '', 0, 0, 'Joao Voz E Violato', 55934, 0.6316008180888096, 'SODPNJR12A6D4FA52D', 'Segredo', 581259)
	  ('', 19967, 0.495819328959285, 0.34276521913001623, 'ARFELOH1187B991F95', nan, '', nan, '65b785d9-499f-48e6-9063-3a1fd1bd488d', 'Niraj Chag', -1, '', 0, 0, 'The Lost Souls Bonus EP', 722229, nan, 'SOFFLLP12AB018ED52', 'Sajana (Ft Faheem Mazhar)', 8005714)
	  ...(10000)
	musicbrainz
	 songs
	  (0, 2001)
	  (0, 1984)
	  (0, 0)
	  (0, 0)
	  (0, 2010)
	  (0, 2000)
	  (0, 0)
	  (0, 0)
	  (0, 2000)
	  (0, 0)
	  ...(10000)
