<!-- modal_site_open START -->
<button onclick="modalShow('modal-site-open')" class="w3-btn">open site</button>
<div id="modal-site-open" class="w3-modal" style="display:none">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container w3-border">
            <span class="w3-closebtn" onclick="modalHide('modal-site-open')">&times;</span>
            <h2>open site</h2>
            <hr>
            <form class="w3-container">

            <label class="w3-label">
                site docroot (public_html) full path
            </label>
            <input class="w3-input w3-border"
                placeholder="/home/joe/sites/my-php-site/docroot"
                type="text">

            <br>
            <button class="w3-btn">open</button>

            </form>
            <br>
        </div>
    </div>
</div>
<!-- modal_site_open END -->
