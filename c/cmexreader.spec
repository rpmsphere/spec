Summary: CMEX epub reader
Name: cmexreader
Version: 0.1
Release: 1
License: GPL
Group: System/Utility
Source0: cmexreader-pkg.tgz
Source1: cmex.png

%description
epub viewer for CMEX.

%prep
%setup -q -n cmexreader-pkg

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%__install -Dm755 cmexreader $RPM_BUILD_ROOT%{_bindir}/%{name}
%__install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/cmex.png


# Install menu entry
mkdir -p %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CMEX ePub View
Name[zh_TW]=CMEX 電子書閱讀器
Comment=ePub viewer written for CMEX
Comment[zh_TW]=給 CMEX 編寫的電子書閱讀器
Categories=Application;Utility;
Exec=cmexreader
Terminal=false
Type=Application
Icon=cmex.png
Encoding=UTF-8
EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%exclude %{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/pixmaps/cmex.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri Mar 05 2010 Harry <bluebat@member.fsf.org> 0.1-1
- Initial build for OSSII

