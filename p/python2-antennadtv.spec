Name: 	 	python2-antennadtv
Summary: 	A dvb-t tuner for linux desktops
Version: 	0.11.01.20
Release: 	3.1
Source:		https://sourceforge.net/projects/antenna-dtv/files/antenna-dtv_%{version}-0_all/antenna-dtv-%{version}.tar
URL:		https://antenna-dtv.sourceforge.net/
License:	GPLv2
Group:		Applications/Multimedia
BuildRequires: python-devel
BuildArch:	noarch
Requires: pygtk2-libglade
Requires: w_scan
Requires: xine-ui
Requires: alevt
Requires: dvb-apps

%description
Antenna is a full featured tool to see what's going on in the sky. Antenna can:
* Scan the sky for new services
* Continuosly monitor signal status
* Search through known channels and tune
* Search and manage favorite channels
* See what's on (i.e. listen to radios and watch tvs)
* Record streams while watching
* Read teletext

%prep
%setup -q -n antenna-dtv-%{version}
sed -i '/scripts/d' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc README 
%python2_sitelib/antennadtv
%python2_sitelib/*.egg-info

%changelog
* Mon Jan 27 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.01.20
- Rebuilt for Fedora
