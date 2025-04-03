<script>
  let listdata = [];
  let loading;

  fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      //.then((results)=>listdata=results)
      .then((results) => {
          listdata = results;
          console.log(listdata);
          loading = false;
      });
</script>

<table class="table table-striped table-hover">
  <thead>
      <tr id="encabezado">
          <th>#</th>
          <th>Nombre</th>
          <th>Usuario</th>
          <th>Ciudad</th>
          <th>Email</th>
      </tr>
  </thead>
</table>
<table>
  <tbody>
    <tr>
      <td>1</td>
      <td>John Doe</td>
      <td>johndoe</td>
      <td>New York</td>
      <td>john.doe@example.com</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jane Smith</td>
      <td>janesmith</td>
      <td>London</td>
      <td>jane.smith@example.com</td>
    </tr>
    </tbody>
</table>

<style>
  #encabezado {
    color: darkblue;
    background-color: rgb(23, 233, 93);
  }
</style>