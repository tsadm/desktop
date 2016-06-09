%rebase('inc/base.tpl')
<h3>Docker</h3>
<p>
    <b>Ping:</b> {{docker.ping()}}<br>
%setdefault('dockinf', docker.version())
%for ik in sorted(dockinf.keys()):
    <b>{{ik}}:</b> {{dockinf.get(ik)}}<br>
%end
</p>

<h3>Container Images</h3>
