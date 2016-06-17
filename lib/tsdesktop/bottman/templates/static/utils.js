function modalShow(name) {
    var modal = document.getElementById(name)
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    modal.style.display = 'block';
    return modal;
}


function modalHide(name) {
    document.getElementById(name).style.display = 'none';
}


var confirmCallback;


function modalConfirm(text, cbfunc) {
    confirmCallback = function(){
        startPrgrsBar();
        cbfunc();
    }
    _confirmText(text);
    modalShow('modalConfirm');
}


function modalConfirmEnd() {
    stopPrgrsBar();
    modalHide('modalConfirm');
}


function _confirmText(text) {
    var elem = document.getElementById('modalConfirm-message');
    elem.innerHTML = text;
}


var prgrsBar;


function startPrgrsBar() {
    var pbarCont = document.getElementById('prgrsBar-container');
    var pbar = document.getElementById('prgrsBar');
    var confirmBtns = document.getElementById('modalConfirm-buttons');
    var closeBtn = document.getElementById('prgrsBar-close');
    width = 0;
    elapsed = 0;
    pbarCont.style.display = 'block';
    confirmBtns.style.display = 'none';
    closeBtn.style.display = 'block';
    prgrsBar = window.setInterval(frame, 1000);
    function frame() {
        if (width >= 100) {
            width = 0;
        }
        width++;
        elapsed++;
        pbar.style.width = width+'%';
        pbar.innerHTML = elapsed+'s';
    }
}


function stopPrgrsBar() {
    var pbarCont = document.getElementById('prgrsBar-container');
    var pbar = document.getElementById('prgrsBar');
    var confirmBtns = document.getElementById('modalConfirm-buttons');
    var closeBtn = document.getElementById('prgrsBar-close');
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
}
