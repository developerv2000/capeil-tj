// Home page carousel
if (document.querySelector('.home-glide')) {
    let homeCarousel = new Glide('.home-glide', {
        type: 'carousel',
        gap: 0,
        hoverpause: false,
        // autoplay: 6000,
    }).mount();
}
