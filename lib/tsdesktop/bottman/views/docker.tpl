%rebase('base.tpl')
<p>
    <b>Ping:</b> {{docker.ping()}}<br>
%for ik, iv in docker.version().items():
    <b>{{ik}}:</b> {{iv}}<br>
%end
</p>
