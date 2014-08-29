function shuffle(array) {
    var elementsRemaining = array.length, temp, randomIndex;
    while (elementsRemaining > 1) {
    randomIndex = Math.floor(Math.random() * elementsRemaining--);
    if (randomIndex != elementsRemaining) {
        temp = array[elementsRemaining];
        array[elementsRemaining] = array[randomIndex];
        array[randomIndex] = temp;
    }
    }
    return array;
}

$(document).ready(function() {
    
    $('#carousel[data-mixed] ul').anoSlide(
        {
        items: 3,
        speed: 500,
        prev: 'a.prev[data-prev]',
        next: 'a.next[data-next]',
        lazy: true,
        delay: 0,
        auto: 3000,
        autostop: false,
        
        onConstruct: function(instance)
        {
            shuffle(instance.slides);
        },
    });
});
     
