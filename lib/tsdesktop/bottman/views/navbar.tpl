<!-- navbar -->
<ul class="w3-navbar w3-card-2 w3-theme-dark w3-wide">

%if req.path == '/':
    <li class="w3-opacity">
%else:
    <li>
%end
        <a href="/">dashboard</a>
    </li>

%if req.path == '/settings':
    <li class="w3-opacity">
%else:
    <li>
%end
        <a href="/settings">settings</a>
    </li>

</ul>
<!-- navbar -->
