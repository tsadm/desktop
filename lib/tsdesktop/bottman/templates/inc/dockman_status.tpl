<!-- dockman status -->
<div class="w3-container w3-tiny w3-wide w3-padding-0">
%for srv in dockmanServices:
    %if not srv.dedicated:
        <%
            if srv.status() == 'running':
                btnColor='w3-green'
            elif srv.status() == 'error':
                btnColor='w3-red'
            else:
                btnColor='w3-grey'
            end
        %>
            <button
                class="w3-btn w3-round-xxlarge {{btnColor}}"
                onclick="dockmanShow('dockman_{{srv.name}}')"
            >{{srv.name}}</button>
    %end
%end
</div>
<!-- dockman status -->
