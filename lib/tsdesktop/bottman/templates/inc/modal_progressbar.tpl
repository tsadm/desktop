<!-- modal_progressbar -->
<div
    id="prgrsBar-container"
    class="w3-progress-container w3-round-large w3-tiny"
    style="display:none"
>
    <div
        id="prgrsBar"
        class="w3-progressbar w3-blue w3-round-large w3-padding-tiny"
        style="width:0"
    ></div>
</div>
<!-- close button -->
<p
    id="prgrsBar-close"
    style="display:none"
    class="w3-center"
>
    <button
        class="w3-btn"
        onclick="stopPrgrsBar(); modalHide('modalConfirm')"
    >close</button>
</p>
<!-- modal_progressbar -->
