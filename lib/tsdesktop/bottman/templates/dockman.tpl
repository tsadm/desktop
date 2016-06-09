%rebase('base.tpl')
<h2>Docker</h2>
<p>
    <b>Ping:</b> {{docker.ping()}}<br>
%setdefault('dockinf', docker.version())
%for ik in sorted(dockinf.keys()):
    <b>{{ik}}:</b> {{dockinf.get(ik)}}<br>
%end
</p>

<h2>Container Images</h2>
