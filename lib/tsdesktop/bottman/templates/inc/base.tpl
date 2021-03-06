<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <base href="{{req.url}}" target="_self">
    <!-- css files -->
    <link rel="stylesheet" type="text/css" href="/static/w3.css">
    <link rel="stylesheet" type="text/css" href="/static/w3-theme-black.css">
    <link type="image/x-icon" href="/static/favicon.ico" rel="shortcut icon">
    <!-- js deps -->
    <script src="/static/utils.js"></script>
    <!-- page title -->
    <title>{{appName}} - {{req.path}}</title>
</head>
<body class="w3-theme-l1" style="font-family:monospace;font-size:16px">

%   include('inc/navbar.tpl')

    <!-- main -->
    <div class="w3-content w3-theme-l5 w3-padding-0 w3-card-8"
        style="max-width:90%">

        <!-- content -->
        <div class="w3-container">
%           include('inc/umesg.tpl')
            {{!base}}
        </div>
        <!-- content -->

        <br>

    </div>
    <!-- main  -->

%   include('inc/footer.tpl')

</body>
</html>
