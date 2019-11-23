$(document).ready(function(){
    var actualScreen = null;
function record(){
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

var inter = setInterval(screenshot, 200);

video.onclick = function(){ clearInterval(inter);};

})
.catch(function(err) { console.log(err.name + ": " + err.message); });

};
    $('.main').on('click', function(){

        if(actualScreen == null)
            actualScreen = $('.home');
        else
            actualScreen = actualScreen.next();
        
             
        if($(actualScreen).hasClass('blank')) 
            $('.Scanning').addClass('hide');
        if($(actualScreen).hasClass('Home')) 
            $('.Scanning').removeClass('hide'); 
        //if no traffic light was found, show specific screen

        //if rest request returns traffic light is green, show the green screen, else the redscreen


        if(!$(actualScreen).hasClass('.hide')){
            $(actualScreen).addClass('hide');
            var nextSibling = actualScreen.next();
            if(nextSibling.length != 0)
                $(nextSibling).removeClass('hide');
            //else
                //todo, if all screens were shown, how to proceed 
        }
	
	if($(actualScreen).hasClass('Home'))
		record();


    });
});