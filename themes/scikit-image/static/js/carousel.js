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
    
    $('#carousel ul').anoSlide(
        {
        items: 2,
        lazy: true,
        speed: 1000,
        auto: 4000,
        delay: 100,
        autostop: false,
        
        onConstruct: function(instance)
        {
            shuffle(instance.slides);
        },
        /* rewind should be instant */
        onStart: function(ui)
        {
            if (ui.index==0) 
            {
                ui.instance.options.speed = 0;
            }            
        },
        onEnd: function(ui)
        {
            if (ui.index==0) 
            {
                ui.instance.options.speed = 1000;
            }            
        },
    });
});
     
