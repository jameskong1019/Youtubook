var video_id = document.getElementById('video_id').getAttribute('value');

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('YouTube-player', {
        height: '100%',
        width: '100%',
        origin: 'http://localhost:8000',
        videoId: video_id,
        playerVars: {
            'enablejsapi': 1,
            'playsinline': 1,
            'autoplay': 1,
            'controls': 1,
            'rel': 0,
            'showinfo': 0,
            'showsearch': 0,
            'mute': 0,
            'modestbranding': 1,
            'disablekb': 1,
            'loop': 1,
            'origin': window.location.href,
            'cc_load_policy' : 1,
        },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    player.playVideo();
    var test = document.getElementById('YouTube-player').contentWindow.document;
    $("iframe").contents().find("head").append("<style>.ytp-pause-overlay{display: none !important;}</style>");  
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
    // setTimeout(function () {
    //     player.pauseVideo();
    //     $(".ytp-button.ytp-collapse").ready(function() {
    //         setTimeout(function () {
    //             $(".ytp-button.ytp-collapse").click();
    //         }, 100);
    //     });
    // }, 100);
    return false;
}