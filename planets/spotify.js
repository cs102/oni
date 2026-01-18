// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQA-KX3Dzmdp7ykF5iQeI8hpFKjnc2dzaiIUa3lXvG4a6Hd--Hs0x6yNkyIP8NS28gXSSuyINJWjP7doYuuR6_T00BwUQWc6qzwvC6UbSXnCNv1HDMkmmRSE_fGYxd8NY2-P_JTq36a3JRCnehsOfZBO2OfRuWkGRbqSMSRuZIdahNI0M2FSR8kLLshQrgg1o1R3_aeSsK6mh9WuAcZ6BTPairCILW6B16PYtCSNS5L39oDjSbVCisLbBdP-kufq_CLW26w59hxt7qsbVHOw_2I0wm8TLqpyhvD0FfWFLwDA_lg';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

const tracksUri = [
  'spotify:track:5QO79kh1waicV47BqGRL3g','spotify:track:0kdqcbwei4MDWFEX5f33yG','spotify:track:3khEEPRyBeOUabbmOPJzAG','spotify:track:0WZZJ0mDKIkLfL0710ssZt','spotify:track:6rD7CV7dyPBEMHt5MtXgD1'
];

async function createPlaylist(tracksUri){
  const { id: user_id } = await fetchWebApi('v1/me', 'GET')

  const playlist = await fetchWebApi(
    `v1/users/${user_id}/playlists`, 'POST', {
      "name": "My top tracks playlist",
      "description": "Playlist created by the tutorial on developer.spotify.com",
      "public": false
  })

  await fetchWebApi(
    `v1/playlists/${playlist.id}/tracks?uris=${tracksUri.join(',')}`,
    'POST'
  );

  return playlist;
}

const createdPlaylist = await createPlaylist(tracksUri);
console.log(createdPlaylist.name, createdPlaylist.id);
----
-results
My top tracks playlist
Playlist created by the tutorial on developer.spotify.com
1
Save Your Tears

The Weeknd

03:35
2
Bling-Bang-Bang-Born

Creepy Nuts

02:48
3
KICK BACK

Kenshi Yonezu

03:13
4
Neighborhood #1 (Tunnels)

Arcade Fire

04:48
5
Chalk Outlines

Ren, CHINCHILLA

03:53
