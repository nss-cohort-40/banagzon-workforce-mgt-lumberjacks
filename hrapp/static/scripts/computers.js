const showDeleteDialog = () => {
    const deleteDialogMessage = document.getElementById('delete-dialog-message');
    const deleteDialog = document.getElementById('delete-dialog');
    deleteDialogMessage.innerHTML = "Are you sure you want to delete this computer?";
    deleteDialog.show();
}

const closeDeleteDialog = () => {
    const deleteDialog = document.getElementById('delete-dialog');
    deleteDialog.close();
}

const init = () => {
    document.getElementById('delete-prompt-button').addEventListener('click', showDeleteDialog);
    document.getElementById('cancel-delete-button').addEventListener('click', closeDeleteDialog);
}

init()


