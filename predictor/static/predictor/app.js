var $position = $('[name="position"]');  //--Find Element
var $player = $('[name="player"]');

$position.on('change', function() {
  $.ajax({
    method: 'GET',
    url: '/api/players/',
    data: { 'position': $position.val() }
  }).success(function(playerNames) {
    $player.empty();
    playerNames.forEach(function(playerName) {
      $('<option>').text(playerName).appendTo($player);  //--Create element
    });
  });
});

$('button[type=submit]').click(function() {
  var target = $(this).data('target');
  $(target).submit();
});

// function qb_rb_wr_te(name, pj){
//   this.name = name;
//   this.projection = pj;
// };
//
// var allPlayers = [];
//
// var newPlayer = new qb_rb_wr_te();
//
// $('#player-submit').on('click', function(){
//   newPlayer.name = $('.name').val();
//   newPlayer.projection = $('.projection').val();
// })

// localStorage.setItem(newPlayer.name, JSON.stringify(newPlayer));

// localStorage.setItem("name", qb_rb_wr_te.name);
// localStorage.setItem("projection", qb_rb_wr_te.projection);



// $('#player-submit').on('click', function(){
//    $('.player-information').append(
//       '<div>' +
//         '<div>' +
//           '<p class="col-xs-8">' +
//             '<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">' +
//             localStorage.getItem("name") +
//             '</button>' +
//          '</p>' +
//          '<p class="col-xs-4">PJ: '+ localStorage.getItem("projection") +'</p>'+
//         '</div>'+
//       '</div>'
//    );
// });


// var $playerNameSend = $('.btn btn-primary btn-lg');
//
// $playerNameSend.on("click", function() {
//   $.ajax({
//     method: "GET",
//     url: '/predictor/add_player/',
//     data: {'player_name': $playerNameSend.text()}
//
//   });
// });
