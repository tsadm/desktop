<!-- dockman status -->
<div class="w3-container w3-tiny w3-wide w3-padding-0">
%for srv in dockmanServices:
    <button
        class="w3-btn w3-round-xxlarge w3-grey"
        onclick="dockmanShow('dockman_{{srv['name']}}')"
    >{{srv['name']}}</button>
%end
</div>
<!-- dockman status -->
