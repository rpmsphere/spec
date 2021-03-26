%define	_cachedir	/var/cache
%define	py_ver		%(python -c 'import sys; print sys.version[:3]')

# Set default freevo parameters
%define	display		x11

Summary:	Open-source digital video jukebox 
Name:		freevo
Version:	1.9.2b2
Release:	1
License:	GPLv2+
Group:		Video
URL:		http://freevo.sourceforge.net/
# TODO: Upgrade to the stalled 2.x devel tree
Source0:	https://github.com/freevo/freevo1/archive//%{name}-%{version}.tar.bz2
Source1:	redhat-boot_config
Source2:	local_conf.py
Source4:	firebird.py
Source7:	freevo_tvgrab
Source8:	mute
Source9:	unmute
Source10:	fonts.tgz
Source11:	freevo-mail-0.6.tgz
Source100:	%{name}.rpmlintrc
Patch0:		%{name}-1.9.2b2-build.patch
Patch1:		%{name}-webserver.patch
Patch2:		%{name}-boot.patch
Patch3:		%{name}-volume.patch
Patch4:		%{name}-1.9.2b2-pillow.patch
Patch5:		%{name}-1.9.2b2-fix-revision.patch
BuildRequires:	docbook-utils
BuildRequires:	wget
BuildRequires:	pkgconfig(python) >= 2.4
BuildRequires:	pygame >= 1.5
BuildRequires:	python-beautifulsoup >= 3.0.3
BuildRequires:	python-imaging >= 1.1.4
BuildRequires:	python-imdb
BuildRequires:	python-kaa-base
BuildRequires:	python-kaa-imlib2
BuildRequires:	python-kaa-metadata
BuildRequires:	python-numpy
BuildRequires:	python2-twisted
BuildRequires:	python2-setuptools

BuildArch:	noarch

Requires:	cdparanoia
Requires:	lsdvd >= 0.16
Requires:	libjpeg-progs
Requires:	mencoder
Requires:	mplayer
Requires:	pygame >= 1.5
Requires:	python-beautifulsoup >= 3.0.3
Requires:	python-imaging >= 1.1.4
Requires:	python-imdb
Requires:	python-kaa-base
Requires:	python-kaa-metadata
Requires:	python-kaa-imlib2
Requires:	python-lirc >= 0.0.4
Requires:	python-numeric >= 2.31
Requires:	python-osd
Requires:	python-twisted >= 1.3.0
Requires:	tvtime
Requires:	util-linux
Requires:	vorbis-tools
Requires:	xine-ui
Requires:	xmltv-grabbers
Requires:	xmltv

Requires(pre,post):		rpm-helper
Requires(post,postun):	desktop-file-utils

%description
This is a Linux application that turns a PC with a TV capture card and/or
TV-out into a standalone multimedia jukebox/VCR. It builds on other
applications such as xine, mplayer, tvtime and mencoder to play and record
video and audio.

%files -f %{name}.lang
%doc COPYING ChangeLog FAQ README local_conf.py.example TODO
%doc Docs/NOTES Docs/*.dtd Docs/plugins
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/applications/rosa-%{name}.desktop
%config(noreplace) /etc/cron.weekly/*
# Hu, even those files are need, tmpwatch will delete it !!
#%%attr(777,root,root) %%dir /tmp/%%{name}/Videos
#%%attr(777,root,root) %%dir /tmp/%%{name}/
# TODO: Verify if 777 is the right mask... rpmlint complains loudly
%attr(777,root,root) %dir %{_cachedir}/%{name}
%attr(777,root,root) %dir %{_cachedir}/%{name}/audio
%attr(777,root,root) %dir %{_cachedir}/%{name}/thumbnails
%attr(777,root,root) %dir %{_cachedir}/xmltv
%attr(777,root,root) %dir %{_cachedir}/xmltv/logos
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/rc.d/init.d/*
%{python_sitelib}/%{name}
%{python_sitelib}/*.egg-info
%{_defaultdocdir}/%{name}-%{version}

#-----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
#patch3 -p0
%patch4 -p1
%patch5 -p1

# Install our fonts
cd share/fonts/
tar -xvzf %{SOURCE10}

# Clean ups
find . -name CVS | xargs rm -rf
find . -name ".cvsignore" |xargs rm -f
find . -name "*.pyc" |xargs rm -f
find . -name "*.pyo" |xargs rm -f
#find . -name "*.py" |xargs chmod 644 *


%build
#Building freevo
#Available rpmbuild rebuild options: --without: use_sysapps
./autogen.sh
%py2_build


%install
mkdir -p %{buildroot}%{_sysconfdir}/freevo
# The following is needed to let RPM know that the files should be backed up
touch %{buildroot}%{_sysconfdir}/freevo/freevo.conf

# Install boot scripts
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_bindir}
install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/freevo/boot_config

# TODO: Verify if 777 is the right mask... rpmlint complains loudly
mkdir -p %{buildroot}%{_cachedir}/freevo
mkdir -p %{buildroot}%{_cachedir}/freevo/{thumbnails,audio}
mkdir -p %{buildroot}%{_cachedir}/xmltv/logos
chmod 777 %{buildroot}%{_cachedir}/{freevo,freevo/thumbnails,freevo/audio,xmltv,xmltv/logos}

mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}/etc/freevo
mkdir -p %{buildroot}%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}/tmp/%{name}/Videos
mkdir -p %{buildroot}/etc/cron.weekly

python2 setup.py install %{?_without_compile_obj:--no-compile} --root=%{buildroot} --record=INSTALLED_FILES

#cp -av contrib/examples contrib/fbcon contrib/xmltv %%{buildroot}%%{_prefix}/contrib
cp -av contrib/lirc/ %{buildroot}%{_datadir}/%{name}/contrib/
install -m 755 freevo %{buildroot}%{_datadir}/%{name}
install -m 755 freevo_config.py %{buildroot}%{_datadir}/%{name}
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/freevo/local_conf.py
install -m 755 %{SOURCE7} %{buildroot}/etc/cron.weekly
install %{SOURCE8} %{buildroot}%{_datadir}/%{name}
install %{SOURCE9} %{buildroot}%{_datadir}/%{name}

#######################
#Installing Initscripts
#######################
#install -m 755 boot/freevo %%{buildroot}%%{_sysconfdir}/rc.d/init.d
#install -m 755 boot/freevo_dep %%{buildroot}%%{_sysconfdir}/rc.d/init.d
install -m 755 boot/recordserver %{buildroot}%{_initrddir}/freevo_recordserver
install -m 755 boot/webserver %{buildroot}%{_initrddir}/freevo_webserver
#install -m 755 boot/recordserver_init %%{buildroot}%%{_bindir}/freevo_recordserver_init
#install -m 755 boot/webserver_init %%{buildroot}%%{_bindir}/freevo_webserver_init

####################
# Installing Plugins
####################
# Mailer Plugin
#cd $RPM_BUILD_DIR/%%{name}-%%{version}/*mail*
#PYTHONPATH=../build/lib python2 setup.py install %%{?_without_compile_obj:--no-compile} --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
#
install %{SOURCE4} %{buildroot}%{python_sitelib}/freevo/plugins

###############
# Copying icons
###############
install -D -m 644 share/icons/misc/freevo_app.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -m 644 share/icons/misc/freevo_app.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 644 share/icons/misc/freevo_app.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

#####################
# Adding a menu entry
#####################
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/rosa-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;TV;Player;Recorder;
EOF

####################
# About locales... #
####################
find %{buildroot}%{_datadir}/locale -name "*.po" -exec rm -f {} \;
%find_lang %{name}

####################
# Cleaning
####################
rm -rf %{buildroot}%{_datadir}/fxd/web*
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/INSTALL
chmod -x %{buildroot}%{_datadir}/%{name}/freevo_config.py
chmod +x %{buildroot}%{_datadir}/%{name}/htdocs/help/*.rpy
chmod -x %{buildroot}%{_datadir}/%{name}/skins/osd/*.fxd
chmod +x %{buildroot}%{python_sitelib}/%{name}/audio/plugins/mpdclient2.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/helpers/{audioscrobbler-errors,daemon,imdbpy,inputhelper}.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/helpers/{install,makelircrc,makelogos,makestationlist,remote}.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/helpers/{schedulefavorites,tv_grab,vtrelease,webserver}.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/plugins/zoneminder.py
chmod -x %{buildroot}%{python_sitelib}/%{name}/plugins/firebird.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/util/{feedparser,youtube_dl}.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/video/plugins/applelib.py
chmod +x %{buildroot}%{python_sitelib}/%{name}/video/commdetectclient.py

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python_sitelib}/%{name}/*/*.py
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/htdocs/help/*.rpy
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/htdocs/downloadurl %{buildroot}%{_datadir}/%{name}/%{name}
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{python_sitelib}/%{name}/video/plugins/applelib.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python_sitelib}/%{name}/audio/plugins/mpdclient2.py

%pre
%_pre_useradd %{name} %{_datadir}/%{name} /bin/bash

%post
rm -rf /var/log/freevo 2>/dev/null

#Determining TV_NORM & CHANNEL_LIST from local clock
ZONE=`grep "ZONE" /etc/sysconfig/clock | sed -e "s/^ZONE\=\(.*\)\/\(.*\)/\1/g"`
CITY=`grep "ZONE" /etc/sysconfig/clock | sed -e "s/^ZONE\=\(.*\)\/\(.*\)/\2/g"`
TV_NORM="ntsc"
CHANNEL_LIST="us-cable"

if [ "${CITY}" = "Paris" ]; then
TV_NORM="secam"
CHANNEL_LIST="france"
else
        if [ "${ZONE}" = "Europe" ]; then
                TV_NORM="pal"
                CHANNEL_LIST="europe-west"
        fi
fi

#Determining current X configuration
RESOLUTION=`xdpyinfo 2>/dev/null | grep dimensions | awk '{ print $2 }'`
case $RESOLUTION in
	"1280x800")
		RESOLUTION="1024x768";
		;;
	"1280x720")
		RESOLUTION="1024x768";
		;;
	"1680x1050")
		RESOLUTION="1280x1024";
		;;
	"1400x1050")
		RESOLUTION="1280x1024";
		;;

	"1920x1200")
		RESOLUTION="1600x1200";
		;;
	"")	
		RESOLUTION="800x600";
		;;
esac

# Copy old local_conf.py to replace dummy file
cd %{_datadir}/%{name}
./freevo setup --geometry=$RESOLUTION --display=%{display} \
        --tv=${TV_NORM} --chanlist=${CHANNEL_LIST} \
	%{!?_without_use_sysapps:--sysfirst} 

if [ ! -f /etc/freevo/lircrc ]; then
	ln -sf %{_datadir}/%{name}/contrib/lirc/pinnacle_PCTV /etc/freevo/lircrc
fi;
%_post_service freevo_webserver
%_post_service freevo_recordserver


%preun
%_preun_service freevo_recordserver
%_preun_service freevo_webserver


%postun
%_postun_userdel %{name}


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.2b2
- Rebuild for Fedora
* Sun Oct 15 2017 Giovanni Mariani <mc2374@mclink.it> 1.9.2b2-1
- (c243505) Updated to release 1.9.2 (beta2), rediffed P0 and P4, added P5 to fix build, added S100 to silence wrong rpmlint errors, fixed our .desktop file and remove many other rpmlint warnings
