import json
import av

from django.http import JsonResponse
from aiortc import RTCPeerConnection, RTCSessionDescription, MediaStreamTrack

class IPCameraTrack(MediaStreamTrack):
	kind = "video"
	def __init__(self, url):
		super().__init__()
		self.container = av.open(url, options={'rtsp_transport': 'tcp'})
		self.stream = self.container.streams.video[0]

	async def recv(self):
		for frame in self.container.decode(self.stream):
			return frame

track = None
pcs = set()

async def offer(request):
    params = json.loads(request.body)
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)

    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        print("Connection state is %s" % pc.connectionState)
        if pc.connectionState == "failed":
            await pc.close()
            pcs.discard(pc)

    track = IPCameraTrack(params["url"])

    await pc.setRemoteDescription(offer)
    for t in pc.getTransceivers():
        if t.kind == "video" and track:
            pc.addTrack(track)

    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    
    return JsonResponse(
        data={
        "sdp": pc.localDescription.sdp,"type": pc.localDescription.type
        }
    )

