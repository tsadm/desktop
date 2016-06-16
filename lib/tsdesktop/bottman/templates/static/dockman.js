function dockmanPullImage(modalName, srvcName) {
    modalShow(modalName, function(){
        var url = '/dockman/'+srvcName+'/pull-image';
        reqGET(url, function(xhttp){
            if (xhttp.readyState == 1) {
                startPrgrsBar(modalName);
            } else if (xhttp.readyState == 4) {
                if (xhttp.status == 200) {
                    umesgOK(srvcName+' pull image done!');
                } else {
                    umesgError('pull image error: '+xhttp.status);
                }
                stopPrgrsBar(modalName);
                modalHide(modalName);
            }
        });
    });
}
