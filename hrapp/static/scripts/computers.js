const deleteDialog = document.getElementById('delete-dialog');
const deleteDialogMessage = document.getElementById('delete-dialog-message');


const showDeleteDialog = () => {
    deleteDialogMessage.innerHTML = "Are you sure you want to delete this computer?";
    deleteDialog.show();
}

const closeDeleteDialog = () => {
    deleteDialog.close();
}

document.getElementById('delete-prompt-button').addEventListener('click', showDeleteDialog);
document.getElementById('cancel-delete-button').addEventListener('click', closeDeleteDialog);
