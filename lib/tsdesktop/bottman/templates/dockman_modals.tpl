<!-- dockman modals -->
%for srv in dockmanServices:
<div id="dockman_{{srv.name}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container">
            <span class="w3-closebtn" onclick="dockmanHide('dockman_{{srv.name}}')">&times;</span>
            <p><b>{{srv.name}}</b></p>
            <hr>
            <p>
                <a href="#service-start">start</a>
            </p>
        </div>
    </div>
</div>
%end
<!-- dockman modals -->
