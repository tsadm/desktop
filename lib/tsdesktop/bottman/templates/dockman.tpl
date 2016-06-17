% rebase('inc/base.tpl')
% include('inc/dockman_status.tpl')

<h3>images</h3>
<div class="w3-container">
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
    <p>
        <b>{{srv.name}}</b>:
        <small>&lt;{{imgInfo.name}}&gt;</small>
        <button
            class="w3-btn w3-small w3-padding-tiny w3-border {{btnColor}}"
            onclick="dockmanPullImage('{{srv.name}}')"
        >{{linkAction}}</button>
    </p>
% end
</div>

<h3>docker</h3>
<p class="w3-container w3-small">
    Ping: {{docker.ping()}}<br>
% dockinf = docker.version()
% for ik in sorted(dockinf.keys()):
    {{ik}}: {{dockinf.get(ik)}}<br>
% end
</p>
