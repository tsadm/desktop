<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="/static/w3.css">
    <link rel="stylesheet" type="text/css" href="/static/w3-theme-black.css">
    <link type="image/x-icon" href="/static/favicon.ico" rel="shortcut icon">
    <title>{{appName}}</title>
</head>
<body class="w3-theme-dark w3-padding" style="font-family:monospace;font-size:16px">

    <!-- main -->
    <div class="w3-content w3-theme-l5 w3-padding-0">

        <!-- navbar -->
        <ul class="w3-navbar w3-card-2 w3-theme-dark">
            <li><a href="/">Home</a></li>
        </ul><!-- navbar -->

        <!-- content -->
        <div class="w3-container">
            {{!base}}
        </div><!-- content -->

        <!-- footer -->
        <div class="w3-container w3-tiny w3-padding-tiny w3-center w3-slim w3-theme-dark">
            <p class="w3-opacity w3-text-shadow">
                {{appName}} v{{appVersion}}
            </p>
        </div><!-- footer -->

    </div><!-- main  -->

</body>
</html>
