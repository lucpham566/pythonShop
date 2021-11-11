$(document).ready(function () {
  window.addEventListener("scroll", function () {
    var obj = $("header.header-menu").offset().top;
    console.log(obj);
    if (obj > 185) {
      $("header.header-menu").addClass("scroll");
      $(".addThis_listSharing").css({
        display:"block"
      })
    } else {
      $("header.header-menu").removeClass("scroll");
      $(".addThis_listSharing").css({
        display:"none"
      })
    }
  });
  $("#show-comment").click(function(){
    $(".write-comment").css({
      display:"block"
    })
  })
  $(".write-comment #close").click(function(){
    $(".write-comment").css({
      display:"none"
    })
  })
  
});

$(document).ready(function () {
  $(".carousel-banner").slick({
    infinite: true,
    dots: true,
    speed: 1000,
    autoplay: true,
    autoplaySpeed: 4000,
    fade: true,
  });

  $(".carousel-img-product").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.carousel-img-product-nav'
  });

  $('.carousel-img-product-nav').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    asNavFor: '.carousel-img-product',
    dots: true,
    focusOnSelect: true
  });

  $(".carousel-testimonier").slick({
    infinite: true,
    dots: false,
    speed: 700,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 1008,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });

  $(".carousel-special-products").slick({
    infinite: true,
    dots: false,
    speed: 700,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 1,
  });

  $(".carousel-product-hot").slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 4,
    dots:true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: true,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

  $(".carousel-news").slick({
    infinite: true,
    dots: true,
    speed: 700,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 4,
    responsive: [
      {
        breakpoint: 1008,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });

  $(".carousel-video").slick({
    infinite: true,
    dots: true,
    speed: 700,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 3,
    responsive: [
      {
       
      },
      {
        breakpoint: 1008,
      

        settings: {
          centerMode: false,
      centerPadding: '0',
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 600,

        settings: {
      centerMode: false,

          slidesToShow: 1,
        },
      },
    ],
  });

  $(".carousel-gallery").slick({
    infinite: true,
    dots: true,
    speed: 700,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 1008,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });

  $(".tab-a").click(function () {
    $(".tab").removeClass("tab-active");
    $(".tab[data-id='" + $(this).attr("data-id") + "']").addClass("tab-active");
    $(".tab-a").removeClass("active-a");
    $(this).parent().find(".tab-a").addClass("active-a");
  });

  var isSearch = false;

  $("main").on("click", function () {
    isSearch = false;
    $("header .search .content").css({
      display: "none",
    });
  });
  $(".banner-top").on("click", function () {
    isSearch = false;
    $("header .search .content").css({
      display: "none",
    });
  });
  $("header .search .btn-sch").on("click", function () {
    isSearch = !isSearch;
    if (isSearch) {
      $("header .search .content").css({
        display: "block",
      });
    } else {
      $("header .search .content").css({
        display: "none",
      });
    }
  });

  
});

function increaseValue() {
  var value = parseInt(document.getElementById("number").value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  document.getElementById("number").value = value;
}

function decreaseValue() {
  var value = parseInt(document.getElementById("number").value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? (value = 1) : "";
  value--;
  document.getElementById("number").value = value;
}

$("header .btn-search").click(function(){
  $("header .form-search").css({
    visibility:'inherit',
    opacity: 1,
    transform:'translateX(0)',
  })
})

$('.item-right .cate').click(function () {
  $("header .form-search").css({
    visibility:'hidden',
    opacity: 0,
    transform:'translateX(100%)',
  })

})

var isbox_phone = false;
var isbox_message = false;


$('.hotline-phone-ring-wrap .hotline-phone-ring-img-circle').click(function () {
  if(isbox_phone){
    $('.box-phone').css({
      visibility: 'hidden',
      opacity: 0,
  
    })
    isbox_phone = false;
    
  }
  else{
    $('.box-phone').css({
      visibility: 'visible',
      opacity: 1,
  
    })
    isbox_phone = true;
    if(isbox_message){
      $('.box-contact').css({
        visibility: 'hidden',
        opacity: 0,
    
      })
      isbox_message = false;
    }
  }
  
})

$('.hotline-phone-ring-wrap .box-phone .close-bn ').click(function () {
  if(isbox_phone){
    $('.box-phone').css({
      visibility: 'hidden',
      opacity: 0,
  
    })
    isbox_phone = false;
  }
  else{
    $('.box-phone').css({
      visibility: 'visible',
      opacity: 1,
  
    })
    isbox_phone = true;
    
  }
  
})



$('.message-ring-wrap .hotline-phone-ring-img-circle').click(function () {
  if(isbox_message){
    $('.box-contact').css({
      visibility: 'hidden',
      opacity: 0,
  
    })
    isbox_message = false;
  }
  else{
    $('.box-contact').css({
      visibility: 'visible',
      opacity: 1,
  
    })
    isbox_message = true;
    if(isbox_phone){
      $('.box-phone').css({
        visibility: 'hidden',
        opacity: 0,
    
      })
      isbox_phone = false;
    }
   
  }
  
})

$('.message-ring-wrap .box-contact .close-bn').click(function () {
  if(isbox_message){
    $('.box-contact').css({
      visibility: 'hidden',
      opacity: 0,
  
    })
    isbox_message = false;
  }
  else{
    $('.box-contact').css({
      visibility: 'visible',
      opacity: 1,
  
    })
    isbox_message = true;
  }
  
})

is_cart = false;


$('.logo-container .cart').click(function () {
  if(is_cart){
    $('.logo-container .cart .cart-dropdown').css({
      display:'none'
  
    })
    is_cart = false;
  }
  else{
    $('.logo-container .cart .cart-dropdown').css({
      display:'block'
  
    })
    is_cart = true;
  }

})


$('.logo-container .cart .close').click(function () {
    $('.logo-container .cart .cart-dropdown').css({
      display:'none'
  
    })
    is_cart = false;
  
})


// --------- menu mobile


$('.nav-item-mobile .add').click(function () {
  $('.box-sub-menu').css({
    opacity: 1,
    transform: 'translateX(0)',

  })

})

$('.box-sub-menu .back-cate').click(function () {
  $('.box-sub-menu').css({
    opacity: 0,
    transform: 'translateX(-100%)',

  })

})

