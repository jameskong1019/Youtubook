var video_id = document.getElementById('video_id').getAttribute('value');

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('YouTube-player', {
        height: '390',
        width: '640',
        videoId: video_id,
        playerVars: {
            cc_load_policy : 1,
            enablejsapi: 1,
            playsinline: 1,
            start: 0,
            disablekb: 0,
            controls: 0,
            showinfo: 0,
            showsearch: 0,
            iv_load_policy: 3,
            modestbranding: 1,
            fs: 0,
            rel: 1
        },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    player.playVideo();
    document.getElementsByClassName("ytp-pause-overlay ytp-scroll-min")[0].style.display = 'none';
}

var done = false;
function onPlayerStateChange(event) {

}
function stopVideo() {
    player.stopVideo();
}

function playVideo(startTime) {
    player.seekTo(startTime);
    player.playVideo();
    setTimeout(function () {
        player.pauseVideo();
    }, 100)

    return false;
}