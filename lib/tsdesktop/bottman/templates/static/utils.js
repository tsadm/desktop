function modalShow(name) {
    var x = document.getElementById(name);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    }
}


function modalHide(name) {
    var x = document.getElementById(name);
    if (x.className.indexOf("w3-show") > -1) {
        x.className = x.className.replace(" w3-show", "");
    }
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
    umesg.innerHTML = tag+': '+text;
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


function reqPOST(url, cbfunc, data) {
    var xhttp;
    xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        cbfunc(xhttp);
    };
    xhttp.open("POST", url, true);
    xhttp.send(data);
}
