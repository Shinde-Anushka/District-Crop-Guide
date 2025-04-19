import os
from district_data import district_data

def generate_district_page(district_name, district_info):
    # Read the template
    with open('district_template.html', 'r') as f:
        template = f.read()

    # Replace placeholders with actual data
    page = template.replace('District Name', district_name.title())
    page = page.replace('[humidity]', district_info['humidity'])
    page = page.replace('[humidity_range]', district_info['humidity_range'])
    page = page.replace('[rainfall]', district_info['rainfall'])
    page = page.replace('[monsoon]', district_info['monsoon'])
    page = page.replace('[soil_types]', district_info['soil_types'])
    page = page.replace('[soil_ph]', district_info['soil_ph'])
    page = page.replace('[kharif]', district_info['kharif'])
    page = page.replace('[rabi]', district_info['rabi'])

    # Generate crops section
    crops_html = ''
    for crop in district_info['crops']:
        crop_html = f'''
        <div class="crop-card">
            <img src="images/{crop['name'].lower()}.webp" alt="{crop['name']}">
            <h3>{crop['name']}</h3>
            <p>{crop['desc']}</p>
        </div>
        '''
        crops_html += crop_html

    # Replace crops placeholder
    page = page.replace('<!-- Crop cards will be inserted here -->', crops_html)

    # Write the generated page
    with open(f'{district_name}.html', 'w') as f:
        f.write(page)

def main():
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Generate pages for specific districts
    districts = ['amravati', 'akola']
    for district_name in districts:
        if district_name in district_data:
            generate_district_page(district_name, district_data[district_name])
            print(f'Generated page for {district_name}')

if __name__ == '__main__':
    main() 