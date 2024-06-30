<template>
    <details>
        <summary>
            <button class="title" @click="selectTask(task)">{{ task.title }}</button>
        </summary>
        <ul>
            <li v-for="subtask in subtasks" :key="subtask.id">
                <TaskPreview :task="subtask" @selectTask="selectTask" @selectTaskForm="selectTaskForm"/>
            </li>
            <li>
                <button class="add-task" @click="selectTaskForm(this.task)">Добавить подзадачу</button>
            </li>
        </ul>
    </details>
</template>

<script>
export default {

    name: 'TaskPreview',
    props: {
        task: {
            type: Object
        }
    },
    data() {
        return {
            subtasks: this.task.subtasks,
        }
    },

    methods: {
        selectTask(task) {
            this.$emit('selectTask', task)
        },
        selectTaskForm(task) {
            this.$emit('selectTaskForm', task)
        }
    }
}
</script>

<style scoped>
.title {
    font-weight: 500;
    font-family: 'Roboto', sans-serif;
    margin-left: 15px;
    margin-top: 10px;
    padding: 0;
    border: none;
    font: inherit;
    color: inherit;
    background-color: transparent;

    display: flex;

    cursor: pointer;
}

.add-task {
    margin-left: 15px;
    margin-top: 10px;
    cursor: pointer;
    padding: 0;
    border: none;
    font: inherit;
    color: inherit;
    background-color: transparent;
    display: flex;
    cursor: pointer;
}
</style>