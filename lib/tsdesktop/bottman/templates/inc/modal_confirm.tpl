<!-- modal_confirm START -->
<div id="modalConfirm" class="w3-modal">
    <div class="w3-modal-content w3-card-8">
        <div class="w3-container w3-border">
            <p class="w3-theme-dark w3-tiny w3-center">!</p>
            <p id="modalConfirm-message"></p>
            % include('inc/modal_progressbar.tpl')
            <!-- confirm buttons -->
            <p
                id="modalConfirm-buttons"
                style="dispaly:block"
                class="w3-center"
            >
                <button class="w3-btn" onclick="confirmCallback()">ok</button>
                -
                <button class="w3-btn" onclick="modalHide('modalConfirm')">cancel</button>
            </p>
        </div>
    </div>
</div>
<!-- modal_confirm END -->
