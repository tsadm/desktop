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
                container: {{site.webserver.containerName}}
            </p>

            <hr class="w3-border">

%       if status == 'running':
            <a href="{{site.webserver.URI}}" target="_blank">{{site.webserver.URI}}</a>
%           if site.webserver.URIDesc:
            <br><small>{{site.webserver.URIDesc}}</small>
%           end
%       end

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
