Name:		editra
Version:	0.7.20
Release:	5.1
Summary:	A developer's text editor
Group:		Editors
License:	GPLv2+
URL:		https://editra.org/
Source0:	https://editra.org/uploads/src/Editra-%{version}.tar.gz
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-wxpython
#Requires:	python2-wxpython
BuildArch:      noarch

%description
Editra is a cross-platform text editor with an implementation that
focuses on creating an easy to use interface and features that aid
in code development. Currently it supports syntax highlighting and
variety of other useful features for over 60 programming languages.

%prep
%setup -qn Editra-%{version}

%build
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-purelib=%{python2_sitearch}
chmod a+r $RPM_BUILD_ROOT%{python2_sitearch}/*/*
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Editra
MimeType=text/plain;
GenericName=Editra
GenericName[es]=Editra
Comment=Text Editor
Comment[es]=Editor de Texto
Exec=editra
Icon=/%{python2_sitearch}/Editra/pixmaps/editra.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Development;TextEditor;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python2_sitearch}/Editra-%{version}-py*.egg-info
%{python2_sitearch}/Editra/*

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.20
- Rebuilt for Fedora
* Sat Sep 08 2012 vaci0 <vaci0> 0.7.12-1.mga3
+ Revision: 289698
-Updated to version 0.7.12
* Sat Aug 04 2012 vaci0 <vaci0> 0.7.08-2.mga3
+ Revision: 278405
- Fixed Categories Development in .desktop file
* Sat Jul 28 2012 vaci0 <vaci0> 0.7.08-1.mga3
+ Revision: 275113
- Updated to 0.7.08 version
- Removed obsolete defattr call in %%files
- Simplified file instalation with one line for all files in %%files.
* Tue Jul 10 2012 juancho <juancho> 0.7.01-1.mga3
+ Revision: 269184
- Added back BR wxPythonGTK
- Changed macro %%{python2_sitelib} for %%{python2_sitearch} so it builds on x86_64
- Removed all .mo individual entries in %%files for a generic one for all of them
- Renamed spec to lower case
- Renamed to lower case
  + vaci0 <vaci0>
    - Fix BuildRequires
    - Fix path to icon in .desktop
    - Fix name in lowercase
    - imported package Editra
