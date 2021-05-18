<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div id="app">
    <Note text="Test Note Text" />
  </div>
</template>


<script>
import Note from "./components/Note.vue";
export default {
  name: 'App',
  components: {
    Note,
  },
}
</script>

<template>
  <div id="app">
    <h2>My Notes</h2>
    <div class="notes">
      <Note v-for="(note, index) in notes"
            :key="index"
            :text="note.note" />
    </div>
    <h2>Add a New Note</h2>
    <form @submit.prevent="addNote">
      <textarea v-model="newNote" placeholder="Note Content...">
      </textarea>
      <button>Add Note</button>
    </form>
  </div>
</template>


<script>
import Note from "./components/Note";
import axios from 'axios';

export default {
  name: 'App',
  components: {
    Note,
  },
  data() {
    return {
      notes: [],
      newNote: "",
    };
  },
  methods: {
    loadNotes: function() {
      axios.get('/api/notes/').then(
        response => {
          this.notes = response.data;
        }
      );
    },
    addNote: function() {
      axios.post('/api/notes/', {note: this.newNote}).then(
        response => {
          this.newNote = "";
          this.notes.push(response.data);
        }
      );
    }
  },
  created() {
    this.loadNotes();
  },
}
</script>


<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  width: 100vw;
  min-width: 300px;
  max-width: 1000px;
  margin: 0 auto;
}
.notes {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 20px;
  justify-content: center;
}
h2 {
  margin: 10px;
}
form {
  margin: 20px;
  display: flex;
  flex-direction: column;
}
form textarea {
  resize: none;
  height: 220px;
  margin: 0 10px;
  background: beige;
  outline: none !important;
  border: none;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  padding: 10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 1em;
}
form button {
  background: lightgreen;
  color: darkgreen;
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin: 10px;
  cursor: pointer;
  outline: none !important;
}
form button:hover {
  background-color: #a0fea0;
}
</style>