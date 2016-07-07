#!/bin/bash

html_head() {
    local fpath=$1
    cat <<EOH
<!DOCTYPE html>
<html>
<head>
    <style>
    body {
        padding:1% 3%;
        margin:0;
        background-color:black;
        color:white;
        font-family:monospace;
        font-size:14px;
    }
    h1, h2, h3 {
        border-bottom:1px solid gray;
    }
    code {
        padding:4px;
        background-color:#333333;
    }
    pre {
        padding:4px;
        background-color:#333333;
    }
    pre code {
        padding:0;
    }
    a {
        color:#0000dd;
    }
    a:hover {
        color:#0000dd;
    }
    </style>
    <title>${fpath}</title>
</head>
<body>
EOH
}

html_tail() {
    cat <<EOT
</body>
</html>
EOT
}

for fpath in `find . -type f -name '*.md'`; do
    dest=htdocs/${fpath/\.md/\.html}
    mkdir -p `dirname $dest`
    html_head $fpath >$dest
    python3 -m markdown -o html5 -f ${dest}.tmp $fpath
    cat ${dest}.tmp | sed 's/\.md"/\.html"/g' >>$dest
    rm -f ${dest}.tmp
    html_tail >>$dest
done
