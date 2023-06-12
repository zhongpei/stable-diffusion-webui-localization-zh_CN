all:
	cd stable-diffusion-webui-localization-zh_Hans; git pull
	python merge.py
clone:
	git clone	git@github.com:hanamizuki-ai/stable-diffusion-webui-localization-zh_Hans.git
