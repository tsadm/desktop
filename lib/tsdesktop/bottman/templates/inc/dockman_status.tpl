<!-- dockman status START -->
<script src="/static/dockman.js"></script>
<br>
<div class="w3-container w3-tiny w3-wide w3-padding-0">
%for srv in dockmanServices:
    %if not srv.dedicated:
        <%
            if srv.status() == 'running':
                btnColor='w3-green'
            elif srv.status() == 'error':
                btnColor='w3-red'
            elif srv.status() == 'exit':
                btnColor='w3-yellow'
            else:
                btnColor='w3-grey'
            end
        %>
            <button
                class="w3-btn w3-round-xxlarge {{btnColor}}"
                onclick="modalShow('dockman_{{srv.name}}')"
            >{{srv.name}}</button>
    %end
%end
</div>
%include('inc/dockman_modals.tpl')
%include('inc/modal_confirm.tpl')
<!-- dockman status END -->
