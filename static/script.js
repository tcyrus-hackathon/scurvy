	<script>
    var jumboHeight = $('.jumbotron').outerHeight();
		function parallax(){
    	var scrolled = $(window).scrollTop();
    	$('.bg').css('height', (jumboHeight-scrolled) + 'px');
		}

	$(window).scroll(function(e){
    parallax();
	});

	</script>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script> 
 
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <script>
      $('.dropdown').on('show.bs.dropdown', function(e){
    	$(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  		});

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  	$('.dropdown').on('hide.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
  	});

  	</script>