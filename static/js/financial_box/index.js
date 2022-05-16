
function repotcloseModalDelete(){
    $('#deleteClient').modal('hide');
}
function reportDeleteBox(url){
    $('#deleteBox').load(url,function(){
        $(this).modal('show'); 
    });
}