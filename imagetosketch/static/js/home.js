function slider(){
    let workbox=document.getElementById('workimg');
    let img=workbox.getAttribute('src');
    console.log(img);

    if(img=="/static/images/input.jpg"){
        workbox.setAttribute('src','/static/images/output.jpg');
    }
    else{
        workbox.setAttribute('src','/static/images/input.jpg');
    }
}
setInterval(slider, 1000);