<script>
document.getElementById("form-conversao").onsubmit = function(event) {
    event.preventDefault();  // Impede o envio tradicional do formulário
    
    // Captura os valores dos inputs
    const formData = new FormData(document.getElementById("form-conversao"));

    // Envia os dados para o backend via AJAX (fetch)
    fetch("{% url 'temperatura' %}", {
        method: "POST",
        headers: {
            "X-Requested-With": "XMLHttpRequest"  // Indica uma requisição AJAX
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Erro: " + data.error);
            return;
        }

        // Esconde os inputs e exibe o resultado
        document.querySelector(".conteinerform").style.display = "none"; // Esconde o formulário
        document.getElementById("resultado-texto").textContent = `O valor convertido é: ${data.valor_convertido} ${data.unidade}`;
        document.getElementById("resultado").style.display = "block";
    })
    .catch(error => console.log("Erro ao fazer a requisição:", error));
};
</script>
