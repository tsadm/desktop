<!-- sites_status START -->
<script src="/static/sites.js"></script>

% if sitesAll:
    <div class="w3-container w3-tiny w3-wide w3-padding-0">

%   for site in sitesAll:
%       status = site.status()
%       if status == 'running':
%           btnColor='w3-green'
%       elif status == 'error':
%           btnColor='w3-red'
%       elif status == 'exit':
%           btnColor='w3-yellow'
%       else:
%           btnColor='w3-grey'
%       end
        <button class="w3-btn w3-round-xxlarge {{btnColor}}"
            onclick="modalShow('modal-site-actions-{{site.name}}')">
            {{site.name}} ({{status}})
        </button>
%   end

    </div>
%   include('inc/modal_site_actions.tpl')
%   include('inc/modal_confirm.tpl')
% end
<!-- sites_status END -->
