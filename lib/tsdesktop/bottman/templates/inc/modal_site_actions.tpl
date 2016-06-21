<!-- modal_site_actions START -->
% if sitesAll:
    % for site in sitesAll:
<div id="modal-site-actions-{{site.name}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">
            <span class="w3-closebtn"
                onclick="modalHide('modal-site-actions-{{site.name}}')">&times;</span>
            <h2>site: {{site.name}}</h2>
            <hr class="w3-border">
            <p>

                <button class="w3-btn"
                    onclick="siteAction('start', '{{site.name}}')">
                    start
                </button>

                <button class="w3-btn"
                    onclick="siteAction('stop', '{{site.name}}')">
                    stop
                </button>

                <button class="w3-btn"
                    onclick="siteRemove('{{site.name}}')">
                    remove
                </button>

            </p>
        </div>
    </div>
</div>
    % end
% end
<!-- modal_site_actions END -->
