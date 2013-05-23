GREEN="\033[32;5;148m"
RED="\033[31;5;148m"
CLOSING="\033[39m"

echo "Deploying to AppEngine, application:your-app-id version: dev"
appcfg.py --oauth2 update . --application=your-app-id --version=dev
OUT=$?
if [ $OUT -ne 0 ];then
  echo "${RED}ERROR${CLOSING}: Deploying Failed."
  exit 127
fi

echo -e "${GREEN}SUCCESS${CLOSING}: Everything looks awesome."



