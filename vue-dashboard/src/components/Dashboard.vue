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
http://127.0.0.1:5000/grist-data");
    // const response = await axios.get("/backend/grist-data");
    const response = await axios.get("/api/grist-data");
    this.records = response.data;
  },
  methods: {
    async classifyIssue(record, index) {
        const requestBody = {
        description: this.records.records[index].fields.Description
        };
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
