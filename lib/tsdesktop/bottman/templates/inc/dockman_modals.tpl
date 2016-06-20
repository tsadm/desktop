<!-- dockman modals -->
%for srv in dockmanServices:
<div id="dockman_{{srv.name}}" class="w3-modal">
    % status = srv.status()
    <div class="w3-modal-content w3-card-8 w3-animate-top">
        <div class="w3-container">
            <span class="w3-closebtn" onclick="modalHide('dockman_{{srv.name}}')">&times;</span>
            <h2>service: {{srv.name}}</h2>
            <hr>
            <p>
            % if status == 'running':
                <button class="w3-btn" onclick="dockmanStop('{{srv.name}}')">stop</button>
            % else:
                <button class="w3-btn" onclick="dockmanStart('{{srv.name}}')">start</button>
            % end
            </p>
        </div>
    </div>
</div>
%end
<!-- dockman modals -->
