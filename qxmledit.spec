%global debug_package %{nil}

Name:           qxmledit
Version:        0.9.7
Release:        4.1
Summary:        Simple XML editor and XSD viewer
Group:          Editors
License:        GPLv2
URL:            http://code.google.com/p/qxmledit
Source:         https://dl.sourceforge.net/project/qxmledit/QXmlEdit-%{version}/%{name}-%{version}-1-src.tgz
BuildRequires:  qt-devel

%description
QXmlEdit is a simple XML editor written in qt4. Its main features are unusual
data visualization modes, nice XML manipulation and presentation.
It can split very big XML files into fragments, and compare XML files.
It is one of the few graphical Open Source XSD viewers.

%prep
%setup -q -n %{name}-%{version}-1
#sed -i 's|-Werror|-std=c++98|' src/sessions/QXmlEditSessions.pro

%build
qmake-qt4 QXmlEdit.pro
make \
	QXMLEDIT_INST_DATA_DIR=%{_datadir}/%{name} \
	QXMLEDIT_INST_DIR=%{_bindir} \
	QXMLEDIT_INST_DOC_DIR=%{_datadir}/doc/%{name}-%{version} \
	QXMLEDIT_INST_LIB_DIR=%{_libdir} \
	QXMLEDIT_INST_INCLUDE_DIR=%{_includedir}/%{name}

%install
make INSTALL_ROOT=%{buildroot} install
rm -fr %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.so

#mv %{buildroot}%{_bindir}/QXmlEdit %{buildroot}%{_bindir}/%{name}

%__install -Dm 0644 ./src/images/icon.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%__install -Dm 0644 ./src/images/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%__mkdir_p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=QXmlEdit
GenericName=Simple XML Editor and XSD viewer
Comment=Simple XML Editor and XSD viewer
Type=Application
Exec=%{name} %u
Icon=%{name}
Categories=Qt;Utility;TextEditor;
MimeType=text/xml;application/xml;
StartupNotify=true
Terminal=false
EOF

cp AUTHORS COPYING DISTRIBUTING GPLV3.txt LGPLV3.txt INSTALL NEWS README ROADMAP TODO %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%{_datadir}/doc/%{name}-%{version}
%{_bindir}/%{name}
%{_libdir}/libQXmlEdit*.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
* Tue Jul 11 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.7
- Rebuild for Fedora
* Mon Oct 21 2013 umeabot <umeabot> 0.8.7-2.mga4
+ Revision: 540747
- Mageia 4 Mass Rebuild
* Wed Oct 09 2013 lmenut <lmenut> 0.8.7-1.mga4
+ Revision: 494267
- update to 0.8.7
  + update summury and description
  + remove obsoletes patches
* Sun Jan 13 2013 umeabot <umeabot> 0.8.3.1-2.mga3
+ Revision: 380143
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Nov 15 2012 fwang <fwang> 0.8.3.1-1.mga3
+ Revision: 318121
- drop unused fiiles
- update file list
- new version 0.8.3.1
* Fri Mar 02 2012 lmenut <lmenut> 0.7.2-1.mga2
+ Revision: 216962
- update to 0.7.2
  + rediff patches 1 & 2
  + add patch 3 to fix format string error
* Sat Jan 21 2012 lmenut <lmenut> 0.6.2-1.mga2
+ Revision: 199146
- update to 0.6.2
* Tue Jan 03 2012 lmenut <lmenut> 0.6.1-1.mga2
+ Revision: 189833
- update to 0.6.1
* Sun Dec 11 2011 lmenut <lmenut> 0.5.4-1.mga2
+ Revision: 180631
- imported package qxmledit
