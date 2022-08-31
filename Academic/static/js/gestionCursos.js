(function(){
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿Seguro de elimiar el curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();