$(document).ready(function () {
    $('#dtPathgenindex').DataTable({
      "pagingType": "simple", // "simple" option for 'Previous' and 'Next' buttons only
      "paging": true
    });
    $('.dataTables_length').addClass('bs-select');

 
  });

  $(document).ready(function() {
    $('#dtPathgenupdate').DataTable({
      "paging": true
    });
} );