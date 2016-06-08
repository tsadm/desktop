<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <base href="{{req.url}}" target="_self">
    <link rel="stylesheet" type="text/css" href="/static/w3.css">
    <link rel="stylesheet" type="text/css" href="/static/w3-theme-black.css">
    <link type="image/x-icon" href="/static/favicon.ico" rel="shortcut icon">
    <title>{{appName}}</title>
</head>
<body class="w3-theme-dark" style="font-family:monospace;font-size:16px">
    <!-- main -->
    <div class="w3-content w3-theme-l5 w3-padding-0">

        %include('navbar.tpl')
        %include('dockman_status.tpl')

        <!-- content -->
        <div class="w3-container">
            {{!base}}
        </div>
        <!-- content -->

        %include('footer.tpl')

    </div>
    <!-- main  -->
</body>
</html>
