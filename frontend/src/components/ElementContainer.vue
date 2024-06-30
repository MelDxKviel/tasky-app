<template lang="">
    <div>
        <component :is="component_id" :task="task" :parent="parent" ></component>
    </div>
</template>
<script>
import TaskElement from './TaskElement.vue'
import TaskCreateForm from './TaskCreateForm.vue'

export default {
    name: 'ElementContainer',
    props: {
        task: {
            type: Object
        },
        parent: {
            type: null
        },
        component_id: {
            type: String
        }
    },
    components: {
        TaskElement,
        TaskCreateForm
    }

}
</script>
<style lang="">
    
</style>