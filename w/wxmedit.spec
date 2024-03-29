Name: wxmedit
License: GPL
Group: Applications/Editors
Summary: A cross-platform Text/Hex Editor
Version: 3.2
Release: 1
Source0: wxMEdit-%{version}.tar.gz
URL: https://wxmedit.github.io/
BuildRequires: gcc-c++ automake
BuildRequires: boost-devel
BuildRequires: wxGTK2-devel
BuildRequires: libicu-devel
BuildRequires: libcurl-devel

%description
wxMEdit is a fork of MadEdit with bug fixes and improvements.

%prep
%setup -q -n wxMEdit-%{version}
#sed -i -e 's|UnicodeString|icu::UnicodeString|g' -e 's|BreakIterator|icu::BreakIterator|g' src/xm/uutils.h src/dialog/wxm_enumeration_dialog.* src/wxm/wx_icu.h
#sed -i 's|LocalUCharsetDetectorPointer|icu::LocalUCharsetDetectorPointer|g' src/xm/encdet.cpp
#sed -i -e 's|boost/tr1|boost|' -e 's|std::tr1|std|' src/wxmedit/*.h src/dialog/*.cpp
sed -i 's|FALSE|0|' src/xm/encoding/multibyte.cpp

%build
#alternatives --set wx-config /usr/bin/wx-config-3.0
%configure
make

%install
%__rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}*
%{_datadir}/icons/hicolor/*/*/wxmedit.*

%changelog
* Sun Jul 23 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
