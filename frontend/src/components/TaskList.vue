<template lang="">
  <ul class="tree">
    <li>
    <details open>
      <summary style="margin-left: 10px">Задачи</summary>
      <ul>
        <li v-for="task in tasks" :key="task.id" >
          <TaskPreview :task="task" @selectTaskForm="selectTaskForm" @selectTask="selectTask"/>
        </li>
        <li>
          <div class="add-task" @click = "this.$emit('selectTaskForm')">Добавить задачу</div>
        </li>
      </ul>
    </details>
  </li>
  </ul>
</template>

<script>
import TaskPreview from './TaskPreview.vue'
export default {
  name: 'TaskList',
  components: {
    TaskPreview
  },
  props: {
    tasks: {
      type: Array
    }
  },
  methods: {
    selectTaskForm(parent_id) {
      this.$emit('selectTaskForm', parent_id)
    },
    selectTask(task) {
      this.$emit('selectTask', task)
    }
  }
}
</script>

<style>
.add-task {
  margin-left: 15px;
  margin-top: 10px;
  cursor: pointer;
}

.tree {
  --spacing: 1.5rem;
  --radius: 11px;
  margin-left: -40px;
}


.tree li {
  display: block;
  position: relative;
  padding-left: calc(2 * var(--spacing) - var(--radius) - 2px);
  font-size: 20px;
}

.tree ul {
  margin-left: calc(var(--radius) - var(--spacing));
  padding-left: 0;
}

.tree ul li {
  border-left: 2px solid #ddd;
}

.tree ul li:last-child {
  border-color: transparent;
}

.tree ul li::before {
  content: '';
  display: block;
  position: absolute;
  top: calc(var(--spacing) / -2);
  left: -2px;
  width: calc(var(--spacing) + 2px);
  height: calc(var(--spacing) + 1px);
  border: solid #ddd;
  border-width: 0 0 2px 2px;
}

.tree summary {
  display: block;
  cursor: pointer;
}

.tree summary::marker,
.tree summary::-webkit-details-marker {
  display: none;
}

.tree summary:focus {
  outline: none;
}

.tree summary:focus-visible {
  outline: 1px dotted #000;
}

.tree li::after,
.tree summary::before {
  content: '';
  display: block;
  position: absolute;
  top: calc(var(--spacing) / 2 - var(--radius));
  left: calc(var(--spacing) - var(--radius) - 1px);
  width: calc(2 * var(--radius));
  height: calc(2 * var(--radius));
  border-radius: 50%;
  background: #ddd;
}

.tree summary::before {
  content: '+';
  z-index: 1;
  background: #9AB168;
  color: #fff;
  line-height: calc(2 * var(--radius) - 2px);
  text-align: center;
}

.tree details[open]>summary::before {
  content: '−';
}

.add-task {
  margin-left: 15px;
  margin-top: 10px;
}
</style>
