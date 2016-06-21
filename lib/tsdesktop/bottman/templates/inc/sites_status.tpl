<!-- sites_status START -->
<script src="/static/sites.js"></script>

% if sitesAll:

    <div class="w3-container w3-tiny w3-wide w3-padding-0">
    % for site in sitesAll:
        <button class="w3-btn w3-round-xxlarge w3-grey"
            onclick="modalShow('modal-site-actions-{{site.name}}')">
            {{site.name}}
        </button>
    % end
    </div>

    % include('inc/modal_site_actions.tpl')
    %include('inc/modal_confirm.tpl')
% end

<!-- sites_status END -->
