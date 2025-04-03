<script>
  // Importamos el componente parImpar.svelte y lo llamamos ParImpar
  import ParImpar from './parImpar.svelte';

  let valor = 0;

  // Escuchamos el evento `input`
  const listenInput = (event) => valor = event.target.value;
</script>

<main>
  <!-- Llamamos el componente que inicialmente procesa el valor de 0 -->
  <ParImpar numero={valor}/>

  <!-- En el elemento input se coloca en value la variable valor que vale 0 -->
  <!-- También se llama el evento on:input para que reaccione al ingresar los números -->
  <input value={valor} on:input={listenInput}>
</main>
