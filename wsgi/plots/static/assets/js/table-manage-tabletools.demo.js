/*   
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 3.3.5
Version: 1.8.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin-v1.8/admin/
*/

var handleDataTableTools = function() {
	"use strict";
    
    if ($('#data-table').length !== 0) {
        $('#data-table').DataTable({
            dom: 'T<"clear">lfrtip',
            tableTools: {
                "sSwfPath": "assets/plugins/DataTables/swf/copy_csv_xls_pdf.swf"
            }
        });
    }
};

var TableManageTableTools = function () {
	"use strict";
    return {
        //main function
        init: function () {
            handleDataTableTools();
        }
    };
}();