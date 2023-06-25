const screenshotmachine = require('screenshotmachine');
const fs = require('fs');
const { google } = require('googleapis');

const customerKey = '8d704a';
const screenshotWidth = 1920;
const screenshotHeight = 1080;
const screenshotFormat = 'jpg';
const folderId = '1G07OKD79MFEhW02Kh_jWOb_BQKK9EUWR';

const websites = [
  { id: 1, name: 'iFunded', url: 'https://ifunded.de/en/' },
  { id: 2, name: 'Property Partner', url: 'https://www.propertypartner.co' },
  { id: 3, name: 'Property Moose', url: 'https://propertymoose.co.uk' },
  { id: 4, name: 'Homegrown', url: 'https://www.homegrown.co.uk' },
  { id: 5, name: 'Realty Mogul', url: 'https://www.realtymogul.com' }
];


// Authenticate Google Drive API
const auth = new google.auth.GoogleAuth({
  keyFile: '/home/nk/Desktop/Code/picauto/credentials.json', // Path to your Google Cloud Platform service account credentials
  scopes: 'https://www.googleapis.com/auth/drive'
});

// Generate screenshots and save to Google Drive
async function generateAndSaveScreenshots() {
  const drive = google.drive({ version: 'v3', auth });

  for (const website of websites) {
    const options = {
      url: website.url,
      dimension: `${screenshotWidth}x${screenshotHeight}`,
      format: screenshotFormat,
      cacheLimit: '0',
      delay: '200',
      zoom: '100'
    };

    const apiUrl = screenshotmachine.generateScreenshotApiUrl(customerKey, '', options);
    const output = `screenshots/${website.id}_${website.name}.${screenshotFormat}`;

    const response = await screenshotmachine.readScreenshot(apiUrl);
    response.pipe(fs.createWriteStream(output));

    await uploadToGoogleDrive(drive, output, website);
    console.log(`Screenshot saved and uploaded for ${website.name}`);
  }
}

// Upload screenshot file to Google Drive
async function uploadToGoogleDrive(drive, filename, website) {
  const fileMetadata = {
    name: `${website.id}_${website.name}.${screenshotFormat}`,
    parents: [folderId]
  };

  const media = {
    mimeType: `image/${screenshotFormat}`,
    body: fs.createReadStream(filename)
  };

  await drive.files.create({
    resource: fileMetadata,
    media: media,
    fields: 'id, webViewLink'
  });
}

generateAndSaveScreenshots();