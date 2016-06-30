<!-- dockman modals -->
% for srv in dockmanServices:
<div id="dockman_{{srv.name}}" class="w3-modal">
%   status = srv.status()
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">
            <span class="w3-closebtn" onclick="modalHide('dockman_{{srv.name}}')">&times;</span>
            <h2>service: {{srv.name}}</h2>
            <p>
                container: {{srv.containerName}}
            </p>
            <hr class="w3-border">
            <p>
%   if status == 'running':
                <a href="{{srv.URI}}" target="_blank">{{srv.URI}}</a>
%       if srv.URIDesc:
                <br><small>{{srv.URIDesc}}</small>
%       end
%   else:
                <span class="w3-opacity">{{srv.URI}}</span>
%   end
            </p>
            <p>
                <button class="w3-btn"
                    onclick="dockmanStart('{{srv.name}}')"
%   if status == 'running':
                    disabled
%   end
                >start</button>

                <button class="w3-btn"
                    onclick="dockmanStop('{{srv.name}}')"
%   if status != 'running':
                    disabled
%   end
                >stop</button>
            </p>
        </div>
    </div>
</div>
% end
<!-- dockman modals -->
