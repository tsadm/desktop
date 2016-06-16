function dockmanPullImage(modalName) {
    var imgName = 'lalala';
    var url = '/dockman/'+imgName+'/pull-image';
    alert('pre reqGET: '+url);
    reqGET(url, function(xhttp){
        stopPrgrsBar(modalName);
        alert('pull image done!');
    });
    startPrgrsBar(modalName);
}
