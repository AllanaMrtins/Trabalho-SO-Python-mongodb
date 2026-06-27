// 📚 Sistema de Monitoria UFPI - Script básico

document.addEventListener("DOMContentLoaded", function () {

    console.log("Sistema UFPI carregado com sucesso 🚀");

    // =========================
    // 🔔 ALERTA DE BOAS-VINDAS
    // =========================
    const path = window.location.pathname;

    if (path === "/dashboard") {
        console.log("Você está no Dashboard 📊");
    }

    // =========================
    // 🧠 CONFIRMAÇÃO DE FORMULÁRIOS
    // =========================
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            const confirmar = confirm("Deseja realmente enviar os dados?");
            
            if (!confirmar) {
                e.preventDefault();
            }
        });
    });

    // =========================
    // ✨ HIGHLIGHT VISUAL (UX simples)
    // =========================
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "scale(1.02)";
            card.style.transition = "0.2s";
            card.style.boxShadow = "0px 4px 10px rgba(0,0,0,0.2)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "none";
        });
    });

    // =========================
    // 🔐 SIMULAÇÃO DE LOGIN
    // =========================
    const loginForm = document.querySelector(".login-box form");

    if (loginForm) {
        loginForm.addEventListener("submit", function () {
            const usuario = loginForm.querySelector("input[name='usuario']").value;

            if (usuario.trim() !== "") {
                console.log("Usuário logado:", usuario);
            }
        });
    }

});