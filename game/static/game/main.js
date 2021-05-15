
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

function selectPlayer (el){
    document.getElementById("QB_name").value = el.getAttribute("data-player-name");
}

function selectRb (el){
    document.getElementById("RB_name").value = el.getAttribute("data-player-name");
}

function selectWr (el){
    document.getElementById("WR_name").value = el.getAttribute("data-player-name");
}

function selectTe (el){
    document.getElementById("TE_name").value = el.getAttribute("data-player-name");
}

function selectK (el){
    document.getElementById("K_name").value = el.getAttribute("data-player-name");
}



