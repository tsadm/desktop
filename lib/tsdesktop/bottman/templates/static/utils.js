var modalCallback;


function modalShow(name, cbfunc) {
    var modal = document.getElementById(name)
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    modal.style.display = 'block'
    modalCallback = cbfunc;
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


function umesg(tag, text) {
    document.getElementById('umesg').style.display = 'block';
    var umesg;
    if (tag == 'OK') {
        umesg = document.getElementById('umesg-ok');
    } else {
        umesg = document.getElementById('umesg-error');
    }
    umesg.style.display = 'block';
    umesg.innerHTML = text;
}


function umesgError(text) {
    umesg('ERROR', text);
}


function umesgOK(text) {
    umesg('OK', text);
}


function reqGET(url, cbfunc) {
    var xhttp;
    xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        cbfunc(xhttp);
    };
    xhttp.open("GET", url, true);
    xhttp.send();
    return xhttp
}
