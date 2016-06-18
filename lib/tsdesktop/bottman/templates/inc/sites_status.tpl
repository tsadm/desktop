<!-- sites_status START -->
% if sitesAll:
<div class="w3-container w3-tiny w3-wide w3-padding-0">
    <p>
    % for site in sitesAll:
        {{site}}<br>
    % end
    </p>
</div>
% end
<!-- sites_status END -->
