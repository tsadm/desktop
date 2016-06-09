%rebase('inc/base.tpl')
%include('inc/dockman_status.tpl')

<h3>images</h3>
<p>
%for srv in dockmanServices:
    %imgInfo = srv.imageInfo()
    <b>{{srv.name}}</b>: {{imgInfo.name}}
    %if imgInfo.status == 'missing':
        <span class="w3-small w3-badge w3-yellow">miss</span>
        <a href="#pull-image/{{imgInfo.name}}">pull</a>
    %elif imgInfo.status == 'ok':
        <span class="w3-small w3-badge w3-green">ok</span>
        <a href="#update-image/{{imgInfo.name}}">update</a>
    %else:
        <span class="w3-small w3-badge w3-red">err</span>
    %end
    <br>
%end
</p>

<h3>docker</h3>
<p>
    Ping: {{docker.ping()}}<br>
%dockinf = docker.version()
%for ik in sorted(dockinf.keys()):
    {{ik}}: {{dockinf.get(ik)}}<br>
%end
</p>
