py -m PyInstaller --noconsole --icon=media/ideatron.ico --noconfirm ideatron.py
cd dist/Ideatron
mkdir media
cd media
mkdir icons
cd ..
cd ..
cd ..
xcopy "media" "dist/Ideatron/media"
xcopy "media/icons" "dist/Ideatron/media/icons"