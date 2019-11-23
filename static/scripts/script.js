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
            video.volume = 0;
        };

        var i = 0;
        screenshot = function(){
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            // Other browsers will fall back to image/png
            img.src = canvas.toDataURL('image/webp');

            var ms = 3000;
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/get-image-data",
                data: JSON.stringify(img.src),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {                     
                    response[0] = false;
                    response[1] = false;
                    response[2] = false;
                    if(response[0] == true) {               
                        stopInter();
                        console.log('traffic light');
                        $('.Scanning').addClass('hide');
                        $('.blank').addClass('hide');
                        $('.Found').removeClass('hide'); 
                        if(response[1] == true){
                            console.log('green'); 
                            $('.Green').removeClass('hide');
                            setTimeout(function(){
                                $('.Green').addClass('hide');
                                $('.Found').addClass('hide'); 
                                $('.Go').removeClass('hide');
                                setTimeout(function(){
                                    $('.Go').addClass('hide');
                                    $('.home').removeClass('hide'); 
                                    $('.main').on('click', click); 
                                    actualScreen = $('.home');
                                }, ms);
                            }, ms);                   
                        }
                        else{
                            console.log('red');
                            $('.Red').removeClass('hide');
                            setTimeout(function(){
                                $('.Red').addClass('hide');
                                $('.Found').addClass('hide'); 
                                $('.DontGo').removeClass('hide');
                                setTimeout(function(){
                                    $('.DontGo').addClass('hide');
                                    $('.home').removeClass('hide'); 
                                    $('.main').on('click', click);  
                                    actualScreen = $('.home');
                                }, ms);
                            }, ms);                
                        }
                    }
                    else{
                        if(i < 20){
                            stopInter();
                            $('.Scanning').addClass('hide');
                            $('.blank').addClass('hide');
                            $('.NotFound').removeClass('hide');
                            setTimeout(function(){
                                $('.NotFound').addClass('hide');
                                if(response[2] == true){
                                    console.log("cars")
                                    $('.Cars').removeClass('hide'); 
                                }else{                               
                                    $('.NoCars').removeClass('hide'); 
                                }
                                setTimeout(function(){
                                    if(!$('.Cars').hasClass('hide')) 
                                        $('.Cars').addClass('hide');
                                    if(!$('.NoCars').hasClass('hide')) 
                                        $('.NoCars').addClass('hide');
                                    $('.home').removeClass('hide', click);
                                    $('.main').on('click', click);  
                                    actualScreen = $('.home');
                                }, ms);
                            }, ms);                           
                        }
                        console.log('no traffic light');
                        i++;                
                    }                    
                    console.log(JSON.stringify(response)); 
                },
                error: function () {
                    console.log('error post');
                }
            });

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
            }, 500);
        };

        var inter = setInterval(screenshot, 2000);

        function stopInter(){ clearInterval(inter);};

        }).catch(function(err) { console.log(err.name + ": " + err.message); });
    };

    



    $('.main').on('click', click); 
    
    function click(){

        if(actualScreen == null)
            actualScreen = $('.home');

             
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
	
        if($(actualScreen).hasClass('Home')){
            record();         
            $('.main').unbind('click');
        }
            


        actualScreen = actualScreen.next();

        }
});