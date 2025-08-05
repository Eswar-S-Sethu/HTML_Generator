import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


# Conversion data
conversions = [
    ("lbs_to_kg", "Pounds", "Kilograms", "Convert Pounds to Kilograms"),
    ("kg_to_lbs", "Kilograms", "Pounds", "Convert Kilograms to Pounds"),
    ("cm_to_in", "Centimeters", "Inches", "Convert Centimeters to Inches"),
    ("in_to_cm", "Inches", "Centimeters", "Convert Inches to Centimeters"),
    ("m_to_km", "Meters", "Kilometers", "Convert Meters to Kilometers"),
    ("km_to_m", "Kilometers", "Meters", "Convert Kilometers to Meters"),
    ("c_to_f", "Celsius", "Fahrenheit", "Convert Celsius to Fahrenheit"),
    ("f_to_c", "Fahrenheit", "Celsius", "Convert Fahrenheit to Celsius"),
    ("c_to_k", "Celsius", "Kelvin", "Convert Celsius to Kelvin"),
    ("k_to_c", "Kelvin", "Celsius", "Convert Kelvin to Celsius"),
    ("kmh_to_mph", "Kilometers per hour", "Miles per hour", "Convert km/h to mph"),
    ("mph_to_kmh", "Miles per hour", "Kilometers per hour", "Convert mph to km/h"),
    ("sqm_to_sqft","Square metres", "Square feet","Convert sqm to sqft"),
    ("sqft_to_sqm","Square feet", "Square metres", "Convert sqft to sqm"),
    ("l_to_gal", "litres", "gallons", "Convert litres to gallons"),
    ("gal_to_l", "gallons", "litres", "Convert gallons to litres"),
    ("hrs_to_min", "hours", "minutes", "Convert hours to minutes"),
    ("min_to_sec", "minutes", "seconds", "Convert minutes to seconds"),
    ("pa_to_psi", "pascal", "psi", "Convert pa to psi"),
    ("psi_to_pa", "psi", "pascal", "Convert psi to pa"),
    ("j_to_cal", "joules", "calories", "Convert joules to calories"),
    ("cal_to_j", "calories", "joules", "Convert calories to joules"),
    ("w_to_kw", "watt", "kilowatt", "Convert watt to kilowatt"),
    ("kw_to_w", "kilowatt", "watt", "Convert kilowatt to watt"),
    ("kb_to_mb", "kilobytes", "megabytes", "Convert kilobytes to megabytes"),
    ("mb_to_gb", "megabytes", "gigabytes", "Convert megabytes to gigabytes"),
    ("gb_to_tb", "gigabytes", "terabytes", "Convert gigabytes to terabytes"),
    ("us_to_eu_ring", "us ring size", "eu ring size", "Convert us ring size to eu size"),
    ("eu_to_us_ring", "eu ring size", "us ring size", "Convert eu ring size to eu size"),
    ("us_shoe_to_eu", "us shoe size", "eu shoe size", "Convert us shoe size to eu size"),
    ("eu_shoe_to_us", "eu shoe size", "us shoe size", "Convert eu shoe size to us size"),
    ("us_to_eu_clothing", "us cloth size", "eu cloth size", "Convert us cloth size to eu size"),
    ("eu_to_us_clothing", "eu cloth size", "us cloth size", "Convert eu cloth size to us size"),
    ("tsp_to_tbsp", "teaspoon", "tablespoon", "Convert teaspoon to tablespoon"),
    ("tbsp_to_tsp", "tablespoon", "teaspoon", "Convert tablespoon to teaspoon"),
    ("cup_to_ml", "cup", "millilitre", "Convert cup to millilitre"),
    ("ml_to_cup", "millilitre", "cup", "Convert millilitre to cup"),
    ("oz_to_grams", "oz", "grams", "Convert oz to grams"),
    ("grams_to_oz", "grams", "oz", "Convert grams to oz"),
    ("steps_to_km", "steps", "kilometres", "Convert steps to kilometres"),
    ("km_to_steps", "kilometres", "steps", "Convert kilometres to steps"),
    ("newtons_to_pounds_force", "Newton", "Pounds Force", "Convert Newtons to Pounds Force"),
    ("pounds_force_to_newtons", "Pounds Force", "Newton", "Convert Pounds Force to Newtons"),
    ("wpm_to_cpm", "words per minute", "characters per minute", "Convert wpm to cpm"),
    ("cpm_to_wpm", "characters per minute", "words per minute", "Convert cpm to wpm"),
    ("percent_to_gpa", "Percent", "GPA", "Convert percent to gpa"),
    ("gpa_to_percent", "GPA", "Percent", "Convert gpa to percent"),
]

# add to the converter data in the list before running it.
def sitemap_generator():
    # Base URL
    base_url = "https://toolstack.com.au/"

    # Converter data
    converters = [
        {"title": "Pounds to Kilograms", "file": "lbs_to_kg.html"},
        {"title": "Kilograms to Pounds", "file": "kg_to_lbs.html"},
        {"title": "Centimeters to Inches", "file": "cm_to_in.html"},
        {"title": "Inches to Centimeters", "file": "in_to_cm.html"},
        {"title": "Meters to Kilometers", "file": "m_to_km.html"},
        {"title": "Kilometers to Meters", "file": "km_to_m.html"},
        {"title": "Celsius to Fahrenheit", "file": "c_to_f.html"},
        {"title": "Fahrenheit to Celsius", "file": "f_to_c.html"},
        {"title": "Celsius to Kelvin", "file": "c_to_k.html"},
        {"title": "Kelvin to Celsius", "file": "k_to_c.html"},
        {"title": "km/h to mph", "file": "kmh_to_mph.html"},
        {"title": "mph to km/h", "file": "mph_to_kmh.html"},
        {"title": "sqm to sqft", "file": "sqm_to_sqft.html"},
        {"title": "sqft to sqm", "file": "sqft_to_sqm.html"},
        {"title": "Litre to Gallon", "file": "l_to_gal.html"},
        {"title": "Gallon to Litre", "file": "gal_to_l.html"},
        {"title": "Hours to Minutes", "file": "hrs_to_min.html"},
        {"title": "Minutes to Seconds", "file": "min_to_sec.html"},
        {"title": "Pascal to PSI", "file": "pa_to_psi.html"},
        {"title": "PSI to Pascal", "file": "psi_to_pa.html"},
        {"title": "Joules to Calories", "file": "j_to_cal.html"},
        {"title": "Calories to Joules", "file": "cal_to_j.html"},
        {"title": "Watt to Kilowatt", "file": "w_to_kw.html"},
        {"title": "Kilowatt to Watt", "file": "kw_to_w.html"},
        {"title": "Kilobytes to Megabytes", "file": "kb_to_mb.html"},
        {"title": "Megabytes to Gigabytes", "file": "mb_to_gb.html"},
        {"title": "Gigabytes to Terabytes", "file": "gb_to_tb.html"},
        {"title": "US ring size to EU ring size", "file": "us_to_eu_ring.html"},
        {"title": "EU ring size to US ring size", "file": "eu_to_us_ring.html"},
        {"title": "US shoe size to EU shoe size", "file": "us_shoe_to_eu.html"},
        {"title": "EU shoe size to US shoe size", "file": "eu_shoe_to_us.html"},
        {"title": "US cloth size to EU cloth size", "file": "us_to_eu_clothing.html"},
        {"title": "EU cloth size to US cloth size", "file": "eu_to_us_clothing.html"},
        {"title": "Teaspoon to Tablespoon", "file": "tsp_to_tbsp.html"},
        {"title": "Tablespoon to Teaspoon", "file": "tbsp_to_tsp.html"},
        {"title": "Cup to Millilitre", "file": "cup_to_ml.html"},
        {"title": "Millilitre to Cup", "file": "ml_to_cup.html"},
        {"title": "Oz to Grams", "file": "oz_to_grams.html"},
        {"title": "Grams to Oz", "file": "grams_to_oz.html"},
        {"title": "Steps to kilometres", "file": "steps_to_km.html"},
        {"title": "Kilometres to Steps", "file": "km_to_steps.html"},
        {"title": "Newton to Pound Force", "file": "newtons_to_pounds_force.html"},
        {"title": "Pound Force to Newton", "file": "pounds_force_to_newtons.html"},
        {"title": "WPM to CPM", "file": "wpm_to_cpm.html"},
        {"title": "CPM to WPM", "file": "cpm_to_wpm.html"},
        {"title": "Percent to GPA", "file": "percent_to_gpa.html"},
        {"title": "GPA to Percent", "file": "gpa_to_percent.html"}
    ]

    # Create XML structure
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Add each page to sitemap
    for item in converters:
        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = base_url + item["file"]

        # Optional: Add <changefreq> and <priority>
        ET.SubElement(url, "changefreq").text = "monthly"
        ET.SubElement(url, "priority").text = "0.8"

    # Format output
    xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")

    # Write to sitemap.xml
    with open("dist/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    print("✅ sitemap.xml created in dist/")


def generate_meta(from_unit, to_unit, label):
    description = f"{label} online using ToolStack. Convert {from_unit.lower()} to {to_unit.lower()} quickly with no signup, for free and offline."
    keywords = f"{from_unit.lower()}, {to_unit.lower()}, convert {from_unit.lower()} to {to_unit.lower()}, {label.lower()}, ToolStack, offline, serverless, in-browser"
    return description, keywords


# HTML template with escaped curly braces
html_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="ToolStack by Eswar">
    <!-- Open Graph Meta -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://toolstack.com.au/{slug}">
    <meta property="og:image" content="https://toolstack.com.au/android-chrome-512x512.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://toolstack.com.au/android-chrome-512x512.png">

    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <!-- Apple touch icon -->
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <!-- PNG versions -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <!-- Web manifest -->
    <link rel="manifest" href="/site.webmanifest">    
    
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/styles.css">
    <script type="module">
        import init, * as wasm from './UnitConverter.js';
        async function run() {{
            await init();
            const btn = document.getElementById('convertBtn');
            btn.onclick = function () {{
                const input = parseFloat(document.getElementById('inputVal').value);
                const isWhole = document.getElementById('wholeToggle').checked;
                const result = wasm.{func}(input);
                const output = isWhole ? Math.round(result) : result.toFixed(4);
                const resultEl = document.getElementById('result');
                resultEl.innerText = `Result: ${{output}} {to_unit}`;
                sessionHistory.push(`${{input}} {from_unit} = ${{output}} {to_unit}`);

                updateHistory();
            }};
        }}
        run();
        
        
    </script>
</head>
<body class="bg-dark text-white">
<nav class="navbar navbar-expand-lg navbar-light custom-navbar border-bottom mb-5">
  <div class="container d-flex justify-content-between align-items-center">
    <!-- Brand -->
    <a class="navbar-brand fw-bold me-auto" href="index.html">ToolStack</a>
  </div>
</nav>

<!-- Search section below navbar -->
<div class="search-wrapper position-relative my-3 w-100 d-flex justify-content-center">
  <div class="w-50 position-relative">
    <input class="form-control rounded-pill px-4" type="search" placeholder="Search conversions" aria-label="Search" id="searchInput">
    <div class="result-list position-absolute w-100" id="results"></div>
  </div>
</div>
<br><br>
<div class="container">
    <div class="row">
        <div class="col-md-8 mx-auto text-center">
            <h1 class="mb-4">{label}</h1>
            <input type="number" id="inputVal" class="form-control mb-3" placeholder="Enter value in {from_unit}">
            <div class="d-flex justify-content-center gap-2 mb-3">
                <button id="convertBtn" class="btn btn-primary">Convert</button>
                <button class="btn btn-secondary" onclick="clearFields()">Clear</button>
                <button class="btn btn-success" onclick="copyResult()">Copy</button>
                <div class="form-check form-switch align-self-center">
                    <input class="form-check-input" type="checkbox" id="wholeToggle">
                    <label class="form-check-label" for="wholeToggle">Whole Number</label>
                </div>
            </div>
            <p id="result" class="fs-4 fw-bold"></p>
        </div>
    </div>
    <hr>
    <div class="row">
        <div class="col-md-8 mx-auto">
            <h4>Session History</h4>
            <ul id="historyList" class="list-group mb-3"></ul>
            <button class="btn btn-outline-primary" onclick="downloadHistory()">Download History</button>
        </div>
    </div>
    <hr>
</div>

<!-- Bulk Conversion -->
<section class="container text-center my-5 rounded-4 px-3 py-5" style="background-color: #0B0C1D;">
  <h2 class="mb-3 text-white">🎉 Bulk Conversions</h2>
  <p class="text-white-50 mb-4">
    Bulk Conversions are here! Upload a CSV file and convert thousands of values at once.<br>
  </p>
    <button id="comingSoonBtn" class="btn btn-outline-light rounded-pill px-4 py-2" onclick=window.open('bulk_converter.html','_self')>Try Now</button>
</section>



<!-- Footer -->
  <footer class="bg-dark text-light pt-4 mt-5">
  <div class="container">
    <div class="row text-center text-md-start">
      <!-- About -->
      <div class="col-md-4 mb-3">
        <h5 class="fw-bold">ToolStack</h5>
        <p class="small">Serverless by Design. No Fluff. No BS. Built for real users, by an indie dev.</p>
      </div>

      <!-- Useful Links -->
      <div class="col-md-4 mb-3">
        <h6 class="fw-bold">Useful Links</h6>
        <ul class="list-unstyled">
          <li><a href="index.html" class="text-light text-decoration-none">Home</a></li>
          <li><a href="privacy_policy.html" class="text-light text-decoration-none">Privacy Policy</a></li>
          <li><a href="terms_of_use.html" class="text-light text-decoration-none">Terms of Use</a></li>
          <li><a href="contact_developer.html" class="text-light text-decoration-none">About Developer</a></li>
        </ul>
      </div>

      <!-- Social / Extras -->
      <div class="col-md-4 mb-3">
        <h6 class="fw-bold">Connect</h6>
        <ul class="list-unstyled">
          <li><a href="https://x.com/eswar_sethu" class="text-light text-decoration-none">X</a></li>
          <li><a href="https://github.com/Eswar-S-Sethu" class="text-light text-decoration-none">Github</a></li>
          <li><a href="mailto:dev@toolstack.com.au" class="text-light text-decoration-none">Email</a></li>
        </ul>
      </div>
    </div>

    <hr class="bg-secondary" />

    <div class="text-center small pb-3">
      &copy; 2025 <strong>ToolStack</strong>. Born in Melbourne. Built for the world. All rights reserved.
    </div>
  </div>
</footer>

<script>
let sessionHistory = [];
function updateHistory() {{
    const ul = document.getElementById('historyList');
    ul.innerHTML = '';
    sessionHistory.forEach(entry => {{
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = entry;
        ul.appendChild(li);
    }});
}}
function copyResult() {{
    const resultText = document.getElementById('result').innerText;
    navigator.clipboard.writeText(resultText);
}}
function clearFields() {{
    document.getElementById('inputVal').value = '';
    document.getElementById('result').innerText = '';
}}
function downloadHistory() {{
    const blob = new Blob([sessionHistory.join('\\n')], {{ type: 'text/plain' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'conversion_history.txt';
    a.click();
    URL.revokeObjectURL(url);
}}
function toggleTheme() {{
    const root = document.documentElement;
    const current = root.getAttribute('data-theme');
    const next = current === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    document.body.className = next === 'dark' ? 'bg-dark text-light' : 'bg-light text-dark';
    localStorage.setItem('theme', next);
}}
(function () {{
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.body.className = savedTheme === 'dark' ? 'bg-dark text-light' : 'bg-light text-dark';
}})();

    const converters = [
      {{ title: 'Pounds to Kilograms', file: 'lbs_to_kg.html', tags: 'lbs to kg pounds kilograms' }},
      {{ title: 'Kilograms to Pounds', file: 'kg_to_lbs.html', tags: 'kg to lbs kilograms pounds' }},
      {{ title: 'Centimeters to Inches', file: 'cm_to_in.html', tags: 'cm to in centimeters inches' }},
      {{ title: 'Inches to Centimeters', file: 'in_to_cm.html', tags: 'in to cm inches centimeters' }},
      {{ title: 'Meters to Kilometers', file: 'm_to_km.html', tags: 'm to km meters kilometers' }},
      {{ title: 'Kilometers to Meters', file: 'km_to_m.html', tags: 'km to m kilometers meters' }},
      {{ title: 'Celsius to Fahrenheit', file: 'c_to_f.html', tags: 'c to f celsius fahrenheit' }},
      {{ title: 'Fahrenheit to Celsius', file: 'f_to_c.html', tags: 'f to c fahrenheit celsius' }},
      {{ title: 'Celsius to Kelvin', file: 'c_to_k.html', tags: 'c to k celsius kelvin' }},
      {{ title: 'Kelvin to Celsius', file: 'k_to_c.html', tags: 'k to c kelvin celsius' }},
      {{ title: 'km/h to mph', file: 'kmh_to_mph.html', tags: 'kmh to mph kilometers per hour miles per hour' }},
      {{ title: 'mph to km/h', file: 'mph_to_kmh.html', tags: 'mph to kmh miles per hour kilometers per hour' }},
      {{ title: 'sqm to sqft', file: 'sqm_to_sqft.html', tags: 'sqm to sqft square meter square feet' }},
      {{ title: 'sqft to sqm', file: 'sqft_to_sqm.html', tags: 'sqft to sqm square feet square meter' }},
      {{ title: 'Litre to Gallon', file: 'l_to_gal.html', tags: 'ltr to gal litre gallon' }},
      {{ title: 'Gallon to Litre', file: 'gal_to_l.html', tags: 'gal to ltr gallon litre' }},
      {{ title: 'Hours to Minutes', file: 'hrs_to_min.html', tags: 'hrs to min hours to minutes' }},
      {{ title: 'Minutes to Seconds', file: 'min_to_sec.html', tags: 'min to sec minutes to seconds' }},
      {{ title: 'Pascal to PSI', file: 'pa_to_psi.html', tags: 'pa to psi' }},
      {{ title: 'PSI to Pascal', file: 'psi_to_pa.html', tags: 'psi to pa' }},
      {{ title: 'Joules to Calories', file: 'j_to_cal.html', tags: 'j to cal joule to calories' }},
      {{ title: 'Calories to Joules', file: 'cal_to_j.html', tags: 'cal to j calories to joule' }},
      {{ title: 'Watt to Kilowatt', file: 'w_to_kw.html', tags: 'w to kw watt to kilowatt' }},
      {{ title: 'Kilowatt to Watt', file: 'kw_to_w.html', tags: 'kw to w kilowatt to watt' }},
      {{ title: 'Kilobytes to Megabytes', file: 'kb_to_mb.html', tags: 'kb to mb KB to MB Kilobytes Megabytes' }},
      {{ title: 'Megabytes to Gigabytes', file: 'mb_to_gb.html', tags: 'mb to gb MB to GB Megabytes Gigabytes' }},
      {{ title: 'Gigabytes to Terabytes', file: 'gb_to_tb.html', tags: 'gb to tb GB to TB Gigabytes Terabytes' }},
      {{ title: 'US ring size to EU ring size', file: 'us_to_eu_ring.html', tags: 'US ring size to EU ring size ' }},
      {{ title: 'EU ring size to US ring size', file: 'eu_to_us_ring.html', tags: 'EU ring size to US ring size' }},
      {{ title: 'US shoe size to EU shoe size', file: 'us_shoe_to_eu.html', tags: 'US shoe size to EU shoe size' }},
      {{ title: 'EU shoe size to US shoe size', file: 'eu_shoe_to_us.html', tags: 'EU shoe size to US shoe size' }},
      {{ title: 'US cloth size to EU cloth size', file: 'us_to_eu_clothing.html', tags: 'US cloth size to Euro cloth size' }},
      {{ title: 'EU cloth size to US cloth size', file: 'eu_to_us_clothing.html', tags: 'Euro cloth size to US cloth size' }},
      {{ title: 'Teaspoon to Tablespoon', file: 'tsp_to_tbsp.html', tags: 'teaspoon to tablespoon teaspoon tablespoon' }},
      {{ title: 'Tablespoon to Teaspoon', file: 'tbsp_to_tsp.html', tags: 'tablespoon to teaspoon tablespoon teaspoon' }},
      {{ title: 'Cup to Millilitre', file: 'cup_to_ml.html', tags: 'cup to ml cup millilitres' }},
      {{ title: 'Millilitre to Cup', file: 'ml_to_cup.html', tags: 'ml to cup millilitres cup' }},
      {{ title: 'Oz to Grams', file: 'oz_to_grams.html', tags: 'oz to grams' }},
      {{ title: 'Grams to Oz', file: 'grams_to_oz.html', tags: 'grams to oz' }},
      {{ title: 'Steps to kilometres', file: 'steps_to_km.html', tags: 'steps to km steps kilometers' }},
      {{ title: 'Kilometres to Steps', file: 'km_to_steps.html', tags: 'km to steps kilometers steps' }},
      {{ title: 'Newton to Pound Force', file: 'newtons_to_pounds_force.html', tags: 'newtons to pounds force' }},
      {{ title: 'Pound Force to Newton', file: 'pounds_force_to_newtons.html', tags: 'pounds force to newtons' }},
      {{ title: 'WPM to CPM', file: 'wpm_to_cpm.html', tags: 'wpm to cpm word per minute character per minute' }},
      {{ title: 'CPM to WPM', file: 'cpm_to_wpm.html', tags: 'cpm to wpm character per minute word per minute' }},
      {{ title: 'Percent to GPA', file: 'percent_to_gpa.html', tags: 'percent to gpa percentage gpa' }},
      {{ title: 'GPA to Percent', file: 'gpa_to_percent.html', tags: 'gpa to percent gpa percentage' }},


    ];


    document.getElementById('searchInput').addEventListener('input', function () {{
      const query = this.value.toLowerCase();
      const resultDiv = document.getElementById('results');
      resultDiv.innerHTML = '';

      if (query.length === 0) {{
        resultDiv.style.display = 'none';
        return;
      }}

      const matches = converters.filter(c => c.tags.includes(query));
      if (matches.length > 0) {{
        resultDiv.style.display = 'block';
        matches.forEach(c => {{
          const a = document.createElement('a');
          a.href = c.file;
          a.textContent = c.title;
          resultDiv.appendChild(a);
        }});
      }} else if (query.length > 2) {{
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = '<p class="text-muted">No matches found.</p>';
      }} else {{
        resultDiv.style.display = 'none';
      }}
    }});


</script>
</body>
</html>
"""

# Output folder
output_dir = "dist"
os.makedirs(output_dir, exist_ok=True)

# Generate HTML files
for func, from_unit, to_unit, label in conversions:
    filename = f"{func}.html"
    description, keywords = generate_meta(from_unit, to_unit, label)
    content = html_template.format(
        title=label,
        label=label,
        func=func,
        from_unit=from_unit,
        to_unit=to_unit,
        description=description,
        keywords=keywords,
        slug=filename  # for Open Graph URL
    )
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)


print("✅ Pages generated in:", output_dir)

# generates a new sitemap. make sure to update the converter data list before running
