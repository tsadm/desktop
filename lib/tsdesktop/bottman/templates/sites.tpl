% rebase('inc/base.tpl')
<br>
<form class="w3-container w3-border" action="/sites/open" method="post">

<label>site name<sup>*</sup></label>
<input class="w3-input w3-border" required name="site_name"
    pattern="^[a-zA-Z0-9.-_]+$"
    placeholder="my-php-site" type="text">

<label>site docroot (public_html) full path</label>
<input class="w3-input w3-border" required name="site_docroot"
    placeholder="/home/sweet/sites/my-php-site/docroot" type="text">

<sub>*only: a-z, A-Z, 0-9 and .-_ (no spaces)</sub>

<div class="w3-right">
<button class="w3-btn">add</button><br>
</div>

</form>

<br>
% include('inc/sites_status.tpl')
