%rebase('inc/base.tpl')
%include('inc/dockman_status.tpl')

<h3>images</h3>
<p>
%for srv in dockmanServices:
    <b>{{srv.name}}</b>:
    %imgInfo = srv.imageInfo()
    <small>&lt;{{imgInfo.name}}&gt;
    %linkAction = 'pull'
    %if imgInfo.status == 'missing':
        <span class="w3-small w3-badge w3-yellow">miss</span>
    %elif imgInfo.status == 'ok':
        <span class="w3-small w3-badge w3-green">ok</span>
        %linkAction = 'update'
    %else:
        <span class="w3-small w3-badge w3-red">err</span>
    %end
        <a href="/dockman/{{srv.name}}/pull-image/">{{linkAction}}</a>
    </small>
    <br>
%end
</p>

<h3>docker</h3>
<p class="w3-small">
    Ping: {{docker.ping()}}<br>
%dockinf = docker.version()
%for ik in sorted(dockinf.keys()):
    {{ik}}: {{dockinf.get(ik)}}<br>
%end
</p>
