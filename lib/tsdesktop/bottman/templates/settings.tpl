%rebase('inc/base.tpl')
<p>
    read files:
%for fpath in readFiles:
    {{fpath}}
%end
</p>
<p>
%for line in config.readlines():
    {{line}}<br>
%end
</p>
