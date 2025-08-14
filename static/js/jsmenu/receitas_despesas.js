// static/jsmenu/receitas_despesas.js
document.addEventListener("DOMContentLoaded", function () {
  const tipoContaSelect = document.getElementById("id_tipo_conta");
  const metodoPagamentoSelect = document.getElementById("id_metodo_pagamento");
  const tipoReceitaDiv = document.getElementById("bloco_tipo_receita");
  const metodoPagamentoDiv = document.getElementById("bloco_metodo_pagamento");
  const parcelasDiv = document.getElementById("bloco_parcelas");
  const totalParcelasInput = document.getElementById("id_total_parcelas");
  const valorParcelaInput = document.getElementById("id_valor_parcela");
  const valorInput = document.getElementById("id_valor");

  function atualizarCampos() {
    const tipo = tipoContaSelect.value;
    const metodo = metodoPagamentoSelect.value;

    // Oculta tudo inicialmente
    tipoReceitaDiv.classList.add("hidden");
    metodoPagamentoDiv.classList.add("hidden");
    parcelasDiv.classList.add("hidden");

    if (tipo === "receita") {
      tipoReceitaDiv.classList.remove("hidden");
    } else if (tipo === "despesa") {
      metodoPagamentoDiv.classList.remove("hidden");

      if (metodo === "Crédito") {
        parcelasDiv.classList.remove("hidden");
      } else {
        // Se não for crédito, parcelas fica 1 e valor parcela = valor total
        totalParcelasInput.value = 1;
        parcelasDiv.classList.add("hidden");
        valorParcelaInput.value = valorInput.value || "";
      }
    }
  }

  // Atualiza o valor da parcela sempre que valor ou total de parcelas mudar
  function atualizarValorParcela() {
    const total = parseFloat(valorInput.value) || 0;
    const parcelas = parseInt(totalParcelasInput.value) || 1;
    valorParcelaInput.value = (total / parcelas).toFixed(2);
  }

  tipoContaSelect.addEventListener("change", () => {
    atualizarCampos();
    atualizarValorParcela();
  });

  metodoPagamentoSelect.addEventListener("change", () => {
    atualizarCampos();
    atualizarValorParcela();
  });

  valorInput.addEventListener("input", atualizarValorParcela);
  totalParcelasInput.addEventListener("input", atualizarValorParcela);

  // Inicializa no carregamento
  atualizarCampos();
  atualizarValorParcela();
});
