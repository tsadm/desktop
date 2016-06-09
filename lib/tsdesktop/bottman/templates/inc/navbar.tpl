<!-- navbar -->
<ul class="w3-navbar w3-theme-dark w3-padding-12 w3-card-4">
%for nl in navbarLinks:
    <li><a href="{{nl[1]}}">
    %if req.path == nl[1]:
        <b>{{nl[0]}}</b>
    %else:
        {{nl[0]}}
    %end
    </a></li>
%end
</ul>
<!-- navbar -->
