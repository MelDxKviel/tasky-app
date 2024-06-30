<template>
    <div>
        <form class="task-create-form" @submit.prevent>

            <h1 class="title">Изменение задачи "{{ title }}"</h1>

            <div class="form-container">
                <input type="text" name="title" placeholder="Название" class="form-element" :value="updated_task.title"
                    @input="updated_task.title = $event.target.value">
                <p class="error" v-if="errors.title">{{ errors.title[0] }}</p>
            </div>

            <div class="form-container">
                <textarea name="description" placeholder="Описание" class="form-element description"
                    :value="updated_task.description" @input="updated_task.description = $event.target.value"
                    rows="4"></textarea>
                <p class="error" v-if="errors.description">{{ errors.description[0] }}</p>
            </div>

            <div class="form-container">
                <input type="text" name="executors" placeholder="Исполнители" class="form-element"
                    :value="updated_task.executors" @input="updated_task.executors = $event.target.value">
                <p class="error" v-if="errors.executors">{{ errors.executors[0] }}</p>
            </div>

            <div class="form-container">
                <input type="number" name="complexity" placeholder="Сложность" class="form-element"
                    :value="updated_task.complexity" @input="updated_task.complexity = $event.target.value">
                <p class="error" v-if="errors.complexity">{{ errors.complexity[0] }}</p>
            </div>

            <div class="form-container">
                <select name="status" class="form-element" :value="updated_task.status"
                    @input="updated_task.status = $event.target.value">
                    <option value="Назначена">Назначена</option>
                    <option value="Выполняется">Выполняется</option>
                    <option value="Приостановлена">Приостановлена</option>
                    <option value="Завершена">Завершена</option>
                </select>
                <p class="error" v-if="errors.status">{{ errors.status[0] }}</p>
            </div>

            <div class="form-container">
                <input type="datetime-local" name="end_date" placeholder="Дата завершения" class="form-element"
                    :value="updated_task.end_date" @input="updated_task.end_date = $event.target.value">
                <p class="error" v-if="errors.end_date">{{ errors.end_date[0] }}</p>
            </div>

            <button class="form-element btn" @click="updateTask">Сохранить</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'TaskUpdateForm',
    data() {
        return {
            errors: {
                title: '',
                description: '',
                executors: '',
                complexity: '',
                status: '',
                end_date: ''
            },
            updated_task: {
                title: '',
                description: '',
                executors: '',
                complexity: '',
                status: '',
                end_date: ''
            },
            title: '',
        }
    },
    props: {
        task: {
            type: Object
        }
    },
    created() {
        this.updated_task = this.task

        let utcDate = new Date(this.updated_task.end_date);

        const year = utcDate.getFullYear();
        const month = String(utcDate.getMonth() + 1).padStart(2, '0');
        const day = String(utcDate.getDate()).padStart(2, '0');
        const hours = String(utcDate.getHours()).padStart(2, '0');
        const minutes = String(utcDate.getMinutes()).padStart(2, '0');

        this.updated_task.end_date = `${year}-${month}-${day}T${hours}:${minutes}`;

        this.title = this.task.title
    },
    methods: {
        updateTask() {
            this.updated_task.end_date = new Date(this.task.end_date).toISOString()
            axios
                .put(`/api/tasks/${this.task.id}/`, this.updated_task)
                .then(response => {
                    this.$emit('updateTask', response.data)
                })
                .catch(error => {
                    this.errors = error.response.data
                    console.log(error.response.data)
                })

            this.$emit('updateTaskForm', this.updated_task)
            console.log(this.updated_task)
        }
    }
}
</script>
<style scoped>
.task-create-form {
    display: flex;
    flex-direction: column;
    border: 1px solid black;
    border-radius: 5px;
    background-color: #F7F4F2;
    padding: 10px;
}

.title {
    font-size: 30px;
    font-weight: 500;
    font-family: 'Roboto', sans-serif;
    margin-left: 10px;
}

.form-container {
    display: flex;
}

.form-element {
    margin: 10px;
    padding: 5px;
    min-height: 30px;
    min-width: 18em;
    max-width: 18em;

    border: 1px solid black;
    border-radius: 5px;
    font-size: 20px;
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
    flex: auto;

    background-color: white
}

.form-element.btn {
    background-color: #9AB168;
    cursor: pointer;
    color: white;
    line-height: 0;
}

.form-element.btn:hover {
    background-color: #9AB168;
}

.form-element.btn:active {
    background-color: r#9AB168;
}

.description {
    resize: none;
}

@media (max-width: 1000px) {
    .task-create-form {
        flex-direction: column;
        align-items: baseline;
    }

    .form-element {
        width: 100%;
        margin: 5px;
    }

    .form-container {
        flex-direction: column;
    }
}
</style>