var pc = null;

function createPeerConnection() {
    pc = new RTCPeerConnection();
    pc.addEventListener('track', function(evt) {
        document.getElementById('video').srcObject = evt.streams[0];
    });
    return pc;
}

function negotiate() {
    return pc.createOffer().then(function(offer) {
        return pc.setLocalDescription(offer);
	}).then(function()){
        var offer = ip;
        return fetch('/offer', {
            body: JSON.stringify({
                ip: offer,
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
    pc = createPeerConnection();
    negotiate();
}

function stop() {
    pc.close();
}

