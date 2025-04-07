<template>
  <div>
    <h1>Grist + n8n + CrewAI Dashboard</h1>
    <RecordsTable />
  </div>
</template>

<script>
import RecordsTable from './components/RecordsTable.vue';

export default {
  components: {
    RecordsTable,
  },
};
</script>

<style>
h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>
