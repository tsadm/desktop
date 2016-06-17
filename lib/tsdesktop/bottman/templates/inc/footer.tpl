<!-- footer -->
<div class="w3-container w3-center w3-small w3-slim w3-theme-l1">
    <br>
    <i class="w3-opacity w3-text-shadow">
    %if req.path == '/about':
        <b><a href="/about">{{appName}} v{{appVersion}}</a></b>
    %else:
        <a href="/about">{{appName}} v{{appVersion}}</a>
    %end
    %if reqTook:
        - {{reqTook}}s
    %end
        <br>{{now}}
    </i>
</div>
<!-- footer -->
