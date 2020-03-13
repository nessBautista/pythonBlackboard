import React from "react";
import "./App.css";
import "antd/dist/antd.css";
import CustomLayout from "./containers/Layout";
import ArticleList from "./containers/ArticleListView";
function App() {
  return (
    <div className="App">
      <CustomLayout>
        <h1>This is how the app will look like!</h1>
        <ArticleList></ArticleList>
      </CustomLayout>
    </div>
  );
}

export default App;
