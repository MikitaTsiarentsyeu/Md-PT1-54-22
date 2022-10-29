let zSpacing =-1000,
    lastPost= zSpacing/5,
    $frames=document.getElementsByClassName('frame'),
    frames=Array.from($frames),
    zVal=[]

window.onscroll=function(){
    let top= document.documentElement.scrollTop,
        delta =lastPost-top
    lastPost=top
    frames.forEach(function(n,i){
        zVal.push((i*zSpacing)+zSpacing)
        zVal[i]+= delta* -5
        let frame= frames[i],
            transform=`translateZ(${zVal[i]}px)`
            opacity=zVal[i]<Math.abs(zSpacing)/1.8 ? 1 : 0
        frame.setAttribute('style',`transform: ${transform};opacity:${opacity}`)
    })
}

window.scrollTo(0,1)

// audio

let soundButton=document.querySelector('.soundbutton')
    audio=document.querySelector('.audio')

soundButton.addEventListener('click',e=>{
    soundButton.classList.toggle('paused')
    audio.paused ? audio.play():audio.pause()
})

window.onfocus=function(){
    soundButton.classList.contains('paused')?audio.pause():audio.play()
}

window.onblur=function(){
    audio.pause()
}




