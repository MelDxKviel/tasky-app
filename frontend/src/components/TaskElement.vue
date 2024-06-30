<template>

    <div class="task-element">
        <div class="task-element__title item">
            <p>Название: {{ task.title }}</p>
        </div>

        <div class="task-element__description item">
            <p>Описание: {{ task.description }}</p>
        </div>

        <div class="task-element__executors item">
            <p>Исполнители: {{ task.executors }}</p>
        </div>

        <div class="task-element__complexity item">
            <p>Сложность: {{ task.complexity }}</p>
        </div>

        <div v-if="task.subtasks.length > 0" class="task-element__complexity item">
            <p>Общая сложность: {{ task.total_complexity }}</p>
        </div>

        <div class="task-element__status item">
            <p>Статус: {{ task.status }}</p>
        </div>

        <div class="task-element__creation-date item">
            <p>Дата создания: {{ new Date(task.creation_date).toLocaleString() }}</p>
        </div>

        <div class="task-element__end-date item">
            <p>Дата завершения: {{ new Date(task.end_date).toLocaleString() }}</p>
        </div>

        <div v-if="task.execution_time" class="task-element__execution-time item">
            <p>Время выполнения: {{ task.execution_time }}</p>
        </div>

        <div v-if="error" class="task-element__error item">
            <p>{{ error }}</p>
        </div>

        <div class="task-element__buttons">
            <button class="task-edit-button" @click="updateTaskForm()" title="Редактировать задачу" v-if="task.status !== 'Завершена'">
                ✏️
            </button>
            <button class="task-delete-button" @click="deleteTask()" title="Удалить задачу">
                🗑️
            </button>
        </div>
    </div>


</template>

<script>
import axios from 'axios';

export default {
    name: 'TaskElement',
    props: {
        task: {
            type: Object
        }
    },
    data() {
        return {
            error: ''
        }
    },
    watch: {
        task() {
            this.error = ''
        }
    },
    methods: {
        deleteTask() {
            axios.delete(`/api/tasks/${this.task.id}`)
                .then(
                    () => {
                        this.$emit('deleteTask', this.task.id)
                    })
                .catch(
                    (error) => {
                        this.error = error.response.data[0]
                        console.log(error.response.data)
                    })
        },
        updateTaskForm() {
            this.$emit('updateTaskForm', this.task)
        },
    }
}
</script>

<style scoped>
.task-element {
    display: flex;
    flex-direction: column;
    padding: 10px;
    font-size: 20px;
    border: 1px solid black;
    border-radius: 5px;
    background-color: #F7F4F2;
}

.task-element__error {
    color: red;
}


.item {
    margin-left: 10px;
    word-break: break-all;
}

.task-element__buttons {
    display: flex;
    margin-left: auto;
}

.task-delete-button {
    min-width: 40px;
    min-height: 40px;
    border: 1px solid black;
    border-radius: 5px;

    margin-left: 10px;

    text-align: center;
    line-height: 20px;
    cursor: pointer;

    background-color: rgb(255, 218, 218);
}

.task-delete-button:hover {
    background-color: rgb(255, 169, 169);
}

.task-delete-button:active {
    background-color: rgb(255, 193, 193);
}

.task-edit-button {
    min-width: 40px;
    min-height: 40px;
    border: 1px solid black;
    border-radius: 5px;

    margin-left: 10px;

    text-align: center;
    line-height: 20px;
    cursor: pointer;

    background-color: rgb(173, 255, 248);
}

.task-edit-button:hover {
    background-color: rgb(113, 255, 242);
}

.task-edit-button:active {
    background-color: rgb(143, 255, 238);
}
</style>