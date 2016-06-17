function dockmanPullImage(srvcName) {
    var msg = 'pull image: '+srvcName;
    modalConfirm(msg, function(){
        var url = '/dockman/'+srvcName+'/pull-image';
        reqGET(url, function(xhttp){
            if (xhttp.readyState == 4) {
                if (xhttp.status == 200) {
                    umesgOK(srvcName+' pull image done!');
                } else {
                    umesgError('pull image error: '+xhttp.status);
                }
                modalConfirmEnd(false);
            }
        });
    });
}


function dockmanAction(action, srvcName) {
    var msg = action+' service: '+srvcName;
    modalConfirm(msg, function(){
        alert(msg);
        modalConfirmEnd(true)
    });
    modalHide('dockman_'+srvcName);
}


function dockmanStart(srvcName) {
    dockmanAction('start', srvcName);
}
