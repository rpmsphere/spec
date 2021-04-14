%undefine _debugsource_packages
Summary: 	Character editor and training manager
Name: 		tegaki-train
Version: 	0.3.1
Release: 	1
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/%name-%version.tar.gz
URL: 		http://www.tegaki.org
BuildRequires:	python2-setuptools
Requires:	tegaki-pygtk
BuildArch:	noarch

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Tegaki Train
Comment=Character editor and training manager
Terminal=false
Icon=/usr/share/tegaki/icons/handwriting.png
Type=Application
Exec=%{name}
Categories=Development;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{python2_sitelib}/tegaki*
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 592784
- import tegaki-train
