<!-- navbar -->
<ul class="w3-navbar w3-theme-dark">

    <li><a href="/">
    %if req.path == '/':
        <b>dashboard</b>
    %else:
        dashboard
    %end
    </a></li>

    <li><a href="/settings">
    %if req.path == '/settings':
        <b>settings</b>
    %else:
        settings
    %end
    </a></li>

</ul>
<!-- navbar -->
