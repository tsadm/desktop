%rebase('inc/base.tpl')
<h3>ERROR - {{err.status}}</h3>
<pre class="w3-red w3-padding">
{{err.body}}
%if err.exception:
{{err.exception}}
%end
%if err.traceback:
{{err.traceback}}
%end
</pre>
