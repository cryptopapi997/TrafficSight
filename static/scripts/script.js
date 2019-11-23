$(document).ready(function(){
    var actualScreen = null;
    $('.main').on('click', function(){
        if(actualScreen == null)
            actualScreen = $('.home');
        else
            actualScreen = actualScreen.next();


        

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

        if($(actualScreen).hasClass('.home')) 
            $('.scanning').removeClass('hide');
        if($(actualScreen).hasClass('.blank')) 
            $('.scanning').addClass('hide');




    });
});