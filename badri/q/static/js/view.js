
// Initialize DataTable on document ready
$(document).ready(function() {
    $('#resultsTable').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true,
        lengthChange: true
    });
});

// Placeholder functions for exporting results
function exportToCSV() {
    alert('Export to CSV functionality will be implemented here.');
}

function exportToPDF() {
    alert('Export to PDF functionality will be implemented here.');
}
