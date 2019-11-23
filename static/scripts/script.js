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

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/get-image-data",
        data: JSON.stringify(img.src),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (response) {
            console.log(JSON.stringify(response)); 
        },
        error: function () {
            console.log('error post');
          }
    });

    };

    var inter = setInterval(screenshot, 200);

    video.onclick = function(){ clearInterval(inter);};

    })
    .catch(function(err) { console.log(err.name + ": " + err.message); });

    };


    setInterval(function(){
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/get-location-info",
            dataType: "json",
            success: function (response) {
                var result = response;
                //alert(result['crossing']);
                if(result['crossing'] == true) 
                    alert(result['crossing']);
                
                
            }
        });
    }, 10000);



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