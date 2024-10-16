function uploadImage() {
    const imageInput = document.getElementById('imageInput');
    
    if (imageInput.files.length === 0) {
        alert('Please select an image to upload.');
        return;
    }

    const file = imageInput.files[0];
    const formData = new FormData();
    formData.append('image', file);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Error: ' + data.error);
        } else {
            // Display extracted text in the textarea
            document.getElementById('extractedText').value = data.extracted_text;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function convertToSpeech(){
    const extractedText = document.getElementById('extractedText').value

    if (!extractedText){
    alert("No text is available to convert.")
    return;
    }

    fetch('/convertToSpeech',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({'text': extractedText})
    })
    .then(response => response.json())
    .then(data => {
        if (data.error)
            alert ('error'+data.error);
        else {
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = data.audio_path;
            //audioPlayer.play();
        }
    })
.catch(error => {
    console.error('Error:',error)
    alert("Please convert an image first", error)
})
}
function downloadAudio(){
    const audioPlayer = document.getElementById('audioPlayer');
    const soundFile = audioPlayer.src;

    if (!soundFile){
        alert('Error. No sound available.');
        return;
    }

    const link = document.createElement('a');
    link.href = soundFile;
    link.download = 'audio.mp3';
    
    link.click();
   

}
