<?php
$tsdesktop_site = getenv('TSDESKTOP_SITE');

$databases = array (
    'default' => array (
        'default' => array (
            'database' => "${tsdesktop_site}db",
            'username' => "${tsdesktop_site}",
            'password' => '',
            'host' => 'tsdesktop-mysqld',
            'port' => '',
            'driver' => 'mysql',
            'prefix' => '',
        ),
    ),
);
