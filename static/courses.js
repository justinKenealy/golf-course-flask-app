// remove course button functionality
const removeCourseButton = document.getElementById('removeCourseButton')
const cancelRemove = document.getElementById('dontRemoveCourse')
const removeConfirmButtons = document.getElementById('removeConfirm')

const showConfirm = function(){
    removeCourseButton.style.display = 'none';
    removeConfirmButtons.style.display = 'block';
}

const undoRemove = function(){
    removeCourseButton.style.display = 'block';
    removeConfirmButtons.style.display = 'none';
}

removeCourseButton.addEventListener('click', showConfirm)
cancelRemove.addEventListener('click', undoRemove)