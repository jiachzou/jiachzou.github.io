---
layout: archive
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div id="about-content">
  <!-- Content will be dynamically loaded based on language selection -->
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Function to load translations and render content
  function loadAboutContent(lang) {
    // Define translations inline for now
    const translations = {
      'en': {
        'bio_title': '__Bio__',
        'bio_content': 'I work on optimization and networks at [Autonomous Mobility & Delivery team of Uber](https://www.uber.com/us/en/autonomous/). Previously, I was a postdoctoral research scientist at [Columbia IEOR](https://ieor.columbia.edu/) and [Data Science Institute](https://datascience.columbia.edu/), hosted by [Agostino Capponi](https://www.columbia.edu/~ac3827/). In 2024, I received PhD in [MS&E](https://msande.stanford.edu/) with PhD Minor in [Statistics](https://statistics.stanford.edu/) from Stanford. I was fortunate to be advised by [Markus Pelger](https://mpelger.people.stanford.edu/) as a member of the [Advanced Financial Technologies Lab](https://fintech.stanford.edu/). <br>',
        
        'committee_title': 'Doctoral dissertation committee:',
        'committee_members': '[Markus Pelger](https://mpelger.people.stanford.edu/), [Kay Giesecke](https://giesecke.people.stanford.edu/), [Itai Ashlagi](https://web.stanford.edu/~iashlagi/), [Han Hong](https://profiles.stanford.edu/han-hong), [Jann Spiess](https://gsb-faculty.stanford.edu/jann-spiess/). <br>',
        
        'contact_label': 'Contact:',
        'contact_info': 'jiachengzou [at] alumni.stanford.edu <br>',
        
        'research_title': '__Research brief__',
        'research_content': 'I develop statistical methods for inference in large dimensional time series data to make better decisions. My goal is to design useful tools merging econometrics and Transformer-based ML.\n\nMy current work includes graph neural networks applications in [supply chains](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617) and learning in non-stationary environment.\n\nSee more in [my research tab]({{ site.baseurl }}/research/).',
        
        'updates_title': '__Updates__',
        'updates': [
          '[Dec 2025] _R&R at **Journal of Financial Economics (JFE)**_ for our [graph learning for supply chain](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617) paper.',
          '[Apr 2025] _R&R at **Management Science (MS)**_ for our [panel inference](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) paper.',
          '[Aug 2024] Present [panel inference](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891) in [Frontiers of Economics and AI+ML Meeting](https://www.econometricsociety.org/regional-activities/schedule/2024/08/13/2024-ESIFEconomics-and-AIML-Meeting#logistics) at Cornell.'
        ]
      },
      'zh-CN': {
        'bio_title': '__个人简介__',
        'bio_content': '我在[优步自动驾驶与配送团队](https://www.uber.com/us/en/autonomous/)从事优化和网络工作。此前，我是[哥伦比亚大学工业工程与运筹学系](https://ieor.columbia.edu/)和[数据科学研究所](https://datascience.columbia.edu/)的博士后研究员，导师是[Agostino Capponi](https://www.columbia.edu/~ac3827/)。2024年，我在斯坦福大学获得[管理科学与工程系](https://msande.stanford.edu/)博士学位，并获得[统计学系](https://statistics.stanford.edu/)辅修博士学位。我有幸在[Markus Pelger](https://mpelger.people.stanford.edu/)教授的指导下，作为[先进金融技术实验室](https://fintech.stanford.edu/)的一员完成学业。<br>',
        
        'committee_title': '博士论文委员会：',
        'committee_members': '[Markus Pelger](https://mpelger.people.stanford.edu/), [Kay Giesecke](https://giesecke.people.stanford.edu/), [Itai Ashlagi](https://web.stanford.edu/~iashlagi/), [Han Hong](https://profiles.stanford.edu/han-hong), [Jann Spiess](https://gsb-faculty.stanford.edu/jann-spiess/)。<br>',
        
        'contact_label': '联系方式：',
        'contact_info': 'jiachengzou [at] alumni.stanford.edu <br>',
        
        'research_title': '__研究简介__',
        'research_content': '我开发用于大规模时间序列数据推断的统计方法，以做出更好的决策。我的目标是设计融合计量经济学和基于Transformer的机器学习的实用工具。\n\n我目前的工作包括图神经网络在[供应链](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617)中的应用以及非平稳环境中的学习。\n\n更多信息请访问[我的研究页面]({{ site.baseurl }}/research/)。',
        
        'updates_title': '__最新动态__',
        'updates': [
          '[2025年12月] _我们的[供应链图学习](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617)论文被**《金融经济学杂志》(JFE)**接收修订。',
          '[2025年4月] _我们的[面板推断](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891)论文被**《管理科学》(MS)**接收修订。',
          '[2024年8月] 在康奈尔大学[经济学与AI+ML前沿会议](https://www.econometricsociety.org/regional-activities/schedule/2024/08/13/2024-ESIFEconomics-and-AIML-Meeting#logistics)上展示[面板推断](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891)研究。'
        ]
      },
      'zh-TW': {
        'bio_title': '__個人簡介__',
        'bio_content': '我在[優步自動駕駛與配送團隊](https://www.uber.com/us/en/autonomous/)從事優化和網路工作。此前，我是[哥倫比亞大學工業工程與運籌學系](https://ieor.columbia.edu/)和[數據科學研究所](https://datascience.columbia.edu/)的博士後研究員，導師是[Agostino Capponi](https://www.columbia.edu/~ac3827/)。2024年，我在史丹佛大學獲得[管理科學與工程系](https://msande.stanford.edu/)博士學位，並獲得[統計學系](https://statistics.stanford.edu/)輔修博士學位。我有幸在[Markus Pelger](https://mpelger.people.stanford.edu/)教授的指導下，作為[先進金融技術實驗室](https://fintech.stanford.edu/)的一員完成學業。<br>',
        
        'committee_title': '博士論文委員會：',
        'committee_members': '[Markus Pelger](https://mpelger.people.stanford.edu/), [Kay Giesecke](https://giesecke.people.stanford.edu/), [Itai Ashlagi](https://web.stanford.edu/~iashlagi/), [Han Hong](https://profiles.stanford.edu/han-hong), [Jann Spiess](https://gsb-faculty.stanford.edu/jann-spiess/)。<br>',
        
        'contact_label': '聯繫方式：',
        'contact_info': 'jiachengzou [at] alumni.stanford.edu <br>',
        
        'research_title': '__研究簡介__',
        'research_content': '我開發用於大規模時間序列數據推斷的統計方法，以做出更好的決策。我的目標是設計融合計量經濟學和基於Transformer的機器學習的實用工具。\n\n我目前的工作包括圖神經網路在[供應鏈](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617)中的應用以及非平穩環境中的學習。\n\n更多資訊請訪問[我的研究頁面]({{ site.baseurl }}/research/)。',
        
        'updates_title': '__最新動態__',
        'updates': [
          '[2025年12月] _我們的[供應鏈圖學習](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5031617)論文被**《金融經濟學雜誌》(JFE)**接收修訂。',
          '[2025年4月] _我們的[面板推斷](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891)論文被**《管理科學》(MS)**接收修訂。',
          '[2024年8月] 在康奈爾大學[經濟學與AI+ML前沿會議](https://www.econometricsociety.org/regional-activities/schedule/2024/08/13/2024-ESIFEconomics-and-AIML-Meeting#logistics)上展示[面板推斷](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4315891)研究。'
        ]
      }
    };
    
    const t = translations[lang] || translations['en'];
    const aboutContent = document.getElementById('about-content');
    
    // Build the content HTML
    let html = '';
    
    // Bio section
    html += `<p>${t.bio_title}</p>\n\n`;
    html += `<p>${t.bio_content}</p>\n\n`;
    
    // Committee section
    html += `<p>${t.committee_title} ${t.committee_members}</p>\n\n`;
    
    // Contact section
    html += `<p>${t.contact_label} ${t.contact_info}</p>\n\n`;
    
    html += '<p>------</p>\n\n';
    
    // Research section
    html += `<p>${t.research_title}</p>\n\n`;
    html += `<p>${t.research_content.replace(/\n\n/g, '<br><br>')}</p>\n\n`;
    
    html += '<p>------</p>\n\n';
    
    // Updates section
    html += `<p>${t.updates_title}</p>\n\n`;
    html += '<ul>\n';
    t.updates.forEach(update => {
      html += `<li>${update}</li>\n`;
    });
    html += '</ul>\n';
    
    // Set the content
    aboutContent.innerHTML = html;
  }
  
  // Get saved language preference or default to English
  const savedLanguage = localStorage.getItem('preferred-language') || 'en';
  loadAboutContent(savedLanguage);
  
  // Listen for language changes
  document.addEventListener('languageChanged', function(e) {
    loadAboutContent(e.detail.lang);
  });
  
  // Override the language selector's applyTranslations function to trigger our event
  const originalApplyTranslations = window.applyTranslations;
  window.applyTranslations = function(lang) {
    if (originalApplyTranslations) originalApplyTranslations(lang);
    
    // Create and dispatch custom event
    const event = new CustomEvent('languageChanged', { detail: { lang } });
    document.dispatchEvent(event);
  };
});
</script>