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


var prgrsBar;


function startPrgrsBar(modalName) {
    var pbarCont = document.getElementById(modalName+'-prgrsBar-container');
    var pbar = document.getElementById(modalName+'-prgrsBar');
    var confirmBtns = document.getElementById(modalName+'-confirm-buttons');
    var closeBtn = document.getElementById(modalName+'-prgrsBar-close');
    width = 1;
    pbarCont.style.display = 'block';
    confirmBtns.style.display = 'none';
    closeBtn.style.display = 'block';
    prgrsBar = window.setInterval(frame, 1000);
    function frame() {
        if (width >= 100) {
            width = 0;
        }
        width++;
        pbar.style.width = width + '%';
    }
}


function stopPrgrsBar(modalName) {
    var pbarCont = document.getElementById(modalName+'-prgrsBar-container');
    var pbar = document.getElementById(modalName+'-prgrsBar');
    var confirmBtns = document.getElementById(modalName+'-confirm-buttons');
    var closeBtn = document.getElementById(modalName+'-prgrsBar-close');
    pbarCont.style.display = 'none';
    closeBtn.style.display = 'none';
    confirmBtns.style.display = 'block';
    pbar.style.width = '0';
    window.clearInterval(prgrsBar);
}
