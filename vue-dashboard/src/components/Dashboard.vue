<template>
  <div>
    <h2>Support Issues</h2>
    <table>
      <thead>
        <tr>
          <th>Customer</th>
          <th>Description</th>
          <th>Status</th>
          <th>Category</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(record, index) in issues" :key="index">
          <td>{{ record.fields['Customer Name'] }}</td>
          <td>{{ record.fields['Issue Description'] }}</td>
          <td>{{ record.fields['Status'] }}</td>
          <td>{{ record.category || '-' }}</td>
          <td>
            <button @click="classifyIssue(record)">Classify</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
 
<script setup>
import { ref, onMounted } from 'vue'
 
const issues = ref([])
 
const fetchIssues = async () => {
const res = await fetch('http://localhost:5000/grist-data')
  const json = await res.json()
  issues.value = json.records
}
 
const classifyIssue = async (issue) => {
const res = await fetch('http://localhost:5000/classify', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ description: issue.fields['Issue Description'] })
  })
  const json = await res.json()
  issue.category = json.category
}
 
onMounted(fetchIssues)
</script>