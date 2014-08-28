/**
* anoSlide - Ultra lightweight responsive slider
* 
* @version 1.0
* @author Angel Kostadinov
* @copyright Anowave
*/
(function () 
{
    var anoSlide = function(element, options) 
    {
    	this.slides   = [];
    	this.progress = false;
    	this.current  = 0;
        this.element  = $(element);
        this.options  = $.extend(
        {
			items: 		  	5,
			speed: 		  	1000,
			auto:		  	0,
			autoStop: 		true,
			next: 		  	'',
			prev: 		  	'',
			responsiveAt: 	480,
			delay: 			0,
			lazy: 			false,
			onConstruct: 	function(instance){},
			onStart: 		function(ui){},
			onEnd: 			function(ui){}
        }, options);
        
        /* Reference */
        this.defaults = 
        {
        	items: this.options.items,
        	auto: 0
        }
        
        /* Preloader */
        this.preloader = new anoPreload();
        
        this.timeout = null;
    };
 
    anoSlide.prototype = 
    {
        construct: function()
    	{
    		this.defaults.auto = this.options.auto;
    		
			this.element.css(
			{
				position: 	'relative',
				overflow: 	'hidden',
				display:	'block'
			}).children().css(
			{
				position:	'absolute',
				cursor: 	'pointer',
				overflow: 	'hidden',
				display:	'block'
			}).each(delegate(this, function(index, slide)
			{
				this.slides.push(
				{
					element: $(slide)
				})
			})).find('img').css(
			{
				float: 'left'
			})
			
			/* Responsive */
			$(window).on(
			{
				resize: delegate(this, this.adapt)
			});
					
			/* Activate next and prev controls */
			if (this.options.next)
			{
				$(this.options.next).on('click', delegate(this, this.next));
			}
			
			if (this.options.prev)
			{
				$(this.options.prev).on('click', delegate(this, this.prev));
			}
			
			if (this.options.autoStop)
			{
				this.element.parent().on(
				{
					mouseenter: delegate(this, function(element)
					{
						if (this.timeout)
						{
							clearTimeout(this.timeout);
							
							this.options.auto = 0;
						}
					}),
					mouseleave: delegate(this, function(element)
					{
						this.options.auto = this.defaults.auto;
						
						this.go(this.current);
					})
				})
			}
				
			this.options.onConstruct.apply(this,[this]);
			
			this.adapt().go(this.current);
    	},
    	preload: function(index, callback)
		{
			var queue = [];
			
			if (this.options.lazy)
			{
				for (i = index, l = index + this.options.items; i < l; i++)
				{
					if (this.slides[i].element.find('img[data-src]').length)
					{
						queue.push(
						{
							source: this.slides[i].element.find('img[data-src]').data('src')
						});
					}
				}
			}
			
			if (queue.length)
			{
				this.preloader.reset().append(queue).preload(callback);
			}
			else 
			{
				callback.apply(this,[
				{
					images:[]
				}]);
			}
		},
		animate: function(index, images, reverse)
		{	
			if (!this.progress)
			{
				this.progress = true;
				
				var viewport = 
				{
					w: this.element.parent().outerWidth(),
					h: this.element.parent().outerHeight()
				}
					
				/* On start callback */	
				this.options.onStart.apply(this,[
				{
					instance: 	this,
					index: 		index,
					slide: 		this.slides[index]
				}]);
	
				$.each((reverse ? this.slides.reverse() : this.slides), delegate(this, function(key, slide)
				{
					var offset = (reverse ? (-(index - (this.slides.length - 1 - key))) : (-(index - key))) * this.element.width()/this.options.items;
					
					/* Check for empty slides */
					if (slide.element.find('img[data-src]').length && images.length)
					{
						if (1 == this.options.items)
						{
							if (index == key)
							{
								var i = images.pop().image;
								
								slide.element.find('img[data-src]').replaceWith(i);
							}
						}
						else
						{
							var i = images.pop().image;
							
							slide.element.find('img[data-src]').replaceWith(i);
						}
					}
					
					var fn = (key == index) ? delegate(this, function()
					{ 
						this.progress = false;
						
						this.options.onEnd.apply(this,[
						{
							instance: 	this,
							index: 		this.current,
							slide: 		this.slides[this.current]
						}])
						
						if (this.options.auto)
						{
							if (this.timeout)
							{
								clearTimeout(this.timeout);
							}
							
							this.timeout = setTimeout(delegate(this, this.next), this.options.auto);
						}
						
					}) : function() {};
					
			
					slide.element.css(
					{
						width: Math.floor(this.element.outerWidth()/this.options.items) + 'px',
						height: 'auto'
					}).delay(key * this.options.delay).animate(
					{
						left: offset + 'px'
					}, this.options.speed, fn);
				}));
				
				if (reverse)
				{
					this.slides.reverse();
				}
				
				this.element.animate(
				{
					height: this.slides[index].element.outerHeight()-2
				});

				/* Toggle controls */
				var queue = this.slides.length - this.options.items - this.current;
				
				if (!queue)
				{
					this.disable.next.call(this);
				}
				else this.enable.next.call(this);
				
				if (index - 1 < 0)
				{
					this.disable.prev.call(this);
				}
				else 
				{
					this.enable.prev.call(this);
				}
			}
			
			return this;
		},
		adapt: function()
		{
			var viewport = 
			{
				w: this.element.parent().outerWidth(),
				h: this.element.parent().outerHeight()
			}
			
			if (viewport.w < this.options.responsiveAt)
			{
				this.options.items = 1;
			}
			else 
			{
				this.options.items = this.defaults.items;
			}
			
			$.each(this.slides, delegate(this, function(key, slide)
			{
				var offset = -(this.current - key) * this.element.width()/this.options.items;

				slide.element.stop().css(
				{
					width: this.element.width()/this.options.items,
					left:  offset
				}, this.options.speed, (key == this.slides.length - 1) ? delegate(this, function()
				{
					this.progress = false;
				}) : function(){})
			}));

			if (0 !== this.slides[this.current].element.parent().height())
			{

				this.element.css(
				{
					height: this.slides[this.current].element.outerHeight()-2
				})
			}

			return this;
		},
		next: function()
		{
			var queue = this.slides.length - this.options.items - this.current;
			
			if (queue)
			{
				this.go(this.current + 1);
			}
			else 
			{
				this.go(0);
			}
		},
		prev: function()
		{
			this.go(this.current - 1, true);
		},
		stop: function()
		{
			if (this.timeout)
			{
				clearTimeout(this.timeout);
			}
			
			this.progress = false;
			
			return this;
		},
		go: function(index, reverse)
		{			
			reverse = reverse || false;
			
			if (!this.progress)
			{
				if (index < 0 || index > this.slides.length - 1)
				{
					return false;
				}
				else 
				{				
					this.current = index; 
						
					this.preload(index, delegate(this, function(ui)
					{																
						this.animate(index, ui.images, reverse);
					}));
				}
			}
		},
		enable:
		{
			next: function()
			{
				$(this.options.next).removeClass('disabled').fadeIn(300);
			},
			prev: function()
			{
				$(this.options.prev).removeClass('disabled').fadeIn(300);
			}
		},
		disable: 
		{
			next: function()
			{
				$(this.options.next).addClass('disabled').fadeOut(300);
			},
			prev: function()
			{
				$(this.options.prev).addClass('disabled').fadeOut(300);
			}
		}
    }
    
    var anoPreload = function()
    {
    	this.queue  = [];
    	this.images = [];
    	this.total = 0;
    	this.config = 
		{
			cache: true
		};
			
		this.time = 
		{
			start: 0,
			end: 0   
		}
    }
    
    anoPreload.prototype = 
    {
    	onComplete: function(ui){},
		reset: function()
		{
			this.queue 	= [];
			this.images = [];
			this.total 	= 0;
			
			return this;
		},
		append: function(element)
		{
			var queue = this.queue;
			
			$.each(element, function(index, element)
			{
				queue.push(element);
			});
			
			return this;
		},
		finish: function(event, index, image)
		{
			/* Decrease number of finished items */
			this.total--;
			
			$.each(this.images, function(x,i)
			{
				if (i.index == index)
				{
					i.size = {
						width: 	image.width,
						height: image.height
					}
				}
			})

			/* Check if no more items to preload */
			if (0 == this.total)
			{
				this.time.end = new Date().getTime();
				
				this.onComplete.apply(this,[
				{
					time: 	((this.time.end - this.time.start)/1000).toPrecision(2),
					images: this.images
				}])
			}
		},
		preload: function(callback)
		{
			/* Set callback function */
			this.onComplete = callback || this.onComplete;
			
			this.time.start = new Date().getTime();
			
			/* Get queue length */
			this.total = i = this.queue.length;
			
			while(i--)
			{
				var image = new Image();

				/* Push image */
				this.images.push(
				{
					index: i,
					image: image,
					size: 
					{
						width:	0,
						height: 0
					}
				});
				
				image.onload  = image.onerror = image.onabort = delegate(this, this.finish, ([i,image]));
	
				/* Set image source */
				image.src = this.config.cache ? this.queue[i].source : (this.queue[i].source + '?u=' + (new Date().getTime()));
			}
		}
    }

	$.fn.anoSlide = function (options) 
	{
		return this.each(function () 
		{
			if (undefined == $(this).data('anoSlide')) 
			{
				var a = new anoSlide(this, options).construct();
				$(this).data('anoSlide', a);
			}
		});
	};
	
	var delegate = function(target, method, args)
	{
		return (typeof method === "function") ? function() 
		{ 
			/* Override prototype */
			arguments.push = Array.prototype.push;
			
			/* Push additional arguments */
			for (var arg in args)
			{
				arguments.push(args[arg]);
			}
			return method.apply(target, arguments); 
		} : function()
		{
			return false;
		};
	}
})();
