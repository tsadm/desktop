% rebase('inc/base.tpl')
<br>
<form class="w3-container" action="/site/open" method="post">

<label>site name:</label>
<input class="w3-input w3-border" required name="site_name"
    placeholder="my-php-site" type="text">

<label>site docroot (public_html) full path:</label>
<input class="w3-input w3-border" required name="site_docroot"
    placeholder="/home/sweet/sites/my-php-site/docroot" type="text">

<button class="w3-btn">open</button>

</form>
