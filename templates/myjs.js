function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie("csrftoken");

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!/^http:.*/.test(settings.url) && !/^https:.*/.test(settings.url)) {
      // Only send the token to relative URLs i.e. locally.
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  },
});
// Function to fetch and display employee list
function loadEmployeeList() {
  $.ajax({
    url: "{% url 'get_employee_list' %}",
    method: "POST",
    success: function (response) {
      if (response.status === "success") {
        let employees = response.employees;
        let employeeHtml = "<ul>";
        employees.forEach((emp) => {
          employeeHtml += `
    <tr>
        <td>${emp.name}</td>
        <td>${emp.email}</td>
        <td>${emp.phone_no}</td>
        <td>${emp.age}</td>
        <td>${emp.gender}</td>
        <td class="action-buttons">
            <button class="edit-button" onclick="editEmployee(${emp.id})">Edit</button>
            <button class="delete-button" onclick="deleteEmployee(${emp.id})">Delete</button>
        </td>
    </tr>
`;
        });
        employeeHtml += "</ul>";
        $("#employeeList").html(employeeHtml);
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to load employee list.");
    },
  });
}

// Create Employee with Ajax
$("#createEmployeeForm").on("submit", function (e) {
  e.preventDefault();
  $.ajax({
    url: "{% url 'add_an_employee' %}",
    method: "POST",
    data: $(this).serialize(),
    success: function (response) {
      if (response.status === "success") {
        loadEmployeeList();
        alert(response.message);
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to create employee.");
    },
  });
});

// Update Employee (implement similarly to Create Employee)
function editEmployee(id) {
  // Fetch employee details using AJAX
  $.ajax({
    url: `/get-employee/${id}/`, // Ensure this URL is mapped in your Django urls.py
    method: "GET",
    success: function (response) {
      if (response.status === "success") {
        let employee = response.employee;
        // Populate the form fields with the employee's data
        $("#editEmployeeId").val(employee.id);
        $("#editname").val(employee.name);
        $("#editEmail").val(employee.email);
        $("#editage").val(employee.age);
        $("#editphone").val(employee.phone_no);

        $("#editgennder").val(employee.gennder);

        // Show the edit form
        $("#editEmployeeForm").show();
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to fetch employee details.");
    },
  });
}

// Update Employee with Ajax
$("#editEmployeeForm").on("submit", function (e) {
  e.preventDefault();
  $.ajax({
    url: `/update_employee/${$("#editEmployeeId").val()}`, // Ensure this URL is mapped in your Django urls.py
    method: "POST",
    data: $(this).serialize(),
    success: function (response) {
      if (response.status === "success") {
        loadEmployeeList();
        alert(response.message);
        $("#editEmployeeForm").hide(); // Hide the form after successful update
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to update employee.");
    },
  });
});

// Delete Employee with Ajax
function deleteEmployee(id) {
  $.ajax({
    url: `/delete_an_employee/${id}`,
    method: "POST",
    success: function (response) {
      if (response.status === "success") {
        loadEmployeeList();
        alert(response.message);
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to delete employee.");
    },
  });
}

// Load employee list on page load
$(document).ready(function () {
  loadEmployeeList();
});

function showCreateForm() {
  document.getElementById("createEmployeeForm").style.display = "block";
  document.getElementById("editEmployeeForm").style.display = "none";
}

// Function to show the edit form and hide the create form
function editEmployee(id) {
  // Fetch employee details and populate the edit form
  $.ajax({
    url: `/get-employee/${id}/`,
    method: "GET",
    success: function (response) {
      if (response.status === "success") {
        let employee = response.employee;
        $("#editEmployeeId").val(employee.id);
        $("#editname").val(employee.name);
        $("#editEmail").val(employee.email);
        $("#editage").val(employee.age);
        $("#editphone").val(employee.phone_no);

        $("#editgennder").val(employee.gennder);

        // Show the edit form and hide the create form
        document.getElementById("editEmployeeForm").style.display = "block";
        document.getElementById("createEmployeeForm").style.display = "none";
      } else {
        alert(response.message);
      }
    },
    error: function () {
      alert("Failed to fetch employee details.");
    },
  });
}
