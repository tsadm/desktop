<!-- modal_confirm -->
% setdefault('modalName', 'modalConfirm')
% setdefault('modalMessage', '')
% setdefault('destURL', '')
<div id="{{modalName}}" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container w3-border">
            <p class="w3-theme-dark w3-tiny w3-center">&nbsp;</p>
            <p>{{modalMessage}}</p>
            % include('inc/modal_progressbar.tpl')
            <!-- confirm buttons -->
            <p
                id="{{modalName}}-confirm-buttons"
                style="dispaly:block"
                class="w3-center"
            >
                <button class="w3-btn" onclick="modalCallback()">ok</button>
                -
                <button class="w3-btn" onclick="modalHide('{{modalName}}')">cancel</button>
            </p>
            <!-- close button -->
            <p
                id="{{modalName}}-prgrsBar-close"
                style="display:none"
                class="w3-center"
            >
                <button
                    class="w3-btn"
                    onclick="stopPrgrsBar('{{modalName}}'); modalHide('{{modalName}}')"
                >close</button>
            </p>
        </div>
    </div>
</div>
<!-- modal_confirm -->
