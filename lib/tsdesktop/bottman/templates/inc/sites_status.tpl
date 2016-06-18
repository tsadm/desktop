<!-- sites_status START -->
% if sitesAll:
<div class="w3-container w3-tiny w3-wide w3-padding-0">
    % for site in sitesAll:
    <button class="w3-btn w3-round-xxlarge w3-grey"
        onclick="alert('site actions modal!')">
        {{site.name}}
    </button>
    % end
</div>
% end
<!-- sites_status END -->
