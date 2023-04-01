var symbols = document.querySelectorAll('.symbol');
var descs = document.querySelectorAll('.desc');

function toggleDescription() {
    var desc = this.nextElementSibling;
    if (desc.style.display === 'block') {
        desc.style.display = 'none';
    } else {
        desc.style.display = 'block';
        desc.style.fontStyle='italic'
    }
}

for (var i = 0; i < symbols.length; i++) {
    symbols[i].addEventListener('click', toggleDescription);
}