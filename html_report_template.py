
html_report_template = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ title }}</title>
  <style>
    /* Base Tufte CSS */
    html {{ font-size: 15px; }}

    body {{
      width: 90%;
      color: #111;
      max-width: 1800px;
      overflow-x: none;
      counter-reset: sidenote-counter;
      background-color: #fffff8;
      font-family: et-book, Palatino, "Palatino Linotype", "Palatino LT STD", "Book Antiqua", Georgia, serif;
      display: flex;
    }}

    /* Layout adjustments */
    #main-content {{
      margin-left: 0%;
      width: 80%; /* Adjusted for majority screen usage */
    }}

    #sidebar {{
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      width: 25%; /* Sidebar adjusted to make main content wider */
      padding: 1rem;
      background-color: #f4f4f4;
      height: 100vh;
      overflow-y: auto;
      font-size: 1.2rem;
      font-family: et-book, Palatino, "Palatino Linotype", "Palatino LT STD", "Book Antiqua", Georgia, serif;
    }}

    /* Sticky Sidebar */
    #sidebar ul {{
      list-style-type: none;
      padding-left: 0;
    }}

    #sidebar li {{
      margin: 0.5rem 0;
    }}

      #sidebar a {{
      all: unset;
      color: #111;
      text-decoration: none !important;
      font-family: et-book, Palatino, "Palatino Linotype", "Palatino LT STD", "Book Antiqua", Georgia, serif;
    }}

    #sidebar a:hover {{
      text-decoration: underline !important;
    }}

    #sidebar .sidebar-section {{
      margin-top: 1.5rem;
      font-weight: bold;
    }}

    #sidebar .sidebar-subsection {{
      margin-left: 1rem;
      font-weight: normal;
    }}

    /* Typography */
    h1.title {{
      font-weight: 400;
      margin-top: 4rem;
      margin-bottom: 1.5rem;
      font-size: 3.2rem;
      line-height: 1;
    }}

    h1 {{
      font-weight: 400;
      margin-top: 2.1rem;
      margin-bottom: 0;
      font-size: 2.2rem;
      line-height: 1;
    }}

    h2 {{
      font-weight: 400;
      font-style: italic;
      font-size: 1.7rem;
      margin-top: 2rem;
      margin-bottom: 0;
      line-height: 1;
    }}

    h3.subtitle {{
      font-weight: 400;
      font-style: italic;
      margin-top: 1rem;
      margin-bottom: 1rem;
      font-size: 1.8rem;
      display: block;
      line-height: 1;
    }}

    h3 {{
      font-weight: 400;
      font-style: italic;
      font-size: 1.5rem;
      margin-top: 1.5rem;
      margin-bottom: 0;
      line-height: 1;
    }}

    h4 {{
      font-weight: 400;
      font-style: italic;
      font-size: 1.3rem;
      margin-top: 1.3rem;
      margin-bottom: 0.5rem;
      line-height: 1;
    }}

    h4.author, h4.date {{
      font-size: 1.4rem;
      font-weight: 400;
      margin: 1rem auto;
      line-height: 1;
    }}

    /* Layout */
    article {{
      position: relative;
      padding: 0rem 0rem 0rem 5rem;
    }}

    p, ol, ul {{ font-size: 1.4rem; }}

    p {{
      line-height: 2rem;
      margin-top: 1.4rem;
      margin-bottom: 1.4rem;
      padding-right: 0;
      vertical-align: baseline;
      width: 100%;
    }}

    /* Tables */
    table {{
      border-top: 2px solid #111;
      border-bottom: 2px solid #111;
      font-size: 1.1rem;
      width: 100%;
      margin: 2rem 0;
      border-collapse: collapse;
    }}

    th {{
      border-bottom: 1px solid #111;
      padding: 0.5rem;
      text-align: left;
    }}

    td {{
      padding: 0.5rem;
      border-bottom: 1px solid #ddd;
    }}

    /* Quotes */
    blockquote {{
      font-size: 1.4rem;
      border-left: 3px solid #ccc;
      padding-left: 1rem;
      margin-left: 1rem;
    }}

    blockquote p {{ width: 90%; }}

    blockquote footer {{
      width: 50%;
      font-size: 1.1rem;
      text-align: right;
    }}

    /* Lists */
    ol, ul {{
      width: 100%;
      -webkit-padding-start: 5%;
      -webkit-padding-end: 5%;
    }}

    li {{ padding: 0.5rem 0; }}

    /* Links */
    a:link, a:visited {{ color: inherit; }}

    a:link {{
      text-decoration: none;
      background: -webkit-linear-gradient(#fffff8, #fffff8), -webkit-linear-gradient(#fffff8, #fffff8), -webkit-linear-gradient(#333, #333);
      background: linear-gradient(#fffff8, #fffff8), linear-gradient(#fffff8, #fffff8), linear-gradient(#333, #333);
      -webkit-background-size: 0.05em 1px, 0.05em 1px, 1px 1px;
      -moz-background-size: 0.05em 1px, 0.05em 1px, 1px 1px;
      background-size: 0.05em 1px, 0.05em 1px, 1px 1px;
      background-repeat: no-repeat, no-repeat, repeat-x;
      text-shadow: 0.03em 0 #fffff8, -0.03em 0 #fffff8, 0 0.03em #fffff8, 0 -0.03em 0 #fffff8, 0.06em 0 #fffff8, -0.06em 0 #fffff8, 0.09em 0 #fffff8, -0.09em 0 #fffff8, 0.12em 0 #fffff8, -0.12em 0 #fffff8, 0.15em 0 #fffff8, -0.15em 0 #fffff8;
      background-position: 0% 93%, 100% 93%, 0% 93%;
    }}

    /* Sidenotes and margin notes */
    .sidenote, .marginnote {{
      float: right;
      clear: right;
      margin-right: -60%;
      width: 50%;
      margin-top: 0;
      margin-bottom: 1rem;
      font-size: 1.1rem;
      line-height: 1.3;
      vertical-align: baseline;
      position: relative;
    }}

    .sidenote-number {{
      position: relative;
      vertical-align: baseline;
      font-size: 1rem;
      top: -0.5rem;
      left: 0.1rem;
    }}

    /* Images and figures */
    img {{max-width: 100%;}}

    .marginnote img {{ display: block; }}

    div.figure {{
      padding: 0;
      border: 0;
      font-size: 100%;
      font: inherit;
      vertical-align: baseline;
      max-width: 100%;
      -webkit-margin-start: 0;
      -webkit-margin-end: 0;
      margin: 0 0 3em 0;
    }}

    figure {{
      margin: 2rem 0;
      text-align: center;
    }}

    figure img {{
      max-width: 100%;
      display: block;
      margin: 0 auto;
    }}

    figure figcaption {{
      font-size: 1.1rem;
      font-style: italic;
      margin-top: 0.5rem;
    }}

    /* Code */
    code {{
      font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 1.125rem;
      line-height: 1.6;
      background-color: #f5f5f5;
      padding: 0.1rem 0.3rem;
      border-radius: 3px;
    }}

    pre code {{
      font-size: 1rem;
      display: block;
      overflow-x: auto;
      padding: 1rem;
      background-color: #f5f5f5;
      border: 1px solid #ddd;
      border-radius: 4px;
    }}

    p code {{ white-space: inherit; }}

    pre {{
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
    }}

    /* Collapsible code blocks */
    .code-container {{
      margin: 1.5rem 0;
    }}

    .code-header {{
      background-color: #f0f0f0;
      padding: 0.5rem 1rem;
      cursor: pointer;
      border: 1px solid #ddd;
      border-radius: 4px 4px 0 0;
      font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 1.1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .code-header:hover {{
      background-color: #e5e5e5;
    }}

    .code-header .arrow {{
      transition: transform 0.3s;
    }}

    .code-header.collapsed .arrow {{
      transform: rotate(-90deg);
    }}

    .code-content {{
      border: 1px solid #ddd;
      border-top: none;
      border-radius: 0 0 4px 4px;
      overflow: hidden;
      transition: max-height 0.3s ease-out;
    }}

    .code-content.collapsed {{
      display: none;
    }}

    .output-container {{
      border: 1px solid #ddd;
      border-radius: 4px;
      margin: 1rem 0;
      padding: 1rem;
      background-color: #fff;
    }}

    .output-header {{
      font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 1.1rem;
      color: #555;
      margin-bottom: 0.5rem;
    }}

    /* Other special elements */
    hr {{
      margin-left: 0;
      width: 55%;
      margin: 2rem 0;
    }}

    .fullwidth {{
      max-width: 90%;
      clear: both;
    }}

    span.newthought {{
      font-variant: small-caps;
      font-size: 1.2em;
    }}

    /* Visualization containers */
    .viz-container {{
      width: 100%;
      margin: 2rem 0;
    }}

    /* Abstract and acknowledgments */
    .abstract, .acknowledgments {{
      font-style: italic;
      margin: 2rem 0;
      padding: 1rem 2rem;
      background-color: #f9f9f9;
      border-left: 3px solid #ccc;
    }}

    /* Equation styling */
    .equation {{
      display: block;
      text-align: center;
      margin: 1.5rem 0;
    }}

    .equation-number {{
      float: right;
    }}

    /* Responsive design */
    @media screen and (max-width: 760px) {{
      body {{
        display: block;
      }}

      #sidebar {{
        position: static;
        width: 100%;
        height: auto;
      }}

      #main-content {{
        width: 100%;
      }}

      p, footer, ol, ul, table, hr {{ width: 90%; }}
      pre {{ width: 87.5%; }}
      ul {{ width: 85%; }}
      figure {{ max-width: 90%; }}
      div.fullwidth p.caption {{ max-width: none; }}
      blockquote p, blockquote footer {{ width: 90%; }}

      .sidenote, .marginnote {{
        display: none;
      }}

      .margin-toggle:checked + .sidenote,
      .margin-toggle:checked + .marginnote {{
        display: block;
        float: left;
        left: 1rem;
        clear: both;
        width: 95%;
        margin: 1rem 2.5%;
        vertical-align: baseline;
        position: relative;
      }}

      label.margin-toggle:not(.sidenote-number) {{ display: inline; }}
      label {{ cursor: pointer; }}

      div.figure {{ max-width: 90%; }}
      pre {{
        width: 90%;
        padding: 0;
      }}
    }}

    input.margin-toggle {{ display: none; }}
    label.sidenote-number {{ display: inline; }}
    label.margin-toggle:not(.sidenote-number) {{ display: none; }}

    /* Custom styles for this report */
    {{ custom_css|safe }}
  </style>
</head>

<body>
  <div id="sidebar">
    <ul>
      <li class="sidebar-section"><a href="#introduction">1. Introduction</a></li>
      <li class="sidebar-subsection"><a href="#background">1.1 Background and Context</a></li>
      <li class="sidebar-subsection"><a href="#research-problem">1.2 Research Problem</a></li>
      <li class="sidebar-subsection"><a href="#significance">1.3 Significance</a></li>
      <li class="sidebar-subsection"><a href="#research-questions">1.4 Research Questions</a></li>
      <li class="sidebar-subsection"><a href="#objectives">1.5 Objectives</a></li>
      <li class="sidebar-subsection"><a href="#thesis-statement">1.6 Key Question</a></li>

      <li class="sidebar-section"><a href="#literature-review">2. Literature Review</a></li>
      <li class="sidebar-subsection"><a href="#theoretical-framework">2.1 Theoretical Framework</a></li>
      <li class="sidebar-subsection"><a href="#current-knowledge">2.2 Current State of Knowledge</a></li>
      <li class="sidebar-subsection"><a href="#research-gaps">2.3 Research Gaps</a></li>
      <li class="sidebar-subsection"><a href="#key-concepts">2.4 Key Concepts</a></li>

      <li class="sidebar-section"><a href="#methodology">3. Methodology</a></li>
      <li class="sidebar-subsection"><a href="#research-design">3.1. Sample Data Previews</a></li>
      <li class="sidebar-subsection"><a href="#data-collection">3.2. Data Preprocessing</a></li>
      <li class="sidebar-subsection"><a href="#data-preprocessing">3.3. Exploratory Data Analysis</a></li>
      <li class="sidebar-subsection"><a href="#exploratory-analysis">3.4. Feature Selection </a></li>
      <li class="sidebar-subsection"><a href="#feature-engineering">3.5. Model Building </a></li>
      <li class="sidebar-subsection"><a href="#model-development">3.6. Model Comparisons</a></li>
      <li class="sidebar-subsection"><a href="#evaluation-metrics">3.7. Predictions and Final Insights</a></li>

      <li class="sidebar-section"><a href="#results">4. Results and Analysis</a></li>
      <li class="sidebar-subsection"><a href="#data-presentation">4.1. Data Presentation</a></li>
      <li class="sidebar-subsection"><a href="#key-findings">4.2. Key Findings</a></li>
      <li class="sidebar-subsection"><a href="#model-performance">4.3. Model Performance</a></li>
      <li class="sidebar-subsection"><a href="#interpretation">4.4. Interpretation</a></li>

      <li class="sidebar-section"><a href="#discussion">5. Synthesis of Findings</a></li>
      <li class="sidebar-subsection"><a href="#relation-to-questions">5.1. Relation to Research Questions</a></li>
      <li class="sidebar-subsection"><a href="#implications">5.2. Implications</a></li>
      <li class="sidebar-subsection"><a href="#limitations">5.3. Limitations</a></li>

      <li class="sidebar-section"><a href="#conclusion">6.1 Conclusion</a></li>
      <li class="sidebar-subsection"><a href="#key-points">6.2 Summary of Key Points</a></li>
      <li class="sidebar-subsection"><a href="#contributions">6.3 Contributions to Field</a></li>
      <li class="sidebar-subsection"><a href="#recommendations">6.4 Recommendations</a></li>
      <li class="sidebar-subsection"><a href="#future-research">6.5 Future Research</a></li>

      
    </ul>
  </div>

   <div id="main-content">
    <article>
      <h1 class="title">{ title }</h1>
      <h3 class="subtitle">{ subtitle }</h3>
      <h4 class="author">{ author }</h4>
      <h4 class="date">{ date }</h4>

      <section id="abstract" class="abstract">
        <h2>Key Question</h2>
        <p>{ Key_Question |safe }</p>
      </section>

      <section id="introduction">
        <h1>1. Introduction</h1>

        <section id="background">
          <h2>1.1. Background and Context</h2>
          <p>{ background|safe }</p>
        </section>

        <section id="research-problem">
          <h2>1.2. Research Problem</h2>
          <p>{ research_problem|safe }</p>
        </section>

        <section id="significance">
          <h2>1.3. Significance of Study</h2>
          <p>{ significance|safe }</p>
        </section>

        <section id="research-questions">
          <h2>1.4. Research Questions</h2>
          <p>{ research_questions|safe }</p>
        </section>

        <section id="objectives">
          <h2>1.5. Objectives</h2>
          <p>{ objectives|safe }</p>
        </section>

        <section id="thesis-statement">
          <h2>1.6. Key Question</h2>
          <p>{ thesis_statement|safe }</p>
        </section>
      </section>

      <section id="literature-review">
        <h1>2. Literature Review</h1>
        <p>{summarised_research_muSearch | safe} </p>
        <section id="theoretical-framework">
          <h2>2.1. Theoretical Framework</h2>
          <p>{ theoretical_framework|safe }</p>
        </section>

        <section id="current-knowledge">
          <h2>2.2. Current State of Knowledge</h2>
          <p>{ current_knowledge|safe }</p>
        </section>

        <section id="research-gaps">
          <h2>2.3. Research Gaps</h2>
          <p>{ research_gaps|safe }</p>
        </section>

        <section id="key-concepts">
          <h2>2.4. Key Concepts and Definitions</h2>
          <p>{ key_concepts|safe }</p>
        </section>
      </section>

     <section id="methodology">
  <h1>3. Methodology</h1>

  <section id="data-collection">
    <h2>3.1. Sample Data Previews</h2>
    <p>add the relevant image or table here followed by the insights</p>

    <section id="data-preprocessing">
        
    <p>add the relevant images or tables here followed by the insights</p>

    <section>

    <section id="
    <h3>3.3. Feature Selection</h3>
    <p>add the relevant images or tables here followed by the insights</p>



  </section>

  <section id="data-preprocessing">
    <h2>3.3. Data Preprocessing</h2>
    <p>{ data_preprocessing_intro|safe }</p>

    <h3>3.3.1. Data Cleaning</h3>
    <p>{ data_cleaning_descriptions|safe }</p>
    <p><strong>Analysis Questions:</strong> Were there any missing values? Were duplicates removed?</p>
    <p><strong>Analysis:</strong> { data_cleaning_analysis|safe }</p>
    <img src="data:image/png;base64,{ data_cleaning_image }" alt="Data Cleaning Visualization">
    <p><strong>Figure:</strong> { data_cleaning_caption|safe }</p>

    <h3>3.3.2. Handling Missing Values</h3>
    <p>{ missing_values_informations|safe }</p>
    <p><strong>Analysis Questions:</strong> How many missing values were removed? What techniques were used?</p>
    <p><strong>Analysis:</strong> { missing_values_analysis|safe }</p>
    <img src="data:image/png;base64,{ missing_values_image }" alt="Handling Missing Values Visualization">
    <p><strong>Figure:</strong> { missing_values_caption|safe }</p>

    <h3>3.3.3. Outlier Detection and Treatment</h3>
    <p>{ outliers|safe }</p>
    <p><strong>Analysis Questions:</strong> Were outliers removed or transformed?</p>
    <p><strong>Analysis:</strong> { outliers_analysis|safe }</p>
    <img src="data:image/png;base64,{ outliers_image }" alt="Outlier Detection Visualization">
    <p><strong>Figure:</strong> { outliers_caption|safe }</p>

    <h3>3.3.4. Data Transformation</h3>
    <p>{ data_transformation|safe }</p>
  </section>

  <section id="exploratory-analysis">
    <h2>3.4. Exploratory Data Analysis (EDA)</h2>
    <p>{ eda_intro|safe }</p>

    <h3>3.4.1. Univariate Analysis</h3>
    <p>{ univariate_analysis|safe }</p>
    <img src="data:image/png;base64,{ univariate_viz }" alt="Univariate Analysis Visualization">
    <p><strong>Figure:</strong> { univariate_viz_caption|safe }</p>

    <h3>3.4.2. Bivariate Analysis</h3>
    <p>{ bivariate_analysis|safe }</p>
    <img src="data:image/png;base64,{ bivariate_viz }" alt="Bivariate Analysis Visualization">
    <p><strong>Figure:</strong> { bivariate_viz_caption|safe }</p>

    <h4>{ other_data_visualizations }</h4>
    <p><strong>Figure:</strong> { other_viz_caption|safe }</p>
    <p> Description for visualizations </p>
  </section>

  <section id="model-development">
    <h2>3.6. Model Development</h2>
    <p>{ model_development_intro|safe }</p>

    <h3>3.6.1. Algorithm Selection</h3>
    <p>{ algorithm_selection|safe }</p>

    <h3>3.6.2. Training Methodology</h3>
    <p>{ training_methodology|safe }</p>

    <h3>3.6.3. Hyperparameter Tuning</h3>
    <p>{ hyperparameter_tuning|safe }</p>
    <img src="data:image/png;base64,{ hyperparameter_tuning_image }" alt="Hyperparameter Tuning Visualization">
    <p><strong>Figure:</strong> { hyperparameter_tuning_caption|safe }</p>
  </section>

  <section id="evaluation-metrics">
    <h2>3.7. Evaluation Metrics</h2>
    <p>{ evaluation_metrics_intro|safe }</p>

    <h3>3.7.1. Performance Metrics</h3>
    <p>{ performance_metrics|safe }</p>
    <div class="equation">{ metrics_equations|safe } <span class="equation-number">(1)</span></div>

    <h3>3.7.2. Validation Strategy</h3>
    <p>{ validation_strategy|safe }</p>
  </section>
</section>


      <section id="results">
        <h1>4. Results and Analysis</h1>

        <section id="data-presentation">
          <h2>4.1. Data Presentation</h2>
          <p>{ data_presentation|safe }</p>

          <div class="viz-container">
            { results_viz|safe }
          </div>
        </section>

        <section id="key-findings">
          <h2>4.2. Key Findings</h2>
          <p>{ key_findings|safe }</p>
        </section>



        <section id="model-performance">
          <h2>4.4. Model Performance</h2>
          <p>{ model_performance|safe }</p>

        </section>
        <section id="interpretation">
          <h2>4.5. Interpretation</h2>
          <p>{ interpretation|safe }</p>

        </section>
      </section>

      <section id="discussion">
        <h1>5. Synthesis of Findings</h1>

        <section id="relation-to-questions">
          <h2>5.1. Relation to Key Question</h2>
          <p>{ relation_to_key_questions|safe }</p>
        </section>

        <section id="implications">
          <h2>5.2.. Implications</h2>
          <p>{ implications|safe }</p>

        </section>
        <section id="limitations">
          <h2>5.4 Limitations</h2>
          <p>{ limitations|safe }</p>
        </section>
      </section>
      <section id="conclusion">
        <h1>6. Conclusion</h1>

        <section id="key-points">
          <h2>6.1. Summary of Key Points</h2>
          <p>{ summary_of_key_points|safe }</p>


        </section>

        <section id="recommendations">
          <h2>6.3. Recommendations</h2>
          <p>{ recommendations|safe }</p>

        </section>
        <section id="future-research">
          <h2>6.4 Future Research</h2>
          <p>{ future_research|safe }</p>
        </section>
      </section>

    </article>
  </div>
</html>
  """
