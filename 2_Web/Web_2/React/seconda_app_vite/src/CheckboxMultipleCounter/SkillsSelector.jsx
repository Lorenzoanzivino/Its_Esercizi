import React, { useState, useEffect } from 'react';
import SkillsList from './SkillsList';

const SkillsSelector = () => {
    const skills = [
        { id: 1, name: "JavaScript" },
        { id: 2, name: "React" },
        { id: 3, name: "Vue" },
        { id: 4, name: "Angular" },
        { id: 5, name: "TypeScript" },
        { id: 6, name: "Node.js" },
        { id: 7, name: "PHP" },
        { id: 8, name: "Laravel" },
        { id: 9, name: "WordPress" },
        { id: 10, name: "CSS/SASS" }
    ];

    const [selectedSkills, setSelectedSkills] = useState([]);

    const handleCheckboxChange = (id) => {
        if (selectedSkills.includes(id)) {
            setSelectedSkills(prev => prev.filter(skillId => skillId !== id));
        } else {
            setSelectedSkills(prev => [...prev, id]);
        }
    };

    useEffect(() => {
        if (selectedSkills.length > 5) {
            alert("Hai selezionato più di 5 skills!");
        }
    }, [selectedSkills]);

    const handleReset = () => {
        setSelectedSkills([]);
    };

    return (
        <div className="text-center" style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
            <h3>Seleziona le tue skills</h3>

            <SkillsList
                skills={skills}
                selectedSkills={selectedSkills}
                onChangeSkill={handleCheckboxChange}
            />

            <p style={{ color: selectedSkills.length > 5 ? "red" : "black" }}>
                Selezionate: {selectedSkills.length} / 10
            </p>

            <div>
                <h4>Riepilogo:</h4>
                <ul>
                    {selectedSkills.map(id => {
                        const skill = skills.find(s => s.id === id);
                        return <li key={id}>{skill.name}</li>;
                    })}
                </ul>
            </div>

            <button onClick={handleReset}>Reset</button>
        </div>
    );
};

export default SkillsSelector;
