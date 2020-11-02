
document.addEventListener('DOMContentLoaded', function() {
  load_booking_list();
});

function load_booking_list() {
  document.querySelector("#list-view").style.display = "block";

fetch(`http://127.0.0.1:8000/api`)
  .then((response) => response.json())
  .then((bookings) => {
    bookings.forEach((element) => {
      var single_book = document.createElement("div");
      single_book.className = `card mt-2`;
      single_book.innerHTML = `<div class="card-header"><b>Booking confirmation  Nº:${element.book_number}</b></div>
      <div class="card-body"> 
        <div class="row">
            <div class="col-md-4">
            <b>Booking for:</b> ${element.name } ${element.last_name }
            </div>
            <div class="col-md-4">
            <b>Hiking:</b> ${element.hike}
        </div>
          </div>
        <div class="row mt-2">
          <div class="col-md-4">
            <b>DATE you are going:</b> ${element.date}
          </div>
          <div class="col-md-4">
            <b>Phone number:</b> ${element.phone}
          </div>
        </div>
    </div>`;
      document.querySelector("#list-view").appendChild(single_book);
    });
    
  });
}
