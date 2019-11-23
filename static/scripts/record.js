<video autoplay style="display:none;"></video>
<img src="" style="display:none;">
<canvas style="display:none;"></canvas>

<script>
var constraints = { audio: true, video: { width: 1280, height: 720 } }; 

const canvas = document.createElement('canvas');
const img = document.querySelector('img');

navigator.mediaDevices.getUserMedia(constraints)
.then(function(mediaStream) {
  var video = document.querySelector('video');
  video.srcObject = mediaStream;
  video.onloadedmetadata = function(e) {
    video.play();
  };

screenshot = function(){
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  // Other browsers will fall back to image/png
  img.src = canvas.toDataURL('image/webp');
};

var inter = setInterval(screenshot, 100);

video.onclick = function(){ clearInterval(inter);};

})
.catch(function(err) { console.log(err.name + ": " + err.message); });