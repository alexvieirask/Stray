$(function () {
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");
  const JWT = sessionStorage.getItem("JWT");

  if (JWT) {
    alert("user is already logged in");
    redirectToHome();
  } else {
    $(".form-container").show();
    $("#form-new-user").validate({
      rules: {
        name: {
          required: true,
          minlength: 4,
        },
        username: {
          required: true,
          rangelength: [4, 30],
        },
        email: {
          required: true,
          email: true,
        },
        password: {
          required: true,
          minlength: 8,
        },
        passwordconfirm: {
          required: true,
          equalTo: "#input_password",
        },
      },
      submitHandler: onSubmit,
    });

    function onSubmit() {
      const formData = JSON.stringify({
        name: $("#input_name").val(),
        username: $("#input_username").val(),
        email: $("#input_username").val(),
        password: $("#input_password").val(),
      });

      $.ajax({
        url: `http://${ENDERECO_IP}:5000/join/auth`,
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: formData,
        success: onSuccess,
        error: onError,
      });

      function onSuccess(response) {
        $("#form-new-user").each(function () {
          this.reset();
        });

        $.ajax({
          url: `http://${ENDERECO_IP}:5000/login/auth`,
          type: "POST",
          dataType: "json",
          contentType: "application/json",
          data: formData,
          success: onSuccess,
          error: onError,
        });

        function onSuccess(response) {
          if (response.result == "ok") {
            sessionStorage.setItem("JWT", response.details);
            sessionStorage.setItem("username", $("#input_username").val());
            redirectToHome();
          } else {
            alert(`Invalid login ${response.details}`);
          }
        }
      }

      function onError(response) {
        console.log("Error, verify backend", response);
      }
    }
  }
  function redirectToHome() {
    window.location = "/";
  }
});
