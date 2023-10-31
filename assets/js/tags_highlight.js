document.addEventListener('DOMContentLoaded', function() {
    function highlightSimilarTags(tagClass) {
        let tags = document.querySelectorAll('.' + tagClass);
        tags.forEach(tag => {
            tag.style.animation = 'highlight 1s infinite';
        });
    }

    function removeHighlight(tagClass) {
        let tags = document.querySelectorAll('.' + tagClass);
        tags.forEach(tag => {
            tag.style.animation = '';
        });
    }

    let panelDataTags = document.querySelectorAll('.tag-panel-data');
    panelDataTags.forEach(tag => {
        tag.addEventListener('mouseover', () => highlightSimilarTags('tag-panel-data'));
        tag.addEventListener('mouseout', () => removeHighlight('tag-panel-data'));
    });

    let healthcareTags = document.querySelectorAll('.tag-healthcare');
    healthcareTags.forEach(tag => {
        tag.addEventListener('mouseover', () => highlightSimilarTags('tag-healthcare'));
        tag.addEventListener('mouseout', () => removeHighlight('tag-healthcare'));
    });
});
