<!-- modal_confirm -->
% setdefault('modalName', 'modalConfirm')
% setdefault('modalMessage', '')
% setdefault('destURL', '')
<div id="{{modalName}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container w3-border">
            <p class="w3-yellow w3-tiny w3-center w3-border">&nbsp;</p>
            <p>{{modalMessage}}</p>
            <p class="w3-center">
                <a href="{{destURL}}">OK</a>
                - <a href="" onclick="modalHide('{{modalName}}')">Cancel</a>
            </p>
        </div>
    </div>
</div>
<!-- modal_confirm -->
