<template>
    <div>
        <form class="task-create-form" @submit.prevent>
            
            <h1 v-if="parent" class="title">Создание подзадачи для "{{ parent.title }}""</h1>
            <h1 v-else class="title">Создание задачи</h1>

            <div class="form-container">
                <input type="text" name="title" placeholder="Название" class="form-element" v-model="task.title">
                <p class="error" v-if="errors.title">{{ errors.title[0] }}</p>
            </div>

            <div class="form-container">
                <textarea name="description" placeholder="Описание" class="form-element description"
                    v-model="task.description" rows="4"></textarea>
                <p class="error" v-if="errors.description">{{ errors.description[0] }}</p>
            </div>

            <div class="form-container">
                <input type="text" name="executors" placeholder="Исполнители" class="form-element"
                    v-model="task.executors">
                <p class="error" v-if="errors.executors">{{ errors.executors[0] }}</p>
            </div>

            <div class="form-container">
                <input type="number" name="complexity" placeholder="Сложность" class="form-element"
                    v-model="task.complexity">
                <p class="error" v-if="errors.complexity">{{ errors.complexity[0] }}</p>
            </div>

            <div class="form-container">
                <input type="datetime-local" name="end_date" placeholder="Дата завершения" class="form-element"
                    v-model="task.end_date">
                <p class="error" v-if="errors.end_date">{{ errors.end_date[0] }}</p>
            </div>

            <button class="form-element btn" @click="createTask">Добавить задачу</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'TaskCreateForm',
    data() {
        return {
            task: {
                title: '',
                description: '',
                executors: '',
                complexity: '',
                end_date: ''
            },
            errors: {
                title: '',
                description: '',
                executors: '',
                complexity: '',
                end_date: ''
            }
        }
    },
    props: {
        parent: {
            type: Object
        }
    },
    methods: {
        createTask() {
            console.log(this.task)
            if (this.parent) {
                this.task.parent = this.parent.id
            }
            if (this.task.end_date) {
                this.task.end_date = new Date(this.task.end_date).toISOString()
            } 
            axios.post('http://127.0.0.1:8000/api/tasks/', this.task)
                .then(response => {
                    this.$emit('createTask', response.data, this.parent)
                })
                .catch(error => {
                    this.errors.title = error.response.data.title
                    this.errors.description = error.response.data.description
                    this.errors.executors = error.response.data.executors
                    this.errors.complexity = error.response.data.complexity
                    this.errors.end_date = error.response.data.end_date
                })
                .finally(() => {
                    this.task.title = ''
                    this.task.description = ''
                    this.task.executors = ''
                    this.task.complexity = ''
                    this.task.end_date = ''
                })
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