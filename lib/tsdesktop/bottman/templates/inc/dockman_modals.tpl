<!-- dockman modals -->
%for srv in dockmanServices:
<div id="dockman_{{srv.name}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">
            <span class="w3-closebtn" onclick="modalHide('dockman_{{srv.name}}')">&times;</span>
            <p><b>{{srv.name}}</b></p>
            <hr>
            <p>
                <button class="w3-btn" onclick="dockmanStart('{{srv.name}}')">start</button>
            </p>
        </div>
    </div>
</div>
%end
<!-- dockman modals -->
