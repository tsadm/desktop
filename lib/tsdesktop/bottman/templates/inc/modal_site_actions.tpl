<!-- modal_site_actions START -->
% if sitesAll:
%   for site in sitesAll:
%       status = site.status()
<div id="modal-site-actions-{{site.name}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">

            <span class="w3-closebtn"
                onclick="modalHide('modal-site-actions-{{site.name}}')">&times;</span>

            <h2>site: <a href="/siteman/{{site.name}}/view">{{site.name}}</a></h2>

            <p>
                webserver: {{site.webserver.name}}<br>
                container: {{site.webserver.containerName}}<br>
            </p>

            <hr class="w3-border">

            <p>
                <button class="w3-btn"
                    onclick="siteStart('{{site.name}}')"
%       if status == 'running':
                    disabled
%       end
                >start</button>
                <button class="w3-btn"
                    onclick="siteStop('{{site.name}}')"
%       if status != 'running':
                    disabled
%       end
                >stop</button>
                <button class="w3-btn"
                    onclick="siteRemove('{{site.name}}')"
%       if status == 'running':
                    disabled
%       end
                >remove</button>
            </p>

        </div>
    </div>
</div>
%   end
% end
<!-- modal_site_actions END -->
