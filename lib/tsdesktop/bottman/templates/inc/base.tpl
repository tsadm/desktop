<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <base href="{{req.url}}" target="_self">
    <link rel="stylesheet" type="text/css" href="/static/w3.css">
    <link rel="stylesheet" type="text/css" href="/static/w3-theme-black.css">
    <link type="image/x-icon" href="/static/favicon.ico" rel="shortcut icon">
    <title>{{appName}} - {{req.path}}</title>
</head>
<body class="w3-theme-l1" style="font-family:monospace;font-size:16px">
    <script src="/static/utils.js"></script>

    %include('inc/navbar.tpl')

    <!-- main -->
    <div class="w3-content w3-theme-l5 w3-padding-0 w3-card-8"
        style="min-width:90%">
        <!-- content -->
        <div class="w3-container">
            {{!base}}
        </div>
        <!-- content -->
        <br>
    </div>
    <!-- main  -->

    %include('inc/footer.tpl')
</body>
</html>
