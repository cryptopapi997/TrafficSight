var crd = null;
var crdCounter = 0;
var crdlist;

var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };
  
  function success(pos) {
    crd = pos.coords;
    console.log("Fuck");
    crdlist[crdCounter] = crd;
    crdCounter++;

  }
  
  function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }
  

  while(true){
    navigator.geolocation.getCurrentPosition(success, error, options);
    setTimeout(function(){
        console.log("Sleeping");
    }, 500);
  }

  