function modalShow(name) {
    var modal = document.getElementById(name)
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    modal.style.display = 'block'
}


function modalHide(name) {
    document.getElementById(name).style.display = 'none'
}
