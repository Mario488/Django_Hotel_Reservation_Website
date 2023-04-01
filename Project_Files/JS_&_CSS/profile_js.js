const rooms = document.querySelector('.room-grid');
const button = document.getElementById('view_res');

const rooms_count = document.querySelectorAll('.room-card');

const toggleVisibility = () => {
    let count = 0
    for(let i = 0; i < rooms_count.length; i++){
        count += 1
    }
    if (count === 0){
        rooms.textContent = 'Нямате направени резервации';
        rooms.style.fontWeight = 'bold';
        rooms.style.fontSize = '1.4rem';
    }   
    if (rooms.style.display === 'none') {
        rooms.style.display = 'grid';
    } else {
        rooms.style.display = 'none';
    }
};
button.addEventListener('click', toggleVisibility);

const cost = document.querySelector('.cost');
const totalCost = document.querySelector('.total-cost');

if (cost.textContent === '0.00') {
    totalCost.style.display = 'none';
}