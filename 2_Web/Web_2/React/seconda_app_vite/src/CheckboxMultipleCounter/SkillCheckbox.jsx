import React from 'react';

const SkillCheckbox = ({ skill, checked, onChange }) => {
    return (
        <div>
            <input
                type="checkbox"
                checked={checked}
                onChange={onChange}
            />
            <label>{skill.name}</label>
        </div>
    );
};

export default SkillCheckbox;