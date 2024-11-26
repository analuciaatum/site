document.querySelectorAll(".delete").forEach((button) => {
  button.addEventListener("click", async function (event) {
    event.preventDefault();
    const confirmDelete = confirm(
      "Tem certeza que deseja excluir este agendamento?"
    );
    if (confirmDelete) {
      const form = this.closest("form");
      const response = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
      });
      if (response.ok) {
        form.closest("tr").remove(); // Remove a linha correspondente
      } else {
        alert("Erro ao excluir agendamento.");
      }
    }
  });
});
