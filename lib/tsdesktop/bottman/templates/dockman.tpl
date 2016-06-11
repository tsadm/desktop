% rebase('inc/base.tpl')
% include('inc/dockman_status.tpl')

<h3>images</h3>
<p>
% for srv in dockmanServices:
    % imgInfo = srv.imageInfo()
    % linkAction = 'pull'
    % btnColor = 'w3-red'
    % if imgInfo.status == 'missing':
        % btnColor = 'w3-yellow'
    % elif imgInfo.status == 'ok':
        % btnColor = 'w3-green'
        % linkAction = 'update'
    % end
    % modalName = 'dockman-'+linkAction+'-image-'+srv.name
    % modalMessage = linkAction+' image: '+imgInfo.name
    % destURL = '/dockman/'+srv.name+'/pull-image/'
    <b>{{srv.name}}</b>:
    <small>&lt;{{imgInfo.name}}&gt;</small>
    <button
        class="w3-btn w3-small w3-padding-tiny w3-border {{btnColor}}"
        onclick="modalShow('{{modalName}}')"
    >{{linkAction}}</button>
    % include('inc/modal_confirm.tpl')
% end
</p>

<h3>docker</h3>
<p class="w3-small">
    Ping: {{docker.ping()}}<br>
% dockinf = docker.version()
% for ik in sorted(dockinf.keys()):
    {{ik}}: {{dockinf.get(ik)}}<br>
% end
</p>
