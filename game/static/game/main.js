
function handleShowPage(evt) {
function showPage(page) {
    document.querySelectorAll('tbody').forEach(tbody => {tbody.style.display = 'none';})

    document.querySelector(`#${page}`).style.display = 'table-row-group';

}
showPage(evt.currentTarget.dataset.page);

}
document.addEventListener('DOMContentLoaded', function() {
document
    .querySelectorAll('button[data-page]')
    .forEach(button =>
    button.addEventListener('click', handleShowPage)
    );
});


function myFunction(txt) {
    var myTxt = txt;
    
    if (txt.includes('QB')) {
        document.getElementById("QB_name").value = myTxt;
    }

    else if (txt.includes('RB')) {
        document.getElementById("RB_name").value = myTxt;
    }

    else if (txt.includes('WR')) {
        document.getElementById("WR_name").value = myTxt;
    }

    else if (txt.includes('TE')) {
        document.getElementById("TE_name").value = myTxt;
    }

    else if (txt.includes('K')) {
        document.getElementById("K_name").value = myTxt;
    }

    
    
}


