%rebase('inc/base.tpl')
<h3>
%for fpath in readFiles:
    {{fpath}}
%end
</h3>
<p class="w3-black w3-padding w3-text-green">
%for line in config.readlines():
    {{line}}<br>
%end
</p>
