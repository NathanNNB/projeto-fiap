/* eslint-disable react/prop-types */
import { useState } from "react";
import "./Tabs.css"; 

const Tabs = ({ tabs }) => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div>
      <div className="tabs">
        {tabs.map((tab, index) => (
          <button
            key={index}
            className={`tab-button ${activeTab === index ? "active" : ""}`}
            onClick={() => setActiveTab(index)}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div className="tab-content">{tabs[activeTab].content}</div>
    </div>
  );
};

export default Tabs;