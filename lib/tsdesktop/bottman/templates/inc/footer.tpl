<!-- footer -->
<div class="w3-container w3-center w3-small w3-slim w3-theme-l1">
    <br>
    <i class="w3-opacity w3-text-shadow">
        <a href="/about">{{appName}} v{{appVersion}}</a>
    %if reqTook:
        - {{reqTook}}s
    %end
        <br>{{now}}
    </i>
</div>
<!-- footer -->
