var imageMOdal = document.getElementById("img-modal");
function onClick(element){
    var modal = document.getElementsByClassName("myModal")[0];
    modal.style.display = "block";
    imageMOdal.src = element.src;
    var span = document.getElementsByClassName("close")[0];
    span.addEventListener('click',function(){
        modal.style.display = "none";
    });
}
