function _siteAction(action, site) {
    var msg = action+' site: '+site;
    modalConfirm(msg, function(){
        var url = '/siteman/'+site+'/'+action;
        reqPOST(url, function(xhttp){
            if (xhttp.readyState == 4) {
                if (xhttp.status == 200) {
                    umesgOK(site+' '+action+' done!');
                } else {
                    umesgError(site+' '+action+': '+xhttp.responseText);
                }
                modalConfirmEnd();
            }
        });
    });
    modalHide('modal-site-actions-'+site);
}


function siteRemove(name) {
    _siteAction('remove', name)
}
