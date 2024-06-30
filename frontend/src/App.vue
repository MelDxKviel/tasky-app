<template>
  <div>
    <header class="header">
      Tasky
    </header>
    <div class="box">
      <div class="list">
        <TaskList :tasks="tasks" @selectTask="handleSelectedTask" @selectTaskForm="handleSelectTaskForm" />
      </div>
      <div class="container">
        <component :is="currentComponent" v-bind="currentProps" @deleteTask="deleteTask" @createTask="createTask"
          @updateTaskForm="handleUpdateTaskForm" @updateTask="updateTask">
        </component>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TaskList from './components/TaskList.vue'
import TaskCreateForm from './components/TaskCreateForm.vue'
import TaskElement from './components/TaskElement.vue';
import TaskUpdateForm from './components/TaskUpdateForm.vue';


export default {
  name: 'App',
  components: {
    TaskList,
    TaskCreateForm,
    TaskElement,
    TaskUpdateForm
  },
  data() {
    return {
      tasks: [],
      currentComponent: null,
      currentProps: {}
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    async getTasks() {
      await axios.get('/api/tasks/')
        .then(
          (response) => {
            this.tasks = response.data
          })
        .catch(
          (error) => {
            console.log(error)
          })
    },
    async getTaskById(id) {
      await axios.get(`/api/tasks/${id}/`)
        .then(
          (response) => {
            this.currentProps.task = response.data
          })
        .catch(
          (error) => {
            console.log(error)
          })
    },
    handleSelectedTask(task) {
      this.currentComponent = 'TaskElement'
      this.currentProps = { task }
      this.getTaskById(task.id)
    },
    handleSelectTaskForm(parent) {
      this.currentComponent = 'TaskCreateForm'
      this.currentProps = { parent }
    },
    handleUpdateTaskForm(task) {
      this.currentComponent = 'TaskUpdateForm'
      this.currentProps = { task }
    },
    deleteTask(task_id) {
      this.tasks = this.tasks.filter(task => task.id !== task_id)
      this.currentComponent = null
      this.currentProps = {}
    },
    createTask(task, parent) {
      if (!parent) {
        this.tasks.push(task)
      } else {
        parent.subtasks.push(task)
      }
      this.currentComponent = 'TaskElement'
      this.currentProps = { task }
    },
    updateTask(task) {
      this.currentComponent = 'TaskElement'
      this.getTaskById(task.id)
      this.getTasks()
    }
  }
}
</script>

<style>
.header {
  text-align: center;
  font-size: 3em;
  font-family: 'Roboto', sans-serif;
  font-weight: 300;
  color: rgb(255, 255, 255);
  background-blend-mode: screen;

  background: #9AB168;
  padding: 10px;

}

body {
  padding: 0;
  margin: 0;
  background: url('@/assets/Group.png');
  font-family: 'Roboto', sans-serif;

}

.box {
  display: flex;
  flex-direction: row;
  margin: auto;
  max-width: 1300px;
}

.list {
  display: flex;
  flex-direction: column;
  min-width: 500px;
  word-break: break-all;
}

.container {
  display: flex;
  flex: auto;
  flex-direction: column;

  margin: 10px;
}

@media (max-width: 1150px) {
  .box {
    flex-direction: column;
  }
}
</style>
