<!-- dockman modals -->
% for srv in dockmanServices:
<div id="dockman_{{srv.name}}" class="w3-modal">
    % status = srv.status()
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">
            <span class="w3-closebtn" onclick="modalHide('dockman_{{srv.name}}')">&times;</span>
            <h2>service: {{srv.name}}</h2>
            <hr class="w3-border">
            <p>
                <button class="w3-btn"
                    onclick="dockmanStart('{{srv.name}}')"
                % if status == 'running':
                    disabled
                % end
                >start</button>

                <button class="w3-btn"
                    onclick="dockmanStop('{{srv.name}}')"
                % if status != 'running':
                    disabled
                %end
                >stop</button>
            </p>
        </div>
    </div>
</div>
% end
<!-- dockman modals -->
