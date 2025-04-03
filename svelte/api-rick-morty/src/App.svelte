<script>
  import Cards from './lib/Cards.svelte';

  let caracteres = [];
  let pagina = 1;

  async function loadCharacters() {
    const response = await fetch(`https://rickandmortyapi.com/api/character?page=${pagina}`);
    const data = await response.json();
    console.log(data);
    caracteres = data.results;
  }

  loadCharacters();

  function siguiente() {
    pagina++;
    loadCharacters();
  }

  function anterior() {
    pagina--;
    loadCharacters();
  }
</script>

<h1 class="title">Rick and Morty Svelte</h1>
<h2 class="title">Pagina: {pagina}</h2>

<div class="contenedor">
  <div class="botones">
    <button class="boton" on:click={anterior} disabled={pagina === 1}>Anterior</button>
    <button class="boton" on:click={siguiente}>Siguiente</button>
  </div>
  <div class="grid">
    {#each caracteres as caracter}
      <Cards {caracter} />
    {/each}
  </div>
</div> 