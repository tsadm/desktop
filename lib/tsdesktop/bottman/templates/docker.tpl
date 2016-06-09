%rebase('base.tpl')
<p>
    <b>Ping:</b> {{docker.ping()}}<br>
%setdefault('dockinf', docker.version())
%for ik in sorted(dockinf.keys()):
    <b>{{ik}}:</b> {{dockinf.get(ik)}}<br>
%end
</p>
