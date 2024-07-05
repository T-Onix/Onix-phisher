(function() {
    $(document).ready(function() {
        $(".alert-close").bind("click", () => {
            $(".alert-container").fadeOut();
        })
        $(".signin-btn").bind("click", () => {
            $(".alert-container").fadeIn()
            $(".alert-container").css("display", "flex");
            document.querySelector("#inputUsername").focus();
            $(".input").val("");
        })
    });
})()