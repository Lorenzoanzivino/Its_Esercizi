import React from 'react';
import SkillCheckbox from './SkillCheckbox';

const SkillsList = ({ skills, selectedSkills, onChangeSkill }) => {
    return (
        <div>
            {skills.map(skill => (
                <SkillCheckbox
                    key={skill.id}
                    skill={skill}
                    checked={selectedSkills.includes(skill.id)}
                    onChange={() => onChangeSkill(skill.id)}
                />
            ))}
        </div>
    );
};

export default SkillsList;