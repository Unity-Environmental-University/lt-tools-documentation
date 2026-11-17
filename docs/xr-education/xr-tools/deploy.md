# Deploy a test build

Use **FTP Deploy** to publish an XR web build to a test destination. Start
with a build folder that already runs locally.

1. Open **FTP Deploy** in the desktop app.
2. Choose the local build folder.
3. Choose a destination in the **test** group.
4. Enter the credentials for the destination.
5. Select **Upload build**.
6. After the upload finishes, open the test site and check that it loads
   the expected build and its assets.

The Rust backend validates the target and local build before uploading.
It uploads into a staging folder and promotes that folder after the upload
succeeds. When a previous build exists, the server keeps it during promotion
so recovery can restore it if a rename fails.

If the upload fails during a rename, read the recovery paths in the app's
error and confirm which build is live before retrying. If the TLS connection
fails, check that the configured host matches the certificate. The app requires
explicit FTPS with an encrypted data connection.
