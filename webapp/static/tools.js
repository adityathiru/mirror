function isValidProjectName(str) { return /^\w+$/.test(str); }

function validateForm() {
  var project_name = document.forms["configurator"]["project_name"].value;
  if (project_name === "") {
    Swal.fire({
      title: 'Error!',
      text: 'project name cannot be empty',
      type: 'error',
      confirmButtonText: 'Cool'
    });
    return false;
  }

  if (!isValidProjectName(project_name)) {
        Swal.fire({
          title: 'Error!',
          text: 'project name must be alphanumeric and underscores only',
          type: 'error',
          confirmButtonText: 'Cool'
        });
        return false;

  }
  var project_path = document.forms["configurator"]["project_path"].value;
  if (project_path === "") {
    Swal.fire({
          title: 'Error!',
          text: 'project path cannot be empty',
          type: 'error',
          confirmButtonText: 'Cool'
    });
    return false;
  }
  if(!project_path.startsWith("/")) {
    Swal.fire({
          title: 'Error!',
          text: 'project path must start with "/" - i.e. absolute path',
          type: 'error',
          confirmButtonText: 'Cool'
    });
    return false;

  }
}
