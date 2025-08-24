import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import AddCard from "./components/AddCard";
import Budgeting from "./components/Budgeting";
import GoalsBills from "./components/GoalsBills";
import Chatbot from "./components/Chatbot";
import Courses from "./components/Courses";
import Badges from "./components/Badges";

function App() {
  const [activeSection, setActiveSection] = useState("goalsBills");

  return (
    <div style={{ display: "flex", height: "100vh", fontFamily: "Inter, sans-serif" }}>
      <Sidebar setActiveSection={setActiveSection} />
      <div style={{ flexGrow: 1, padding: "20px", overflowY: "auto" }}>
        {activeSection === "addCard" && <AddCard />}
        {activeSection === "Budgeting" && <Budgeting />}
        {activeSection === "goalsBills" && <GoalsBills />}
        {activeSection === "chatbot" && <Chatbot />}
        {activeSection === "courses" && <Courses />}
        {activeSection === "badges" && <Badges />}
      </div>
    </div>
  );
}

export default App;
