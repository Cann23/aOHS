var pc = null;

function negotiate() {
	pc.addTransceiver('video', {direction: 'recvonly'});
	return pc.createOffer().then(function(offer) {
		return pc.setLocalDescription(offer);
	}).then(function() {
		// wait for ICE gathering to complete
		return new Promise(function(resolve) {
			if (pc.iceGatheringState === 'complete') {
				resolve();
			} else {
				function checkState() {
					if (pc.iceGatheringState === 'complete') {
						pc.removeEventListener('icegatheringstatechange', checkState);
						resolve();
					}
				}
				pc.addEventListener('icegatheringstatechange', checkState);
			}
		});
	}).then(function() {
		var offer = pc.localDescription;
		var urlParams = new URLSearchParams(window.location.search);
		return fetch('offer/', {
			body: JSON.stringify({
				sdp: offer.sdp,
				type: offer.type,
				url: escape(urlParams.get('url'))
			}),
			headers: {
				'Content-Type': 'application/json'
			},
			method: 'POST'
		});
	}).then(function(response) {
		return response.json();
	}).then(function(answer) {
		return pc.setRemoteDescription(answer);
	}).catch(function(e) {
		alert(e);
	});
}

function start() {
	var config = {
		sdpSemantics: 'unified-plan'
	};
	pc = new RTCPeerConnection(config);
	pc.addEventListener('track', function(evt) {
		if (evt.track.kind == 'video') {
			document.getElementById('video').srcObject = evt.streams[0];
		}
	});	
	negotiate();
}

function stop() {
	setTimeout(function() {
		pc.close();
	}, 500);
}

start();
