function notification(message, type){
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
      })

      Toast.fire({
        icon: type,
        title: message
      })
}

function confirmDelete(title, description, success_text, url, item_id){
  Swal.fire({
    title: title,
    text: description,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, Eliminar'
  }).then((result) => {
    if (result.isConfirmed) {
      const urlAjax = `${url}/${item_id}`;
      const success = deleteReport(urlAjax, success_text);
      return success
    }
  })
}
