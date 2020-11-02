document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#book').addEventListener('click', load_booking);
    load_hike('booking-view');
});

function load_hike() {
    document.querySelector('#booking-view').style.display = 'none';
    document.querySelector('#map-view').style.display = 'block';
    document.querySelector('#comments-view').style.display ='block';
}

function load_booking(){
    document.querySelector('#booking-view').style.display = 'block';
    document.querySelector('#map-view').style.display = 'none';
    document.querySelector('#comments-view').style.display ='none';
}

function load_books() {
    document.querySelector('#booking-view').style.display = 'none';
    document.querySelector('#map-view').style.display = 'none';
    document.querySelector('#comments-view').style.display ='none';
 }