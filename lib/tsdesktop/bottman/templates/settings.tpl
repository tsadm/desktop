%rebase('inc/base.tpl')
<p>
%for line in config.readlines():
    {{line}}<br>
%end
</p>
