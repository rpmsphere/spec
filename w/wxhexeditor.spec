%undefine _debugsource_packages
%define _name wxHexEditor

Name:           wxhexeditor
Summary:        A hex editor for view/edit huge files and devices
Version:        0.24
Release:        1
License:        GPL
Group:          Editors
URL:            https://wxhexeditor.sourceforge.net/
Source0:        https://sourceforge.net/projects/wxhexeditor/files/wxHexEditor/v%{version}%20Beta/%{_name}-v%{version}-src.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig automake
BuildRequires:  wxGTK-devel

%description
wxHexEditor is another GUI hex editor for open HUGE files and devices
in linux mainland. Designed for reverse engineering binary files.
With wxHexEditor, you can edit huge files and devices like (hdd/sdd).
This programs supports tagging parts of the file for taking notes and
make it easier reverse engineer huge binary files.

%prep
%setup -q -n %{_name}
sed -i 's|-fopenmp|-fopenmp -fPIC|' Makefile
sed -i 's|$CFLAGS -Wall|$CFLAGS -Wall -fPIC|' udis86/configure.ac
sed -i 's|-Wall|-Wall -fPIC|' mhash/configure
sed -i 's|abs(|fabs(|' src/HexEditorCtrl/HexEditorCtrl.h
cp /usr/share/automake-*/config.guess mhash

%build
PYTHON=/usr/bin/python3 CFLAGS=-fPIC make WXCONFIG=wx-config

%install
%__install -D -m 755 %{_name} %{buildroot}%{_bindir}/%{_name}
%__install -D -m 644 resources/%{_name}.png %{buildroot}%{_datadir}/pixmaps/%{_name}.png
%__install -D -m 644 resources/%{_name}.desktop %{buildroot}%{_datadir}/applications/%{_name}.desktop

%files
%doc docs/*
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.png

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.24
- Rebuilt for Fedora
* Sat Mar 19 2011 Erdem U. Altinyurt <spamjunkeater@gmail.com> - 0.10-0
- fixed OpenSUSE 11.4 compilation
* Fri Apr 23 2010 Erdem U. Altinyurt <spamjunkeater@gmail.com> - 0.09-0
- closing to final
* Mon Feb 9 2009 Erdem U. Altinyurt <spamjunkeater@gmail.com> - 0.08-0
- initial release of rpm
