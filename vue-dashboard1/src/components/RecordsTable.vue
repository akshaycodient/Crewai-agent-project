<template>
    <div>
      <h2>Customer Issues</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Customer Name</th>
            <th>Issue Description</th>
            <th>Status</th>
            <th>Classify Issue</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="(record, index) in records.records" :key="record.id">
            <td>{{ record.id }}</td>
            <td>{{ record.fields.CustomerName}}</td>
            <td>{{ record.fields.Description }}</td>
            <td>{{ record.fields.Status}}</td>
            <td>
                <button v-if="!record.fields.classification" @click="classifyIssue(record.fields, index)">Classify</button>
                <span v-else> {{ record.fields.classification }}</span>
            </td>
            </tr>
        </tbody>
      </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      records: [],
    };
  },
  async mounted() {
    // Fetch Grist records
    // const response = await axios.get("http://127.0.0.1:5000/grist-data");
    // const response = await axios.get("/backend/grist-data");
    const response = await axios.get("/api/grist-data");
    this.records = response.data;
  },
  methods: {
    async classifyIssue(record, index) {
        const requestBody = {
        description: this.records.records[index].fields.Description
        };
    //   const response = await axios.post("http://127.0.0.1:5000/classify", requestBody);
    //   const response = await axios.post("/backend/classify", requestBody);
      const response = await axios.post("/api/classify", requestBody);
      this.records.records[index].fields.classification=response.data.category;
    },
  },
};

</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}
button {
  cursor: pointer;
  padding: 5px 10px;
}
</style>
